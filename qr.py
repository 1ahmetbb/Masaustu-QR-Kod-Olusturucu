import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode


def qr_olustur():
    url = url_girdi.get()

    if url:
        qr_url = pyqrcode.create(url)
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG Dosyalari", "*.svg")])

        if dosya_yolu:
            qr_url.svg(dosya_yolu, scale=8)
            durum_etiketi.config(text="QR Kod olusturuldu ve kaydedildi.")
        

uygulama_penceresi = tk.Tk()
uygulama_penceresi.title("Qr Kod Olustucu")

label = tk.Label(uygulama_penceresi, text='URL Girin:')
url_girdi = tk.Entry(uygulama_penceresi, width=40)
button = tk.Button(uygulama_penceresi, text='QR Kod Olustur', command=qr_olustur)
durum_etiketi = tk.Label(uygulama_penceresi, text='')

label.grid(row=0, column=0, padx=10, pady=10)
url_girdi.grid(row=0, column=1, padx=10, pady=10)
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
durum_etiketi.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


uygulama_penceresi.mainloop()