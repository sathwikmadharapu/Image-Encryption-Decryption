# Image Encryption and Decryption Tool

This tool allows you to securely encrypt and decrypt image files using AES-GCM encryption. It supports a variety of image formats and uses a password to generate a cryptographic key for encryption and decryption.

## Features

- Encrypt and decrypt images using a password.
- Supports multiple image formats including JPEG,PNG,BMP
- Saves encrypted data with salt, nonce, and image metadata.
- Decrypts encrypted images back to their original format.

## Requirements

- Python 3.x
- Required libraries (can be installed via `requirements.txt`):

## Virtual Envirolment
Create it
```bash
python3 -m venv myenv
```


Activate it 
```bash
source myenv/bin/activate ##For mac
```
```bash
.\myenv\Scripts\Activate ##For windows
```

## Installation
1.  Clone the repository:
   ```bash
git clone https://github.com/sathwikmadharapu/Image-Encryption-Decryption.git
cd Image-Encryption-Decryption
```

2. Install required Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1.  Encrypt an Image
   To encrypt an image, run the following command:
```bash
python main.py encrypt <image> <password> <encrypted_file>
```
* Example Usage:
```bash
python main.py encrypt images.png  "t%h1@0biI{4}M01Tfq" encrypted_image.enc  
```

   **The password should be in quotes either ('') or (" "), This helps if any special or space character is included in the password.**
   
 **The output file should preferably have the .enc extension to indicate that it's an encrypted file (this is recommended but not mandatory).**

2. Decrypt an Image
        To decrypt an encrypted image, use the following command:
```bash
python main.py decrypt <encrypted_file> <password> <decrypted_image>
```
* Example Usage:
```bash
python main.py decrypt encrypted_image.enc "t%h1@0biI{4}M01Tfq" decrypted_image.png
```

 **It is advisable to specify the image format (e.g., .png, .jpg) in the name of the decrypted image file.The code throws error with some file formats**

## How It Works

* Encryption
  1. The image is read and converted into a byte array
  2. A key is derived from the password using PBKDF2 with a random salt.
  3. The image byte array is encrypted using AES-GCM with a random nonce.
  4. The encrypted image, along with metadata (salt, nonce, dimensions, and format), is saved to a file.
* Decryption
  1. The encrypted file is read and the salt, nonce, dimensions, and image format are extracted.
  2. The password is used to derive the key.
  3. AES-GCM is used to decrypt the image data.
  4. The image is reconstructed using the decrypted data and saved to the specified output file.
