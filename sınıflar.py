import pyodbc  # SQL Server ile bağlantı kurmak için kullanılacak kütüphane

# Bağlantı dizesi
connection_string = "Driver={SQL Server 16.0.1000};Server=ZehraYARDIMCI;Database=GemiTakipDB;Uid=sa;Pwd=zehra30;"

class Gemiler:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, seri_numarasi, adi, agirlik, yapim_yili, tur, maks_agirlik=None):
        # Veritabanına yeni bir gemi eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Gemiler (seri_numarasi, adi, agirlik, yapim_yili, tur, maks_agirlik) VALUES (?, ?, ?, ?, ?, ?)",
                           (seri_numarasi, adi, agirlik, yapim_yili, tur, maks_agirlik))
            conn.commit()
            conn.close()
            print("Gemi başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, gemi_id):
        # Veritabanından bir gemiyi silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Gemiler WHERE gemi_id = ?", (gemi_id,))
            conn.commit()
            conn.close()
            print("Gemi başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def güncelle(self, gemi_id, **kwargs):
        # Veritabanında bir gemiyi güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            update_query = "UPDATE Gemiler SET "
            for key, value in kwargs.items():
                update_query += f"{key} = ?, "
            update_query = update_query[:-2]  # Son virgülü kaldır
            update_query += " WHERE gemi_id = ?"
            values = list(kwargs.values()) + [gemi_id]
            cursor.execute(update_query, tuple(values))
            conn.commit()
            conn.close()
            print("Gemi başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, gemi_id):
        # Belirli bir gemiyi veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Gemiler WHERE gemi_id = ?", (gemi_id,))
            gemi = cursor.fetchone()
            conn.close()
            if gemi:
                return gemi
            else:
                print("Belirtilen gemi bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None
class YolcuGemileri:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, gemi_id, yolcu_kapasitesi, maks_agirlik):
        # Veritabanına yeni bir yolcu gemisi eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO YolcuGemileri (gemi_id, yolcu_kapasitesi, maks_agirlik) VALUES (?, ?, ?)",
                           (gemi_id, yolcu_kapasitesi, maks_agirlik))
            conn.commit()
            conn.close()
            print("Yolcu gemisi başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, gemi_id):
        # Veritabanından bir yolcu gemisi silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM YolcuGemileri WHERE gemi_id = ?", (gemi_id,))
            conn.commit()
            conn.close()
            print("Yolcu gemisi başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def güncelle(self, gemi_id, yolcu_kapasitesi=None, maks_agirlik=None):
        # Veritabanında bir yolcu gemisinin özelliklerini güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            update_query = "UPDATE YolcuGemileri SET "
            if yolcu_kapasitesi is not None:
                update_query += "yolcu_kapasitesi = ?, "
            if maks_agirlik is not None:
                update_query += "maks_agirlik = ?, "
            update_query = update_query[:-2]  # Son virgülü kaldır
            update_query += " WHERE gemi_id = ?"
            values = []
            if yolcu_kapasitesi is not None:
                values.append(yolcu_kapasitesi)
            if maks_agirlik is not None:
                values.append(maks_agirlik)
            values.append(gemi_id)
            cursor.execute(update_query, tuple(values))
            conn.commit()
            conn.close()
            print("Yolcu gemisi başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, gemi_id):
        # Belirli bir yolcu gemisini veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM YolcuGemileri WHERE gemi_id = ?", (gemi_id,))
            yolcu_gemisi = cursor.fetchone()
            conn.close()
            if yolcu_gemisi:
                return yolcu_gemisi
            else:
                print("Belirtilen yolcu gemisi bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class PetrolTankerleri:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, gemi_id, petrol_kapasitesi, maks_agirlik):
        # Veritabanına yeni bir petrol tankerı eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO PetrolTankerleri (gemi_id, petrol_kapasitesi, maks_agirlik) VALUES (?, ?, ?)",
                           (gemi_id, petrol_kapasitesi, maks_agirlik))
            conn.commit()
            conn.close()
            print("Petrol tankerı başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, gemi_id):
        # Veritabanından bir petrol tankerı silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM PetrolTankerleri WHERE gemi_id = ?", (gemi_id,))
            conn.commit()
            conn.close()
            print("Petrol tankerı başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def güncelle(self, gemi_id, petrol_kapasitesi=None, maks_agirlik=None):
        # Veritabanında bir petrol tankerının özelliklerini güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            update_query = "UPDATE PetrolTankerleri SET "
            if petrol_kapasitesi is not None:
                update_query += "petrol_kapasitesi = ?, "
            if maks_agirlik is not None:
                update_query += "maks_agirlik = ?, "
            update_query = update_query[:-2]  # Son virgülü kaldır
            update_query += " WHERE gemi_id = ?"
            values = []
            if petrol_kapasitesi is not None:
                values.append(petrol_kapasitesi)
            if maks_agirlik is not None:
                values.append(maks_agirlik)
            values.append(gemi_id)
            cursor.execute(update_query, tuple(values))
            conn.commit()
            conn.close()
            print("Petrol tankerı başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, gemi_id):
        # Belirli bir petrol tankerını veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM PetrolTankerleri WHERE gemi_id = ?", (gemi_id,))
            petrol_tankerı = cursor.fetchone()
            conn.close()
            if petrol_tankerı:
                return petrol_tankerı
            else:
                print("Belirtilen petrol tankerı bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class KonteynerGemileri:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, gemi_id, konteyner_kapasitesi, maks_agirlik):
        # Veritabanına yeni bir konteyner gemisi eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO KonteynerGemileri (gemi_id, konteyner_kapasitesi, maks_agirlik) VALUES (?, ?, ?)",
                           (gemi_id, konteyner_kapasitesi, maks_agirlik))
            conn.commit()
            conn.close()
            print("Konteyner gemisi başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, gemi_id):
        # Veritabanından bir konteyner gemisi silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM KonteynerGemileri WHERE gemi_id = ?", (gemi_id,))
            conn.commit()
            conn.close()
            print("Konteyner gemisi başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def güncelle(self, gemi_id, konteyner_kapasitesi=None, maks_agirlik=None):
        # Veritabanında bir konteyner gemisinin özelliklerini güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            update_query = "UPDATE KonteynerGemileri SET "
            if konteyner_kapasitesi is not None:
                update_query += "konteyner_kapasitesi = ?, "
            if maks_agirlik is not None:
                update_query += "maks_agirlik = ?, "
            update_query = update_query[:-2]  # Son virgülü kaldır
            update_query += " WHERE gemi_id = ?"
            values = []
            if konteyner_kapasitesi is not None:
                values.append(konteyner_kapasitesi)
            if maks_agirlik is not None:
                values.append(maks_agirlik)
            values.append(gemi_id)
            cursor.execute(update_query, tuple(values))
            conn.commit()
            conn.close()
            print("Konteyner gemisi başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, gemi_id):
        # Belirli bir konteyner gemisini veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM KonteynerGemileri WHERE gemi_id = ?", (gemi_id,))
            konteyner_gemisi = cursor.fetchone()
            conn.close()
            if konteyner_gemisi:
                return konteyner_gemisi
            else:
                print("Belirtilen konteyner gemisi bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class SeferDurumu:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, durum_id, durum_adi):
        # Veritabanına yeni bir sefer durumu eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SeferDurumu (durum_id, durum_adı) VALUES (?, ?)",
                           (durum_id, durum_adi))
            conn.commit()
            conn.close()
            print("Sefer durumu başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, durum_id):
        # Veritabanından bir sefer durumu silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SeferDurumu WHERE durum_id = ?", (durum_id,))
            conn.commit()
            conn.close()
            print("Sefer durumu başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def güncelle(self, durum_id, durum_adi):
        # Veritabanında bir sefer durumunun adını güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("UPDATE SeferDurumu SET durum_adı = ? WHERE durum_id = ?", (durum_adi, durum_id))
            conn.commit()
            conn.close()
            print("Sefer durumu başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, durum_id):
        # Belirli bir sefer durumunu veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM SeferDurumu WHERE durum_id = ?", (durum_id,))
            sefer_durumu = cursor.fetchone()
            conn.close()
            if sefer_durumu:
                return sefer_durumu
            else:
                print("Belirtilen sefer durumu bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class Seferler:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, durum_id, sefer_turu, yola_cikis_tarihi, donus_tarihi, limanlar):
        # Veritabanına yeni bir sefer eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Seferler (durum_id, sefer_turu, yola_cikis_tarihi, donus_tarihi) VALUES (?, ?, ?, ?)",
                           (durum_id, sefer_turu, yola_cikis_tarihi, donus_tarihi))
            sefer_id = cursor.execute("SELECT SCOPE_IDENTITY()").fetchval()  # Eklenen seferin ID'sini al
            for liman in limanlar:
                cursor.execute("INSERT INTO SeferLimanlar (sefer_id, liman_adi) VALUES (?, ?)",
                               (sefer_id, liman))
            conn.commit()
            conn.close()
            print("Sefer başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, sefer_id):
        # Veritabanından bir seferi silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Seferler WHERE sefer_id = ?", (sefer_id,))
            cursor.execute("DELETE FROM SeferLimanlar WHERE sefer_id = ?", (sefer_id,))
            conn.commit()
            conn.close()
            print("Sefer başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def güncelle(self, sefer_id, **kwargs):
        # Veritabanında bir seferi güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            update_query = "UPDATE Seferler SET "
            for key, value in kwargs.items():
                update_query += f"{key} = ?, "
            update_query = update_query[:-2]  # Son virgülü kaldır
            update_query += " WHERE sefer_id = ?"
            values = list(kwargs.values()) + [sefer_id]
            cursor.execute(update_query, tuple(values))
            conn.commit()
            conn.close()
            print("Sefer başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, sefer_id):
        # Belirli bir seferi veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Seferler WHERE sefer_id = ?", (sefer_id,))
            sefer = cursor.fetchone()
            conn.close()
            if sefer:
                return sefer
            else:
                print("Belirtilen sefer bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class SeferGemiler:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, sefer_id, gemi_id):
        # Veritabanına yeni bir sefer gemisi eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SeferGemiler (sefer_id, gemi_id) VALUES (?, ?)",
                           (sefer_id, gemi_id))
            conn.commit()
            conn.close()
            print("Sefer gemisi başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, sefer_id, gemi_id):
        # Veritabanından bir sefer gemisi silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SeferGemiler WHERE sefer_id = ? AND gemi_id = ?", (sefer_id, gemi_id))
            conn.commit()
            conn.close()
            print("Sefer gemisi başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, sefer_id, gemi_id):
        # Belirli bir sefer gemisini veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM SeferGemiler WHERE sefer_id = ? AND gemi_id = ?", (sefer_id, gemi_id))
            sefer_gemisi = cursor.fetchone()
            conn.close()
            if sefer_gemisi:
                return sefer_gemisi
            else:
                print("Belirtilen sefer gemisi bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class Limanlar:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, liman_adi, ulke, nufus, pasaport_gerekli_mi, demirleme_ucreti):
        # Veritabanına yeni bir liman eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Limanlar (liman_adi, ulke, nufus, pasaport_gerekli_mi, demirleme_ucreti) VALUES (?, ?, ?, ?, ?)",
                           (liman_adi, ulke, nufus, pasaport_gerekli_mi, demirleme_ucreti))
            conn.commit()
            conn.close()
            print("Liman başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, liman_id):
        # Veritabanından bir limanı silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Limanlar WHERE liman_id = ?", (liman_id,))
            conn.commit()
            conn.close()
            print("Liman başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def güncelle(self, liman_id, **kwargs):
        # Veritabanında bir limanı güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            update_query = "UPDATE Limanlar SET "
            for key, value in kwargs.items():
                update_query += f"{key} = ?, "
            update_query = update_query[:-2]  # Son virgülü kaldır
            update_query += " WHERE liman_id = ?"
            values = list(kwargs.values()) + [liman_id]
            cursor.execute(update_query, tuple(values))
            conn.commit()
            conn.close()
            print("Liman başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, liman_id):
        # Belirli bir limanı veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Limanlar WHERE liman_id = ?", (liman_id,))
            liman = cursor.fetchone()
            conn.close()
            if liman:
                return liman
            else:
                print("Belirtilen liman bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class PotansiyelUgranacakLimanlar:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, liman_adi, ulke):
        # Veritabanına yeni bir potansiyel uğranacak liman eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO PotansiyelUgranacakLimanlar (liman_adi, ulke) VALUES (?, ?)",
                           (liman_adi, ulke))
            conn.commit()
            conn.close()
            print("Potansiyel uğranacak liman başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, liman_id):
        # Veritabanından bir potansiyel uğranacak limanı silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM PotansiyelUgranacakLimanlar WHERE liman_id = ?", (liman_id,))
            conn.commit()
            conn.close()
            print("Potansiyel uğranacak liman başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, liman_id):
        # Belirli bir potansiyel uğranacak limanı veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM PotansiyelUgranacakLimanlar WHERE liman_id = ?", (liman_id,))
            liman = cursor.fetchone()
            conn.close()
            if liman:
                return liman
            else:
                print("Belirtilen potansiyel uğranacak liman bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None
class Personel:
    def __init__(self, connection_string, tablo_adi):
        self.connection_string = connection_string
        self.tablo_adi = tablo_adi

    def ekle(self, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans=None, gorev=None):
        # Veritabanına yeni bir personel eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {self.tablo_adi} (ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans, gorev) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans, gorev))
            conn.commit()
            conn.close()
            print("Personel başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, personel_id):
        # Veritabanından bir personeli silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.tablo_adi} WHERE {self.tablo_adi}_id = ?", (personel_id,))
            conn.commit()
            conn.close()
            print("Personel başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def güncelle(self, personel_id, **kwargs):
        # Veritabanında bir personeli güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            update_query = f"UPDATE {self.tablo_adi} SET "
            for key, value in kwargs.items():
                update_query += f"{key} = ?, "
            update_query = update_query[:-2]  # Son virgülü kaldır
            update_query += f" WHERE {self.tablo_adi}_id = ?"
            values = list(kwargs.values()) + [personel_id]
            cursor.execute(update_query, tuple(values))
            conn.commit()
            conn.close()
            print("Personel başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, personel_id):
        # Belirli bir personeli veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.tablo_adi} WHERE {self.tablo_adi}_id = ?", (personel_id,))
            personel = cursor.fetchone()
            conn.close()
            if personel:
                return personel
            else:
                print("Belirtilen personel bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class Kaptanlar(Personel):
    def __init__(self, connection_string):
        super().__init__(connection_string, "Kaptanlar")

    def ekle(self, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans):
        # Veritabanına yeni bir kaptan eklemek için kullanılacak metod
        super().ekle(ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans)

    def güncelle(self, kaptan_id, lisans):
        # Veritabanında bir kaptanın lisans bilgisini güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("UPDATE Kaptanlar SET lisans = ? WHERE kaptan_id = ?", (lisans, kaptan_id))
            conn.commit()
            conn.close()
            print("Kaptanın lisansı başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

class Mürettebat(Personel):
    def __init__(self, connection_string):
        super().__init__(connection_string, "Mürettebat")

    def ekle(self, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, görev):
        # Veritabanına yeni bir mürettebat eklemek için kullanılacak metod
        super().ekle(ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, görev)

    def güncelle(self, muv_id, görev):
        # Veritabanında bir mürettebatın görev bilgisini güncellemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("UPDATE Mürettebat SET görev = ? WHERE muv_id = ?", (görev, muv_id))
            conn.commit()
            conn.close()
            print("Mürettebatın görevi başarıyla güncellendi.")
        except Exception as e:
            print("Hata:", str(e))

class SeferKaptanMürettebat:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, sefer_id, kaptan_id, muv_id):
        # Veritabanına yeni bir sefer kaptanı ve mürettebatı ilişkisi eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SeferKaptanMürettebat (sefer_id, kaptan_id, muv_id) VALUES (?, ?, ?)",
                           (sefer_id, kaptan_id, muv_id))
            conn.commit()
            conn.close()
            print("Sefer kaptanı ve mürettebatı ilişkisi başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, sefer_kaptan_muv_id):
        # Veritabanından bir sefer kaptanı ve mürettebatı ilişkisi silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SeferKaptanMürettebat WHERE sefer_kaptan_muv_id = ?", (sefer_kaptan_muv_id,))
            conn.commit()
            conn.close()
            print("Sefer kaptanı ve mürettebatı ilişkisi başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, sefer_kaptan_muv_id):
        # Belirli bir sefer kaptanı ve mürettebatı ilişkisini veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM SeferKaptanMürettebat WHERE sefer_kaptan_muv_id = ?", (sefer_kaptan_muv_id,))
            ilişki = cursor.fetchone()
            conn.close()
            if ilişki:
                return ilişki
            else:
                print("Belirtilen sefer kaptanı ve mürettebatı ilişkisi bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None
class SeferKaptanlar:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, sefer_id, kaptan_id):
        # Veritabanına yeni bir sefer kaptanı ilişkisi eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SeferKaptanlar (sefer_id, kaptan_id) VALUES (?, ?)",
                           (sefer_id, kaptan_id))
            conn.commit()
            conn.close()
            print("Sefer kaptanı ilişkisi başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, sefer_id, kaptan_id):
        # Veritabanından bir sefer kaptanı ilişkisi silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SeferKaptanlar WHERE sefer_id = ? AND kaptan_id = ?", (sefer_id, kaptan_id))
            conn.commit()
            conn.close()
            print("Sefer kaptanı ilişkisi başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, sefer_id, kaptan_id):
        # Belirli bir sefer kaptanı ilişkisini veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM SeferKaptanlar WHERE sefer_id = ? AND kaptan_id = ?", (sefer_id, kaptan_id))
            ilişki = cursor.fetchone()
            conn.close()
            if ilişki:
                return ilişki
            else:
                print("Belirtilen sefer kaptanı ilişkisi bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class SeferMürettebat:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, sefer_id, muv_id):
        # Veritabanına yeni bir sefer mürettebat ilişkisi eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SeferMürettebat (sefer_id, muv_id) VALUES (?, ?)",
                           (sefer_id, muv_id))
            conn.commit()
            conn.close()
            print("Sefer mürettebat ilişkisi başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, sefer_id, muv_id):
        # Veritabanından bir sefer mürettebat ilişkisi silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SeferMürettebat WHERE sefer_id = ? AND muv_id = ?", (sefer_id, muv_id))
            conn.commit()
            conn.close()
            print("Sefer mürettebat ilişkisi başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, sefer_id, muv_id):
        # Belirli bir sefer mürettebat ilişkisini veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM SeferMürettebat WHERE sefer_id = ? AND muv_id = ?", (sefer_id, muv_id))
            ilişki = cursor.fetchone()
            conn.close()
            if ilişki:
                return ilişki
            else:
                print("Belirtilen sefer mürettebat ilişkisi bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None

class SeferLimanlar:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def ekle(self, sefer_id, liman_adi):
        # Veritabanına yeni bir sefer liman ilişkisi eklemek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO SeferLimanlar (sefer_id, liman_adi) VALUES (?, ?)",
                           (sefer_id, liman_adi))
            conn.commit()
            conn.close()
            print("Sefer liman ilişkisi başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def sil(self, sefer_id, liman_adi):
        # Veritabanından bir sefer liman ilişkisi silmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM SeferLimanlar WHERE sefer_id = ? AND liman_adi = ?", (sefer_id, liman_adi))
            conn.commit()
            conn.close()
            print("Sefer liman ilişkisi başarıyla silindi.")
        except Exception as e:
            print("Hata:", str(e))

    def getir(self, sefer_id, liman_adi):
        # Belirli bir sefer liman ilişkisini veritabanından getirmek için kullanılacak metod
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM SeferLimanlar WHERE sefer_id = ? AND liman_adi = ?", (sefer_id, liman_adi))
            ilişki = cursor.fetchone()
            conn.close()
            if ilişki:
                return ilişki
            else:
                print("Belirtilen sefer liman ilişkisi bulunamadı.")
                return None
        except Exception as e:
            print("Hata:", str(e))
            return None
