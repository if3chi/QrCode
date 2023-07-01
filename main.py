from src import argumentor, qr

def main():
    args = argumentor.Argumentor().get_argument()
    
    generator = qr.CodeGenerator(args.text, args.filename, args.folder, args.version,
        args.box_size, args.border, args.format, args.fill_color, args.bg, args.method, args.svg_bg)
    
    generator.create()

if __name__ == '__main__': main()
    