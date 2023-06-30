import os

def get_output_path(self) -> str:
    if self._is_svg:
        self.save_dir =os.path.join(self.save_dir, 'svgs')

    os.makedirs(self.save_dir, exist_ok=True)

    return os.path.join(self.save_dir, f"{self.filename}.{self.image_format}")
    
def message(self, code: (int|None)):
    msg = f"{'SVG ' if self._is_svg else ''}QR Code saved as {self.filename} in folder: {self.save_dir}." \
        if code == 1 else "Operation Unsuccessful"
    print(msg)

def set_version(version: int)->int:
    return 4 if version > 26 else version