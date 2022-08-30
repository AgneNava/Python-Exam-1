# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie:
  def __init__(self, title, director, budget):
    self.title = title
    self.director = director
    self.budget = budget

  def __repr__(self):
    return f'(Pavadinimas: {self.title}, rezisierius: {self.director}, biudzetas: {self.budget} Eur)'  

  def was_expensive(self):
    # if self.budget > 100000000:
    #   return True
    # else:
    #   return False
    return self.budget > 100000000

movie1 = Movie('Verge Izaura', 'Oskaras Korsunovas', 2000)
movie2 = Movie('Zmogus Voras', 'Spielbergas', 100000001)

print(movie1, movie2)
print(movie1.was_expensive())
print(movie2.was_expensive())
