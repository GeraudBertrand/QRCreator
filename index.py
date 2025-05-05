import argparse
import sys

from file import read_file,save_qrfile
from generation import generate_qr_code
from ui import launch_ui


def run_cli_mode(file_path:str, name:str):
    try:
        img = generate_qr_code(file_path)
        path = save_qrfile(img, name)
        print(f"QR Code généré et sauvegardé : {path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Générateur de QR Code")
    parser.add_argument("-f", "--file", type=str, help="Chemin du fichier à encoder")
    parser.add_argument("-n", "--name", type=str, help="Nom du fichier de sortie")
    parser.add_argument("--cli", action="store_true", help="Mode ligne de commande (sans interface graphique)")

    args = parser.parse_args()

    if args.cli:
        if not args.file or not args.name:
            print("Erreur: Vous devez spécifier un fichier et un nom de sortie.")
            sys.exit(1)
        run_cli_mode(args.file, args.name)
    else:
        launch_ui()


if __name__ == "__main__":
    main()
   


