import qrcode

# ====== YOUR DETAILS ======
details =   "https://darshini807.github.io/qr-details-generator/"

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(details)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save Image
img.save("my_details_qr.png")

print("✅ QR Code generated successfully!")
