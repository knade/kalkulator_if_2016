import random

# random.seed(39)

osoby = ['Rafał Kura','Piotr Sadziński','Wojciech Szafałowicz','Kuba Sokół (Es)','Marcin Naprawski',
'Łukasz Knade','Piotr Kucharski','Malwina Konieczna','Michał Kolasiński','Kuba Barć','Mateusz Tochowicz',
'Bartek Stroiński','Konrad Fuczkiewicz','Jan Kustoń','Paweł Szymkowiak','Adam Góralski','OSOBA_NIEZNANA_1',
'OSOBA_NIEZNANA_2']

dane = {1:'ANG',2:'ANG',3:'ANG',4:'ANG',5:'ANG',6:'ANG',7:'ANG',8:'ANG',9:'ANG',
10:'ANG',11:'ANG',12:'PL',13:'PL',14:'PL',15:'PL',16:'PL',17:'PL',18:'PL'}

wyniki = {}

for i in range(1, 19):
    osoba = random.choice(osoby)
    # print(osoba)
    osoby.remove(osoba)
    dmg_deck = random.choice(list(dane.keys()))
    # print(dmg_deck)
    del dane[dmg_deck]
    wyniki[osoba] = dmg_deck

print(wyniki)