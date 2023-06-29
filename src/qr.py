import os

import qrcode

class CodeGenerator:
    def __init__(self, text: str, filename: str, save_dir="./output", version=1, box_size=10, border=4, image_format='png', fill_color="black", back_color="white"):
        self.text = text
        self.filename = filename
        self.save_dir = save_dir
        self.version = self._set_version(version)
        self.box_size = box_size
        self.border = border
        self.image_format = image_format
        self.fill_color = fill_color
        self.back_color = back_color

    def create(self):
        qr = qrcode.QRCode(
            version=self.version, error_correction=qrcode.constants.ERROR_CORRECT_L, 
            box_size=self.box_size, border=self.border
        )
        qr.add_data(self.text)
        qr.make(fit=True)

        image = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
        image.save(self._get_output_path())

        self._message()
        

    def _get_output_path(self) -> str:
        os.makedirs(self.save_dir, exist_ok=True)

        return os.path.join(self.save_dir, f"{self.filename}.{self.image_format}")
    
    def _message(self):
        print(f"QR Code saved as {self.filename} in folder: {self.save_dir}.")

    def _set_version(self, version: int)->int:
        return 4 if version > 26 else version
    