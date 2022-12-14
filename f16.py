# karakterek:list[chr] = ['r', 'f', 'a', 's', 'w', 'q', 'b', 'a']
# karakterek.sort()
# print(karakterek)

szo:str = input('írj be egy szót: ')
karakter_lista:list[chr] = list[chr](szo)
karakter_lista.sort()
szo = '\0'.join(karakter_lista)
print(szo)