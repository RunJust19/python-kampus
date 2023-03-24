import numpy as np
import os
os.system('cls')

# program rekrusif hasil pemangkatan
print(5*"-","Rekrusif Pemangkatan".upper(),5*"-","\n")
def pangkat(a1,p1) :
    
    print(f'Hasil dari {a1} pangkat {p1} = {(a1 ** p1)}')
    if (p1 == 0):
        #if (p1 == p1):
        return 1
    else:
        #return pangkat(a1,p1-1) 
        return pangkat(a1,p1-1) * a1 
        
    
pangkat(3,2)
#(pangkat(3,5))

# program rekrusif menghitung nila terbesar dan terkecil dari sebuah array
print("\n",5*"-","Rekrusif menghitung nilai teerbesar dan terkecil dari sebuah array ".upper(),5*"-","\n")    

## Tugaas 2

num = np.array([1,2,10,4,5])
print(f"array = {num}")

# nilai max
def nilai_max(number) :
    nilai = number[0]

    if len(number) > 1:
        nbig = nilai_max(number[1:])
        if nbig > nilai:
           nilai=nbig

    return nilai

# nilai_min
def nilai_min(number) :
    nilai = number[0]

    if len(number) > 1:
        nbig = nilai_max(number[1:])
        if nbig < nilai:
           nilai = nbig

    return nilai

print(f"nilai max = {nilai_max(num)}")
print(f"nilai min = {nilai_min(num)}")

