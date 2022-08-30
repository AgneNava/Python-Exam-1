# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def show_object_keys(y):
  a = list(y.values())
  return a

#print(show_object_keys(audi))

# Tomo atsakymai

def showObjectKeys(d):
  return d.values()

print(showObjectKeys(audi))

# 2

def showObjectKeys_2(d):
  values = []
  for value in d.values():
    values.append(value)
  return values

print(showObjectKeys_2(audi))
