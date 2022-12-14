szo_1:list[chr] = list(input('első szó: '))
szo_2:list[chr] = list(input('második szó: '))
szo_1.sort()
szo_2.sort()

if szo_1 == szo_2: print('a két szó anagramma')
else: print('ez a két szó nem anagramma')