from . import Operasi_input 
# file txt
DB_NAME = "data.txt"

# Dictionary template database
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis": 255*" ",
    "tahun":"yyyy"
}

# funsi cek database
def init_console():
    # menggunakan exeption

    try:
        # jika database tersedia
        with open(DB_NAME,"r") as file:
            print("Database tersedia, init done!")
    except:
        # jika tidak tersedia maka akan dibuatkan database bertipe txt 
        print("Database tidak ditemukan, silahkan membuat database baru")
        # memanggil fungsi dari file operasi_input
        Operasi_input.create_first_data()