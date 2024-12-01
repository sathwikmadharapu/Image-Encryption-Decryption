from pathlib import Path
import struct
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from PIL import Image
import numpy as np
from utils import derive_key
from cryptography.exceptions import InvalidTag

def decrypt_image(encrypted_path: Path, password: str, output_path: Path):
    try:
        with open(encrypted_path, 'rb') as file:
            data = file.read()

        # Extract salt, nonce, dimensions, format, and encrypted data
        salt = data[:16]
        nonce = data[16:28]
        dimensions = struct.unpack("III", data[28:40])  # Read height, width, channels
        format_length = struct.unpack("I", data[40:44])[0]  # Read format length
        image_format = data[44:44 + format_length].decode('utf-8')  # Read and decode format
        encrypted_image = data[44 + format_length:]  # Remaining data is encrypted image

        # Derive key
        key = derive_key(password, salt)

        # Decrypt image bytes
        aesgcm = AESGCM(key)
        image_bytes = aesgcm.decrypt(nonce, encrypted_image, None)

        # Reconstruct image using dynamic dimensions
        height, width, channels = dimensions
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image = Image.fromarray(image_array.reshape((height, width, channels)))

        # Automatically determine the correct extension for the output file
        if not output_path.suffix:
            # If no extension is provided, use the image format as the extension
            output_path = output_path.with_suffix(f".{image_format.lower()}")

        # Save the image in its original format
        image.save(output_path, format=image_format)

        print(f"Image decrypted and saved to {output_path}")

    except InvalidTag:
        print("Error: Decryption failed. The password might be incorrect or the file is corrupted.")