import qrcode

# ====== YOUR DETAILS ======
details =   """
Name: Priyadarshini 
Course: B.Tech (Artificial Intelligence & Data Science)
Year: 3rd Year
College: Your College Name
GitHub: https://github.com/Darshini807
Email: your_email@example.com
"""

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
