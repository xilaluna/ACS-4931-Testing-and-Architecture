# by Kami Bigdely
# Extract class

class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def send_hiring_email(self):
        print("email sent to: ", self.email)


first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
          ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']


actors = []

for i in range(len(first_names)):
    actors.append(Actor(first_names[i], last_names[i],
                        birth_year[i], movies[i], emails[i]))


for actor in actors:
    if actor.birth_year > 1985:
        print(actor.first_name, actor.last_name)
        print('Movies Played: ', end='')
        for movie in actor.movies:
            print(movie, end=', ')
        print('***')
