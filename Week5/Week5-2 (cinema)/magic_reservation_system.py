import sqlite3

cinema_hall = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "x", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]


def printHall():
    print("  1 2 3 4 5 6 7 8 9 10")
    for i, element in enumerate(cinema_hall):
        print (i + 1, ' '.join(element))


def show_movies():
    cinema = sqlite3.connect("cinema.db")
    cinema.row_factory = sqlite3.Row
    cursor = cinema.cursor()
    result = cursor.execute(
        '''SELECT id, name FROM movies ORDER BY rating desc''')
    for movie in result:
        print(movie['id'], " - ", movie['name'])
    cinema.commit()

# ne sym go napravil da priema opcionalna data


def show_movie_projections(MovieID):
    cinema = sqlite3.connect("cinema.db")
    cinema.row_factory = sqlite3.Row
    cursor = cinema.cursor()
    result = cursor.execute(
        '''SELECT movies.name, projections.date, projections.time FROM movies INNER JOIN projections ON movies.id = projections.movie_id WHERE movies.id = ?''', (MovieID,))
    for movie in result:
        print(movie['name'], movie['date'], movie['time'])
    cinema.commit()


def make_reservation():
    cinema = sqlite3.connect("cinema.db")
    cinema.row_factory = sqlite3.Row
    cursor = cinema.cursor()
    inputs = input("<hacker_name>, <number_of_tickets>")
    hacker_name = inputs[0]
    number_of_tickets = inputs[1]
    print("Choose the ID of the movie you want to watch and remeber it!")
    show_movies()
    print("Now enter the ID to see the available movie projections!")
    MovieID = input("<MovieID>")
    show_movie_projections(MovieID)
    print("Now you will see the available seats in the Hall!")
    printHall()
    for i in range(0, int(number_of_tickets)):
        print("Choose a seat now!")
        chosen_seat = input("<row>, <column>")
        row = chosen_seat[0]
        col = chosen_seat[1]
        if cinema_hall[row][col] != "x":
            cinema_hall[row][col] = "x"
            cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                      VALUES(?,?,?,?)''', (hacker_name, show_movie_projections(), row, col))
        else:
            print("Seat already taken!")

make_reservation()
