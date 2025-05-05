import qrcode;
from PIL import Image

def generate_qr_code(data):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    if(len(data) > 3000):
        raise ValueError("Data is too long to be encoded in a QR code.")
    
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # S'assurer qu'on a une image RGB de type PIL.Image.Image
    if not isinstance(img, Image.Image):
        img = img.convert("RGB")

    return img

