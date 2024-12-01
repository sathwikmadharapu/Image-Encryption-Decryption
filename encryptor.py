from pathlib import Path
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from PIL import Image
import numpy as np
from utils import derive_key
import struct
def encrypt_image(input_image: Path, password: str, output_path: Path):
    img = Image.open(input_image)
    image_array = np.array(img)
    height, width, channels = image_array.shape
    image_format = img.format  # Get the format (e.g., 'JPEG', 'PNG')

    # Flatten image data
    image_bytes = image_array.tobytes()

    # Generate salt and derive key
    salt = os.urandom(16)
    key = derive_key(password, salt)

    # Encrypt the image
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    encrypted_data = aesgcm.encrypt(nonce, image_bytes, None)

    # Save salt, nonce, dimensions, format length, format, and encrypted data
    format_encoded = image_format.encode('utf-8')
    with open(output_path, 'wb') as file:
        file.write(salt)
        file.write(nonce)
        file.write(struct.pack("III", height, width, channels))
        file.write(struct.pack("I", len(format_encoded)))
        file.write(format_encoded)
        file.write(encrypted_data)

    print(f"Image encrypted and saved to {output_path}")