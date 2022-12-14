szo:str = input('írj be egy szót: ')
c:int = 0
for k in szo.lower():
    if k in 'aáeéiíoóöőuúüű': c += 1
print(f'magánhangzók száma: {c}')