import argparse

class Argumentor:
    def get_argument(self):
        parser = argparse.ArgumentParser(description='Generate QR Code')
        parser.add_argument('text', type=str, help='Text to encode in QR Code')
        parser.add_argument('filename', type=str, help='Output filename for the QR Code image')
        parser.add_argument('--folder', type=str, action="store", default="./output")
        parser.add_argument('--box-size', type=int, default=10, help='Box size (pixels)')
        parser.add_argument('--border', type=int, default=4, help='Border size (modules)')
        parser.add_argument('--format', type=str, default='png', help='Output image format')
        parser.add_argument('--fill-color', type=str, default='black', help='QR Code fill color')
        parser.add_argument('--bg', type=str, default='white', help='QR Code background color')

        return parser.parse_args()