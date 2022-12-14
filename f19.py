from random import randint

v:str = input('vezetékneved: ')
k:str = input('keresztneved: ')

un_1:str = f'{v[:2]}{k[:2]}'
print(f'ajánlott username #1: {un_1}')

un_2:str = f'{v[:2]}{k[len(k)-2:]}'
print(f'ajánlott username #2: {un_2}')

un_3:str = f'{v[:3]}{randint(100, 999)}'
print(f'ajánlott username #3: {un_3}')