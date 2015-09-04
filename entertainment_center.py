import media
import fresh_tomatoes


# Creating Movie Instances
star_wars= media.Movie(
                    "Star Wars",
                    "An Intergalactic battle between good and evil",
                    "http://bit.ly/1Jr1nhs",
                    "https://youtu.be/9gvqpFbRKtQ")

avatar = media.Movie(
                    "Avatar",
                    "A marine on an Alien Planet",
                    "http://bit.ly/1JofiD1",
                    "https://youtu.be/5PSNL1qE6VY")

matrix = media.Movie(
                    "The Matrix",
                    "A man discovers his world isn't what he thought",
                    "http://bit.ly/1Joflyu",
                    "https://youtu.be/vKQi3bBA1y8")

coming_to_america = media.Movie(
                    "Coming To America",
                    "An African prince searches for love in America",
                    "http://bit.ly/1Jr1Joo",
                    "https://youtu.be/fqfJqLFQSIk")

raiders_of_the_lost_arc = media.Movie(
                    "Raiders of the Lost Arc",
                    "A man on a geographical mission finds Adventure",
                    "http://bit.ly/1Jofj9R",
                    "https://youtu.be/gz4crpFaW4M")

three_Hundred = media.Movie(
                    "300",
                    "A small army of Spartans defend their home against insurmountable odds",
                    "http://bit.ly/1UbBYAK",
                    "https://youtu.be/2zqy21Z29ps")

#List of each instance
movies = [star_wars, avatar, matrix, coming_to_america,
          raiders_of_the_lost_arc, three_Hundred ]

#opens web page via fresh_tomatoes.py,using the list "movies" as the argument)
fresh_tomatoes.open_movies_page(movies)
