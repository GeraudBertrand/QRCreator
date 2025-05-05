import chardet
from PIL import Image
import os

def read_file(file_path:str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
    
    with open(file_path, 'r', encoding=encoding) as f:
        data = f.read()
    return data


def save_qrfile(file:Image.Image, file_name:str, path:str = None) -> str:
    flag1 = False
    if( path is not None):
        if( os.path.exists(path)):
            path = os.path.join(path, f"{file_name}.png")
        else:
            print("Path does not exist, saving to default path")
            flag1 = True
    else:
        flag1 = True

    if(flag1):
        output_dir = os.path.join(os.path.dirname(__file__), "output")
        os.makedirs(output_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas
        path = os.path.join(output_dir, f"{file_name}.png")

    file.save(path)
    print(f"File saved to: {path}")
    return path


def add_logo(qr_img:Image.Image, logo_path:str) -> Image.Image:
    if(logo_path is None):
        return qr_img
    
    logo = Image.open(logo_path)
    logo_size = int(min(qr_img.size) * 0.5)
    logo = logo.resize((logo_size, logo_size))

    pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
    qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

    return qr_img