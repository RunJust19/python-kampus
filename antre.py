import os
import queue


class myQueque:
    def __init__(self):
        self.items = queue.Queue()

    def isEmpty(self):
        return self.items.empty()
    
    def qAdd(self, item):
        self.items.put(item)

    def qOut(self):
        if not self.items.empty():
            return self.items.get()
        else:
            return "No Antrian Kosong"
        
    def size(self):
        return self.items.qsize()
    
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system('cls')
            print("==========================")
            print("*     KELOMPOK 6 UTS     *")
            print("==========================")
            print("1. Masuk Antrian")
            print("2. Keluar Antrian")
            print("3. Cek Antrian")
            print("4. Banyak Antrian")
            print("5. Keluar Antrian")
            print("==========================")
            pilihan = str(input("Silahkan masukan pilihan anda: "))
            if (pilihan == "1"):
                os.system('cls')
                obj = str(input("Masukan NIM: "))
                self.qAdd(obj)
                print(f"{obj} telah masuk antrian")
                i = input("")
            elif(pilihan == "2"):
                os.system("cls")
                keluar = self.qOut()
                if keluar != "No Antrian Kosong":
                    print(f"{keluar} Keluar Antrian")
                else:
                    print("Antrian Kosong")
                i = input("")
            elif(pilihan == "3"):
                os.system('cls')
                print(self.isEmpty()) 
                i = input("")
            elif(pilihan == "4"):
                os.system("cls")
                print(f"panjang dari antrian adalah: {str(self.size())}")
                i = input("")
            elif(pilihan == "5"):
                os.system('cls')
                print("ARIGATO KARENA SUDAH MENGGUNAKAN PROGRAM INI")
                print("PLEASE TEKAN ENTER UNTUK OUT THE PROGRAM")
                print("SEMOGA HARIMU KAMIS TERUS")
                print(quit())
            else:
                pilih = "n"

if __name__ == "__main__":
    q = myQueque()
    q.mainmenu()

        
