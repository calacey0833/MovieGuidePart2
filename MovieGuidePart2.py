#Athena Caldwell
#CIS 261
#Movie Guide Part 2

FILENAME = 'Movies.txt'

def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(f"{movie}\n")
            
def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
        return movies
    
def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()
        
def add_movie(movies):
    movie = input("Movie:")
    movies.append(movie)
    write_movies(movies)
    print(f"{movie} was added.\n")
    
def delete_movie(movies):
    index = int(input("Number:"))
    if index < 1 or index > len(movies):
        print("Invalid movie number.\n")
    else:
        movie = movies.pop(index - 1)
        write_movies(movies)
        print("f{movie} was deleted.")
        
def main():
    movie_list = ["Cat on a Tin Roof", "On the Waterfront", "Monty Python and the Holy Grail to the file"]

def display_menu():
    print("The Movie List program\n")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program\n")
    print()
    
if __name__ == "__main__":
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command:")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")