# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "filterDogOwers" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filterAdults" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
  { "id": '1', "name": 'John Smith', "age": 20, "hasDog": True },
  { "id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False },
  { "id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True },
  { "id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False },
  { "id": '5', "name": 'Alex John', "age": 25, "hasDog": True },
  { "id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True },
  { "id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True },
  { "id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False },
  { "id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True },
]

# 1:

# def filter_dog_owners(x):
#   return x['hasDog'] == True

# has_dog = [d for d in users if filter_dog_owners(d)]

# print(has_dog)

# 2:

# def filter_adults(y):
#   return y['age'] >= 18

# adults = [d for d in users if filter_adults(d)]

# print(adults)

# Tomo atsakymai:

# Pirmas variantas

# def filterDogOwners(user_list):
#   dog_owners = []
#   for user in user_list:
#     if user['hasDog'] == True:
#       dog_owners.append(user)
#   return dog_owners


# def filterAdults(user_list):
#   adults = []
#   for user in user_list:
#     if user['age'] >= 18:
#       adults.append(user)
#   return adults

# print(filterDogOwners(users))
# print(filterAdults(users))

# Antras variantas

# def filterDogOwners_2(user_list):
#   dog_owners = [user for user in user_list if user['hasDog'] == True]
#   return dog_owners

# def filterAdults_2(user_list):
#   adults = [user for user in user_list if user['age'] >= 18]
#   return adults

# print(filterDogOwners_2(users))
# print(filterAdults_2(users))

# Trecias variantas:

def is_dog_owner(user):
  # if user['hasDog'] == True:
  #   return True
  # else:
  #   return False
  return user['hasDog']

def filterDogOwners_3(user_list):
  # dog_owners = filter(is_dog_owner, user_list)
  dog_owners = filter(lambda user: user['hasDog'], user_list)
  return list(dog_owners)

def is_adult(user):
  if user['age'] >= 18:
    return True
  else:
    return False

def filterAdults_3(user_list):
  # adults = filter(is_adult, user_list)
  adults = filter(lambda user: user['age'] >= 18, user_list)
  return list(adults)

print(filterDogOwners_3(users))
print(filterAdults_3(users))



