import re

while True:
    print('Podaj adres IP do sprawdzenia')
    address = input()
    if re.match('^\d\d\d.\d\d\d.\d\d\d.\d\d\d$', address):
        print ("Podano adres IP:" + address)
    else:
        print ('Nieprawidłowa składnia adresu')
