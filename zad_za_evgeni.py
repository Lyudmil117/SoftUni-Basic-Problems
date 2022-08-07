

while True:
    name = input('name: ')
    if name == 'exit':
            print('bye')
            break
    elif name.isnumeric():  #taka se kazva 'ako vuvedenoto chislo e nomer'-->print(int(name ** 2)
        print(int(name) ** 2)
    else:
        print(name)


#PROMENLIVA.ISNUMERIC() ---> AKO PROMENLIVATA E CHISLO,A NE STRING...., NAPRAVI NESTO SI....

