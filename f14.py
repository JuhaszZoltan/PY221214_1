szo:str = input('írj be egy szót: ')
ekezet_nelkul:str = ''

ekezetes_betuk =      'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
ekezet_mentes_betuk = 'aeiooouuuAEIOOOUUU'

for k in szo:
    if k not in ekezetes_betuk:
        ekezet_nelkul += k
    else:
        i:int = ekezetes_betuk.index(k)
        ekezet_nelkul += ekezet_mentes_betuk[i]

print(ekezet_nelkul)