import qrcode

links = {
    "kinh_te_phat_trien": "https://github.com/StephenSouth13/Kinh_Te_Phat_Trien",
    "du_bao_kinh_te": "https://github.com/StephenSouth13/Du_Bao_Kinh_Te_-_Phan_Tich_Du_Lieu",
    "ppnc_kinh_te": "https://github.com/StephenSouth13/ppnc_monhoc_master"
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