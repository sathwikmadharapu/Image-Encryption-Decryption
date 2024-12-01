from pathlib import Path
import argparse
from encryptor import encrypt_image
from decryptor import decrypt_image

def main():
    parser = argparse.ArgumentParser(description="Image Encryption and Decryption Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Encryption subcommand
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt an image")
    encrypt_parser.add_argument("input", help="Path to the input image")
    encrypt_parser.add_argument("password", help="Password for encryption")
    encrypt_parser.add_argument("output", help="Path to save the encrypted file")

    # Decryption subcommand
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt an image")
    decrypt_parser.add_argument("input", help="Path to the encrypted file")
    decrypt_parser.add_argument("password", help="Password for decryption")
    decrypt_parser.add_argument("output", help="Path to save the decrypted image")

    args = parser.parse_args()

    # Convert the string paths to Path objects using pathlib
    input_path = Path(args.input)
    output_path = Path(args.output)

    if args.command == "encrypt":
        encrypt_image(input_path, args.password, output_path)
    elif args.command == "decrypt":
        decrypt_image(input_path, args.password, output_path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
