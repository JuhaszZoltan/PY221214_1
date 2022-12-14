from random import randint

karakterek:str = 'abcdefgh1234567890_'

jelszo:str = ''
for n in range(8):
    jelszo += karakterek[randint(0, len(karakterek)-1)]

print(f'a generált jelszó: {jelszo}')