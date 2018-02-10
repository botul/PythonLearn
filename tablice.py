
#LISTY = []

#lista produktów
produkty = ["mleko", "ser", "chleb"]
print(produkty)
#print(type(produkty))
produkty.append("szynka")
produkty.append("mleko")
print(produkty)
m = produkty.count("mleko")
print(m)

wiecej_produktow = ["majonez", "jajka", "chleb"]
produkty.extend(wiecej_produktow)
print(produkty)

#usuwanie
produkty.pop(1)
#metoda pop usuwa element listy o podanym indeksie

produkty.remove("mleko")
#metoda remove usuwa produkt o podanej nazwie

#TUPLE - ()
#tupli nie można edytować
#metody są ograniczone
prod2 = ("Stale","mleko", "ser", "chleb")
print(prod2)

#SLOWNIKI - {}
person = {"wiek":20, "imie": "Anna", "nazwisko": "Kowalska"}
print(person["imie"])
print(person["nazwisko"])

person.get("wzrost", 170)
keys = person.keys()
print(keys)


