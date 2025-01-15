def main():
    data =[]
    while True:
        nim = input("Masukkan NIM :")
        nama = input("Maukan Nama :")
        data.append(nim,nama)
        if input("Tambah lagi?(ya/tidak) :").lower()!='ya':
            break
    print("Data Mahasiswa")
    for i,(nim,nama)in enumerate(data):
        print(f"NIM: {nim}Nama: {nama}")
if __name__ == "__main__":
    main()