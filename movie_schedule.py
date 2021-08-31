current_movies = {"Die Hard": "11:00am",
                  "Die Hard 2: Die Harder": "1:00pm",
                  "Die Hard with a Vengeance": "3:00pm",
                  "Live Free or Die Hard": "5:00pm",
                  "A Good Day to Die Hard": "7:00pm"}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested showtime isn't playing.")
else:
    print(movie, "is playing at", showtime)