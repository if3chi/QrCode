import qrcode

data = "Jesus loves you."

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

qr.add_data(data)

qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")

image.save("info_qrcode.png")