import tkinter as tk
from tkinter import messagebox
from sınıflar import Gemiler
import pyodbc
connection_string = "Driver={SQL Server 16.0.1000};Server=ZehraYARDIMCI;Database=GemiTakipDB;Uid=sa;Pwd=zehra30;"

class GemiForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Gemi Bilgi Formu")

        # Gemi ID
        self.label_gemi_id = tk.Label(root, text="Gemi ID:")
        self.label_gemi_id.grid(row=6, column=0)
        self.entry_gemi_id = tk.Entry(root)
        self.entry_gemi_id.grid(row=6, column=1)

        # Gemi seri numarası
        self.label_seri_numarasi = tk.Label(root, text="Seri Numarası:")
        self.label_seri_numarasi.grid(row=0, column=0)
        self.entry_seri_numarasi = tk.Entry(root)
        self.entry_seri_numarasi.grid(row=0, column=1)

        # Gemi adı
        self.label_adi = tk.Label(root, text="Adı:")
        self.label_adi.grid(row=1, column=0)
        self.entry_adi = tk.Entry(root)
        self.entry_adi.grid(row=1, column=1)

        # Gemi ağırlık
        self.label_agirlik = tk.Label(root, text="Ağırlık:")
        self.label_agirlik.grid(row=2, column=0)
        self.entry_agirlik = tk.Entry(root)
        self.entry_agirlik.grid(row=2, column=1)

        # Gemi yapım yılı
        self.label_yapim_yili = tk.Label(root, text="Yapım Yılı:")
        self.label_yapim_yili.grid(row=3, column=0)
        self.entry_yapim_yili = tk.Entry(root)
        self.entry_yapim_yili.grid(row=3, column=1)

        # Gemi türü
        self.label_tur = tk.Label(root, text="Tür:")
        self.label_tur.grid(row=4, column=0)
        self.entry_tur = tk.Entry(root)
        self.entry_tur.grid(row=4, column=1)

        # Maksimum ağırlık
        self.label_maks_agirlik = tk.Label(root, text="Maksimum Ağırlık:")
        self.label_maks_agirlik.grid(row=5, column=0)
        self.entry_maks_agirlik = tk.Entry(root)
        self.entry_maks_agirlik.grid(row=5, column=1)

        # Ekleme Butonu
        self.button_ekle = tk.Button(root, text="Ekle", command=self.gemi_ekle)
        self.button_ekle.grid(row=7, column=0)

        # Güncelleme Butonu
        self.button_guncelle = tk.Button(root, text="Güncelle", command=self.gemi_guncelle)
        self.button_guncelle.grid(row=7, column=1)

        # Silme Butonu
        self.button_sil = tk.Button(root, text="Sil", command=self.gemi_sil)
        self.button_sil.grid(row=7, column=2)

    def gemi_ekle(self):
        seri_numarasi = self.entry_seri_numarasi.get()
        adi = self.entry_adi.get()
        agirlik = self.entry_agirlik.get()
        yapim_yili = self.entry_yapim_yili.get()
        tur = self.entry_tur.get()
        maks_agirlik = self.entry_maks_agirlik.get()

        # Veritabanına yeni bir gemi ekleme
        try:
            gemiler = Gemiler(connection_string)
            gemiler.ekle(seri_numarasi, adi, agirlik, yapim_yili, tur, maks_agirlik)
            messagebox.showinfo("Başarılı", "Gemi başarıyla eklendi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

    def gemi_guncelle(self):
        gemi_id = self.entry_gemi_id.get()
        if not gemi_id:
            messagebox.showerror("Hata", "Lütfen güncellenecek geminin ID'sini girin.")
            return

        adi = self.entry_adi.get()
        agirlik = self.entry_agirlik.get()
        yapim_yili = self.entry_yapim_yili.get()
        tur = self.entry_tur.get()
        maks_agirlik = self.entry_maks_agirlik.get()

        # Güncelleme işlemleri
        try:
            gemiler = Gemiler(connection_string)
            gemiler.güncelle(gemi_id, adi=adi, agirlik=agirlik, yapim_yili=yapim_yili, tur=tur,
                             maks_agirlik=maks_agirlik)
            messagebox.showinfo("Başarılı", "Gemi başarıyla güncellendi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

    def gemi_sil(self):
        gemi_id = self.entry_gemi_id.get()
        if not gemi_id:
            messagebox.showerror("Hata", "Lütfen silinecek geminin ID'sini girin.")
            return

        # Gemiyi silme işlemleri
        try:
            gemiler = Gemiler(connection_string)
            gemiler.sil(gemi_id)
            messagebox.showinfo("Başarılı", "Gemi başarıyla silindi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

def main():
    root = tk.Tk()
    form = GemiForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()





