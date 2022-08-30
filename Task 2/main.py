from statistics import mean

# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

# 1:

# def get_user_average_age(x):
#   result = float(sum(d['age'] for d in x) / len(x))
#   return result

# average_age = get_user_average_age(users)
# print(average_age)


# 2:

# def get_users_names(y):
#   names_list = [item['name'] for item in y if 'name' in item]
#   return sorted(names_list)
  
# print(get_users_names(users))

# Tomo atsakymai

# def getUsersAverageAge(user_list):
#   age_total = 0
#   for user in user_list:
#     age_total += user['age']
#   age_average = age_total / len(user_list)
#   return age_average

# def getUsersNames(user_list):
#   names = []
#   for user in user_list:
#     names.append(user['name'])
#   return sorted(names)

# print(getUsersAverageAge(users))
# print(getUsersNames(users))

# Antras variantas

def getUsersAverageAge_2(user_list):
  ages = [user['age'] for user in user_list]
  age_average = sum(ages) / len(ages)
  return age_average

  
def getUsersNames_2(user_list):
  names = [user['name'] for user in user_list]
  return sorted(names)

# print(getUsersAverageAge_2(users))
# print(getUsersNames_2(users))

# Trecias variantas

def getUsersAverageAge_3(user_list):
  ages = list(map(lambda user: user['age'], user_list))
  return sum(ages) / len(ages)

def getUsersNames_3(user_list):
  names = map(lambda user: user['name'], user_list)
  names = map(lambda user: user.get('name', '<NENURODYTAS VARDAS>'), user_list)
  return sorted(names)

#print(getUsersAverageAge_3(users))
print(getUsersNames_3(users))

# Ketvirtas variantas

def getUsersAverageAge_4(user_list):
  return mean(list(map(lambda user: user['age'], user_list)))

#print(getUsersAverageAge_4(users))