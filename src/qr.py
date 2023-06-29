import os

import qrcode
import qrcode.image.svg

class CodeGenerator:
    _is_svg = False

    def __init__(self, text: str, filename: str, save_dir="./output", version=1, box_size=10, border=4, 
                 image_format='png', fill_color="black", back_color="white", method="basic"):
        self.data = text
        self.filename = filename
        self.save_dir = save_dir
        self.version = self._set_version(version)
        self.box_size = box_size
        self.border = border
        self.image_format = image_format
        self.fill_color = fill_color
        self.back_color = back_color
        self.method = method


    def create(self):
        self._is_svg = self.image_format.lower() == 'svg'
        
        if self._is_svg:
            status_code = self._create_svg_code()
        else:
            status_code = self._create_img_code()

        self._message(status_code)
        

    def _get_output_path(self) -> str:
        if self._is_svg:
            self.save_dir =os.path.join(self.save_dir, 'svgs')

        os.makedirs(self.save_dir, exist_ok=True)

        return os.path.join(self.save_dir, f"{self.filename}.{self.image_format}")
    
    def _message(self, code: (int|None)):
        msg = f"{'SVG ' if self._is_svg else ''}QR Code saved as {self.filename} in folder: {self.save_dir}." \
            if code == 1 else "Operation Unsuccessful"
        print(msg)

    def _set_version(self, version: int)->int:
        return 4 if version > 26 else version
    
    def _create_img_code(self) -> (int | None):
        try:
            qr = qrcode.QRCode(
                version=self.version, error_correction=qrcode.constants.ERROR_CORRECT_L, 
                box_size=self.box_size, border=self.border
            )
            qr.add_data(self.data)
            qr.make(fit=True)

            image = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
            
            image.save(self._get_output_path())
            return 1
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def _create_svg_code(self) -> (int | None):
        try:
            if self.method == 'basic':
                factory = qrcode.image.svg.SvgImage
            elif self.method == 'fragment':
                factory = qrcode.image.svg.SvgFragmentImage
            elif self.method == 'path':
                factory = qrcode.image.svg.SvgPathImage

            img = qrcode.make(self.data, image_factory = factory)

            img.save(self._get_output_path())

            return 1
        except Exception as e:
            print(f"An error occurred: {e}")
    