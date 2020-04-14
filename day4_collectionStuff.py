FHAIR = {}
FHAIR['first'] = "Fhair"
FHAIR["last"] = "NVOALSD"

SUSAN = {}
SUSAN['first'] = "Susan"
SUSAN["last"] = "NVOALSD"

people =[]
people.append(FHAIR)
people.append(SUSAN)
people.append({"first": "joko", "last": "widoddo"})
print(people)
print(people[0]["first"])

from array import array

kamus = array('f')
kamus.append(88)
kamus.append(34124)

print(kamus[1])