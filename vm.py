import time

def welcome():
    print('Welcome to KCC Vending Machine',end='')
    for i in range(1,5):
        time.sleep(0.5)
        print('-',end='')
    for i in range(1,5):
        time.sleep(0.5)
        print('>',end='')
    print('\n')
    
def menu():
    for item in options().values():
        print(item[0],item[1],' - Rs.',item[2],'per item')
    print('5 Exit')

def options():
    products = {'1':[1,"Good Day Biscuit",10],
                '2':[2,"Lays",20],
                '3':[3,"Thumbs Up Can",40],
                '4':[4,"Kurkure", 20]}
    return products