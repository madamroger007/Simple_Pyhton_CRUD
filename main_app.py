import os
import CRUD as CRUD

if __name__=="__main__":
    # mendeteksi sistem operasi
    sistem_operasi = os.name
    match sistem_operasi:
            # untuk menghilangkan komen di atas terminal
            case "posix": os.system("clear") # os unix/posix
            case "nt": os.system("cls") # os window/nt
    # output       
    print("SELAMAT DATANG DI PROGRAM")
    print(" DATABASE PERPUSTAKAAN")       
    print(20*"=")

    # check database ada atau tidak
    CRUD.init_console()

    # perulangan menu program dengan while apabila true akan terus berulang   
    while(True):
        match sistem_operasi:
            # untuk menghilangkan komen di atas terminal
            case "posix": os.system("clear") # os unix/posix
            case "nt": os.system("cls") # os window/nt
        # output   
        print("SELAMAT DATANG DI PROGRAM")
        print(" DATABASE PERPUSTAKAAN")       
        print(20*"=")
        # output menu
        print(f"1. Read data ")
        print(f"2. Create data ")
        print(f"3. Update data ")
        print(f"4. Delete data ")
        print(f"5. keluar")
        
        # input memilih menu
        menu_user= input("coba pilih no menu :")
        
        print(20*"=")
        # match = menukar data yang sudah di input input dengan case
        match menu_user:
            case '1':CRUD.read_console() # memanggil fungsi read_console dalam package CRUD
            case '2':CRUD.create_console() # memanggil fungsi create_console dalam package CRUD
            case '3':CRUD.update_console() # memanggil fungsi update_console dalam package CRUD
            case '4':CRUD.delete_console() # memanggil fungsi delete_console dalam package CRUD
            case '5':break
            case _: print("Yang anda masukan salah")
        
        # menggunakan statement memilih lanjut atau tidak
        is_selesai = input("Apakah selesai (y/n) ?:")
        if is_selesai == 'y' or is_selesai== 'Y':
            break

    print("Program berakhir")