import androidhelper
import baca
import tambah

droid = androidhelper.Android()


def nav():
    droid.dialogCreateAlert("PILIHAN", " ")
    droid.dialogSetItems(["Membaca Soal","Menambah Soal","Play Quiz","Exit"])
    droid.dialogShow()
    menu=droid.dialogGetResponse().result['item']
    if menu==0:
        baca.lihat()
    elif menu==1:
         tambah.kedua()
    elif menu==2:
        import play
    elif menu==3:
        exit()
    else:
        print("gak")
        droid.dialogShow()