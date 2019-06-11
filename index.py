#Dilara Turhan BBY162 Programlama ve Algoritmalar
from tkinter import *
import tkinter.messagebox
class katalogum:
    def __init__(self,anasayfa):
        self.anasayfa = anasayfa
        anasayfa.title("Kütüphane Arşivi")
        anasayfa.configure(background="red")

        self.kitapları_listele = Button(anasayfa, text="Kitapları Listele",bg="red",fg="yellow",cursor="star",font="bold", command=self.kitaplari_listele)
        self.kitapları_listele.grid(row="1")

        self.kitap_ekle = Button(anasayfa, text="Kitap Ekle", bg="red",fg="yellow",cursor="star",font="bold",command = self.kitap_ekle)
        self.kitap_ekle.grid(row="2")

        self.kitap_ara = Button(anasayfa, text="Kitap Ara", bg="red",fg="yellow",cursor="star",font="bold",command=self.kitap_ara)
        self.kitap_ara.grid(row="3")

        self.cikis = Button(anasayfa, text ="Kapat", command=exit, fg="red", bg="yellow",cursor="man")
        self.cikis.grid(row="4")

    def kitap_ekle(self):
        global kitap_adi, yazar_adi, yy, pencere1
        pencere1 = Tk()
        baslik1 = pencere1.title("Kitap Kayıt Penceresi")
        pencere1.configure(background="red")

        kitap_adi= Entry(pencere1,width=27)
        kitap_adi.grid(column=2, row=3)
        yazar_adi = Entry(pencere1, width=27)
        yazar_adi.grid(column=2, row=4)
        yy = Entry(pencere1, width=27)
        yy.grid(column=2, row=8)
        self.kaydet = Button(pencere1, text= "Kaydet",command=self.kitap_kaydet, fg="red", bg="yellow")
        self.kaydet.grid(column=1, row=9)

        self.cıkıs = Button(pencere1 ,text = "Kapat", command=pencere1.destroy, fg="red", bg="yellow",cursor="man")
        self.cıkıs.grid(column=3, row=9)
        Label(pencere1,bg="red",fg="yellow", text='Kitap bilgilerini giriniz! ').grid(column=1, row=1)
        Label(pencere1,bg="red",fg="yellow", text='Kitap Adı: ').grid(column=1, row=3)
        Label(pencere1,bg="red",fg="yellow", text='Yazar Adı: ').grid(column=1, row=4)
        Label(pencere1,bg="red",fg="yellow", text='Yayın Yılı:').grid(column=1, row=8)
    def kitap_kaydet(self):
        kayit_sistemi = str((kitap_adi.get() + "=" + yazar_adi.get() + "=" + yy.get())+"\n")
        dosya= open("katalog.txt","a")
        for i in kayit_sistemi:
            dosya.write(i)
        dosya.close()
        tkinter.messagebox.showinfo('Mesaj', 'Kitap Başarıyla Eklendi..')
        command=pencere1.destroy()

    def kitaplari_listele(self):
        pencere2= Tk()
        baslik2 = pencere2.title("Kayıtlı Kitaplar")
        pencere2.configure(background="red")
        file = open("katalog.txt")
        data = file.read()
        file.close()

        kitap_liste = Label(pencere2, text=data,fg="yellow", bg="red")
        kitap_liste.pack()

        self.cıkıs = Button(pencere2 ,text = "Kapat", command=pencere2.destroy, fg="red", bg="yellow",cursor="man")
        self.cıkıs.pack()

    def kitap_ara(self):
        pencere3 = Tk()
        baslık4 = pencere3.title("Kitap arama penceresi")
        pencere3.configure(background="red")

        def kitap():
            pencere4 = Tk()
            baslik2 = pencere4.title("Aranılan Sonuç")
            pencere4.configure(background="red")
            dosya = open("katalog.txt", "r")
            veri = dosya.readlines()
            dosya = open("katalog.txt")
            aranan = input("Aramak istediğiniz bilgileri giriniz: ")
            aranan_varmi = dosya.read().find(aranan)

            if aranan_varmi != -1:
                print("var")
            else:
                print("yok")
            dosya.close()

        self.labelKitap = Label(pencere3, bg="red", fg="yellow", text="Kitap Aramak istiyorum ")
        self.labelKitap.grid(row=0, column=0)
        self.butonKitap = Button(pencere3, text="onay", bg="red", fg="yellow", cursor="star", font="bold",command=kitap)
        self.butonKitap.grid(row=0, column=2)
root = Tk()
yeniPencere = katalogum(root)
root.mainloop()