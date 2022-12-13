import qrcode
import image

qr=qrcode.QRCode(
    version=15,
    box_size=5,
    border=5
)

data="https://www.instagram.com/p/CmB-BkCjFoA/?igshid=YmMyMTA2M2Y="

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",backcolor="white")
img.save("Aniket.png")            