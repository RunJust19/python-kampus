import os
os.system('cls')

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data =data
        self.next_node = next_node
    
    # untuk mengmbil data dari node
    def get_data(self):
        return self.data
    
    # untuk mengmbil node berikutnya
    def get_next(self):
        return self.next_node
    
    # menentukan node berikutnya
    def set_next(self, new_next):
        self.next_node = new_next
        
        
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    
    #insert node baru 
    def insert(self, data):
        
        #Inisialisasi node baru
        new_node = Node(data)
        
        # tunjuk node berikutnya dari node head
        new_node.set_next(self.head)
        
        # dari head nunjuk ke node berikutnya
        self.head = new_node
        
    # menghitung panjang node
    def size(self):
        
        # membuat pointer node yang ditunjuk oleh head
        current = self.head
        count = 0
        
        # perulangan untuk menghitung node
        while current:
            count += 1
            current = current.get_next()
        return count
    
    # mencari data pada list
    def  search(self, data):
        # pointer untuk menunjuk node yang ditunjuk oleh head
        current = self.head
        found = False
        
        # perulangan untuk mencari
        while current and found is False:
            if current.get_data() == data:
                found == True
            else:
                current = current.get_next()
        return found
    
    # menghapus node
    def delete(self,data):
        current = self.head
        found = False
        previous = None
        while current and found is False:
            if current.get_data() == data:
                found == True
            else:
                current = current.get_next()
                previous = current
        if current is None:
            raise ValueError("data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())     
            
    # menampilkan data
    def showData(self):
        print("list data :\n Node -> Next Node")   
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            print(" --> ")
            print(current_node.next_node.data) if hasattr(current_node.next_node, "data") else None
            current_node = current_node.next_node
    
    def mainmenu(self):
        pilih = "y"
        while(pilih == "y"):
            print("1. insert Data")
            print("2. Delete Data")
            print("3. Cari Data")
            print("4. Panjang Data")
            print("5. show Data")
            print("6. Delete ALL")
            print(" Masih mau lanjut atau tidak ya/no")
            pilihan= str(input("\npilih yang mana, ayooo: "))
            if (pilihan == "1"):
                inp = str(input("Data yang ingin ditambahkan "))
                self.insert(inp)
            elif (pilihan =="2" ):
                inp = str(input("data yang ingin dihapus"))
                self.delete(inp)
            elif (pilihan =="3" ):
                inp = str(input("data yang ingin dicari"))
                status = self.search(inp)
                if status == True:
                    print("data ditemukan")
                else:
                    print("data tidak ditemukan")
            elif (pilihan =="4" ):
               print("panjang LL :" + str(self.size()))
            elif (pilihan == "5") :
                self.showData()
            elif (pilihan == "ya"):
                continue
            elif (pilihan == "no"):
                print("anda lelah")
                break
            else:
                pilih = "n"
                
# call class
if __name__ == "__main__":
    ll = LinkedList()
    ll.mainmenu()
