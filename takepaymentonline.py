import qrcode
upi_id= input("Enter a upi id=")
phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Names&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Names&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Names&mc=1234'

#create QR codes for each payment app
phonepe_qr= qrcode.make(phonepe_url)
paytm_qr= qrcode.make(paytm_url)
google_pay_qr= qrcode.make(google_pay_url)

#save the QR code to image file(optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

#display the QR code (you may need to install pil/pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()







