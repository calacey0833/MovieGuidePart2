#Athena Caldwell
#CIS 261
#Movie Guide Part 2

file = 'Movies.txt'

def write_movies(movies):
    with open(filename, 'w') as file:
        for movie in movies:
            file.write(f'{movie}\n')
            
def read_movies():
    movies = []
    with open(filename) as file:
        for line in file:
            line = line.replace('\n', '')
            movies.append(line)
        return movies
    
def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f'{i}. {movie}')
        print()
        
def add_movie(movies):
    movie = input('Movie: ')
    movies.append(movie)
    write_movies(movies)
    print(f'{movie} was added.')
    
def delete_movie(movies):
    index = int(input('Number:'))
    if index < 1 or index > len(movies):
        print('Invalid movie number.')
    else:
        movie = movies.pop(index - 1)
        print