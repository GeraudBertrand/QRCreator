import qrcode;

def generate_qr_code(data, filename):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)




# give argument to main execution
# py index.py "https://www.example.com" "example_qr.png"
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python index.py <data> <filename>")
        sys.exit(1)

    data = sys.argv[1]
    filename = sys.argv[2]

    generate_qr_code(data, filename)
    print(f"QR Code generated and saved as {filename}")

