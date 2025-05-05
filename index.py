from generation import generate_qr_code
from file import save_qrfile


# give argument to main execution
# py index.py "https://www.example.com" "example_qr.png"
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python index.py <data> <filename>")
        sys.exit(1)

    data = sys.argv[1]
    filename = sys.argv[2]

    code_file = generate_qr_code(data, filename)
    print(f"QR Code generated as {filename}")

    # Save the QR Code image to a file using the file_download function
    # asking for the file name to be saved in the system
    file_name = input("Enter the file name to save the QR code (default: example_qr.png): ")
    save_qrfile(code_file, file_name)



