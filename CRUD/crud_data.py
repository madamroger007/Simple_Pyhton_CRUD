from numpy import number
from . import Operasi_input


# fungsi delete
def delete_console():
    # memanggil fungsi read
    read_console()
     # perulangan while = true
    while(True):
        print("Silahkan masukan nomor buku yang akan di delete")
        # input
        no_buku = int(input("Nomor Buku : "))
        # memanggi fungsi read(index=keyword,no_buku=argumen) atau **kwarg
        data_buku = Operasi_input.read(index=no_buku)
        # statement jika ada data_buku maka break
        if data_buku:
            # dipecah berdasarkan koma dengan split
            data_break = data_buku.split(",")
            pk=data_break[0]
            data_add =data_break[1]   
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

       

   
            # data yang ingin di didelete
            print("\n"+"="*100)
            print("Data yang akan di hapus")
            # (judul:.40) batas spasi 40
            print(f"1. judul\t: {judul:.40}")
            print(f"2. penulis\t: {penulis:.40}")
            print(f"3. tahun\t: {tahun:.4}")
            
            # input memilih data hapus
            is_selesai = input("Yakin akan di hapus? (y/n) ?:")
            if is_selesai == 'y' or is_selesai== 'Y':
                Operasi_input.delete(no_buku)
                break
        else:
            print("nomor tidak valid,silahkan masukan lagi")
    
    print("Data berhasil di hapus")


# fungsi update
def update_console():
    # memanggil fungsi read
    read_console()
    # perulangan while = true
    while(True):
        print("Silahkan masukan nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku : "))
        # memanggi fungsi read(index=keyword,no_buku=argumen) atau **kwarg
        data_buku = Operasi_input.read(index=no_buku)
        # statement jika ada data_buku maka break
        if data_buku:
            break
        else:
            print("nomor tidak valid,silahkan masukan lagi")
    
    # dipecah berdasarkan koma dengan split
    data_break = data_buku.split(",")
    pk=data_break[0]
    data_add=data_break[1]   
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    # perulangan
    while(True):
        # data yang ingin di update
        print("\n"+"="*100)
        print("Silahkan pilih data yang ingin di rubah")
        # (judul:.40) batas spasi 40
        print(f"1. judul\t: {judul:.40}")
        print(f"2. penulis\t: {penulis:.40}")
        print(f"3. tahun\t: {tahun:.4}")
        # input memilih data yang akan di edit
        user_opsi = input("pilih data[1,2,3]: ")
        print("\n"+"="*100)

        # match = menukar data yang sudah di input dengan case
        match user_opsi:
            case '1': judul = input("Judul\t: ")
            case '2': penulis = input("penulis\t: ")
            case '3':  
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
            # case default
            case _:print("index tidak cocok")     
        print("Data baru sudah di update")
        print(f"1. judul\t: {judul:.40}")
        print(f"2. penulis\t: {penulis:.40}")
        print(f"3. tahun\t: {tahun:.4}")   
        # menggunakan statement memilih lanjut atau tidak
        is_selesai = input("sudah updatenya (y/n) ?:")
        if is_selesai == 'y' or is_selesai== 'Y':
            break
    # setter ke fungsi update
    Operasi_input.update(no_buku,pk,data_add,tahun,judul,penulis) 

# fungsi create data
def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul =  input("Judul\t: ")
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
    # setter (untuk memberikan data ke fungsi create())
    Operasi_input.create(tahun,judul,penulis)
    print("\n berikut adalah data baru anda")
    
    # memanggil fungsi read()
    read_console()

# fungsi read data
def read_console():
    data_file = Operasi_input.read()
    # styling console
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
    
    # Header
    print("\n"+"="*100)
    # memberikan lebar contoh = (judul:40)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)


    # perulangan per Data
    # perbaris
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]

        # memberikan spasi dengan menambahkan tanda titik contoh (judul :.40)
        # index+1 supaya program dimulai pada no angka 1 
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:5}",end="")
    # Footer
    print("\n","="*100+"\n")

