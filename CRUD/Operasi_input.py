import os
from . import Database
from . Util import random_string
import time

# fungsi delete data
def delete(no_buku):
    try:
        with(open(Database.DB_NAME,'r')) as file:
            # untuk menghitung readlines yang akan di delete
            counter = 0
            while(True):
                # readline = dibaca per baris
                content = file.readline()
                    # statment len= panjang sbaris data == 0
                if len(content) == 0:
                    break
                    # untuk meng skip 1 buku yang ada di data no buku
                elif counter == no_buku - 1:
                    pass
                    # memindahkan data.txt di pindah ke data temporary
                else:
                        # membuat txt baru dan di append/tambahkan
                    with open("data_temp.txt",'a',encoding='utf-8') as temp_file:
                           # menuliskan as temp_file ke daa bairs
                        temp_file.write(content)

                    # menambah 1 baris    
                counter += 1
    except:
        print("database error")
    
    # buat data temporary me replace data.txt = DB_NAME
    os.rename("data_temp.txt",Database.DB_NAME)

# fungsi update data
def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()
    data["pk"] = pk
    data["date_add"] =  data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"]   = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"]   = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"

    panjang_data = len(data_str)

    try:
        # menggunakan r+ untuk menimpa di dalam database
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            # untuk memindahkan kursor panjang dikali no lalu dikurangi 1
            file.seek(panjang_data*(no_buku-1))
            # menuliskan ke data_str
            file.write(data_str)
    except:
        print("eror dalam update")   

# fungsi membuat data
def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string
    data["date_add"] =  time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"]   = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"]   = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    print(data_str)
    
   # menggunakan exception untuk menambah data  dengan append 'a'
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("gagal cok")


def create_first_data():
    # input database 
    penulis = input("Penulis :")
    judul =  input("Judul :")
    # supaya input dibacanya tipe data number dan tidak mengalami error
    # menggunakan try except
    while(True):
        try:
            tahun =  int(input("Tahun\t: "))
            # supaya pengetikan tahun sama dengan 4 dan tidak lebih dari 4
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus 4 angka,silakan masukan lagi(yyyy)")
            
        except:
            print("tahun harus number silahkan masukan tahun lagi")

    # membuat tamplate database
    # data ["pk"] mengambil dari dictionary dari tamplate di file database.py
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string
    data["date_add"] =  time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"]   = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"]   = tahun
    
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    print(data_str)
    
   # menggunakan exception untuk membuat atau menulis data dengan write 'a'
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan")
    
# fungsi ambil data untuk Read_data.py
# untuk update menggunakan **kwargs
def read(**kwargs):
    # menggunakan exception untuk membaca data
    try:
        with open(Database.DB_NAME,'r') as file:
            #readlines=perbaris
            content= file.readlines()
            # len= panjang baris di content
            jumlah_buku = len(content)
            if "index" in kwargs:
                # indeks list dictionary dengan kwargs (indeks dimulai dari 0) maka di kurang -1 biar memulai dari 1
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:                    
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database gagal")
        return False