import unittest
import os
from PIL import Image
from generation import generate_qr_code
from file import read_file, save_qrfile

class TestQRCodeGenerator(unittest.TestCase):

    def setUp(self):
        self.sample_file = "tests/sample.txt"
        self.sample_content = "Ceci est un test pour QR Code."
        self.qr_name = "test_qrcode"

        # Créer un fichier de test
        with open(self.sample_file, "w", encoding="utf-8") as f:
            f.write(self.sample_content)

    def test_read_file(self):
        content = read_file(self.sample_file)
        self.assertEqual(content.strip(), self.sample_content)

    def test_generate_qr_code(self):
        img = generate_qr_code(self.sample_content)
        self.assertIsInstance(img, Image.Image)

    def test_generate_qr_code_too_long(self):
        long_content = "A" * 4000
        with self.assertRaises(ValueError):
            generate_qr_code(long_content)

    def test_save_qrfile(self):
        img = generate_qr_code(self.sample_content)
        path = save_qrfile(img, self.qr_name)
        self.assertTrue(os.path.isfile(path))
        os.remove(path)  # nettoyage

    def test_save_qrfile_with_path(self):
        img = generate_qr_code(self.sample_content)
        output_dir = os.path.join(os.path.dirname(__file__), "output")
        os.makedirs(output_dir, exist_ok=True)
        path = save_qrfile(img, self.qr_name, output_dir)
        self.assertTrue(os.path.isfile(path))
        os.remove(path)



    def tearDown(self):
        os.remove(self.sample_file)


if __name__ == "__main__":
    unittest.main()