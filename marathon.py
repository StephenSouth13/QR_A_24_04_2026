import qrcode

links = {
    "Running Training Plan": "https://docs.google.com/spreadsheets/d/1EWHNd3Mx_DGCZk6hgws33e8MV2QZsHQKzcz9bowndIU/edit?usp=sharing"
}

for name, url in links.items():
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{name}.png")