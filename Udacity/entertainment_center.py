import fresh_tomatoes
import media

star_wars = media.Movie("Star Wars", "A young boy from Tatooine sets out on an adventure with an old Jedi named Obi-Wan Kenobi as his mentor to save Princess Leia from the ruthless Darth Vader and Destroy the Death Star built by the Empire which has the power to destroy the entire galaxy.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQZKZtrlY3dnzsjBIGKR_b1QhkgZfM4-FIcH61uHnLQRR3WpNhk",
                        "https://www.youtube.com/watch?v=vP_1T4ilm8M")
#print(star_wars.storyline)
matrix = media.Movie("Matrix",
                     "This film depicts a dystopian future in which reality as perceived by most humans is actually a simulated reality called the Matrix, created by sentient machines to subdue the human population, while their bodies' heat and electrical activity are used as an energy source.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")
#print(matrix.storyline)
#avatar.show_trailer()
prometheus = media.Movie("Prometheus",
                     "One seriously freaky Riddly Scott movie",
                     "http://20ui41tp7v127j03rcnp97oh.wpengine.netdna-cdn.com/wp-content/uploads/2012/11/prometheusbg3.jpg",
                     "https://www.youtube.com/watch?v=nmJOO6D5RvA")
#print prometheus.show_trailer()
#prometheus.show_trailer()
bladerunner = media.Movie("Blade Runner",
                     "Man has made his match..., now it is his problem. Meet Nexus 6",
                     "http://t3.gstatic.com/images?q=tbn:ANd9GcTcvek3p12Gwqwk-2wjTSHWTNq0LTTeoOgXUwqerVOY2u9zjOgO",
                     "https://www.youtube.com/watch?v=3qZSIla_zPQ")
#print bladerunner.show_trailer()
#bladerunner.show_trailer()
terminator = media.Movie("Terminator",
                     "Arnold Schwarzenegger as the The Terminator / T-800 Model 101, a cybernetic android disguised as a human being sent back in time to assassinate Sarah Connor.",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcRHzSaUCOKu1RwS-bfbaUeeo_I1JcBkiuJRjBElvJi7qsHXkUkJ",
                     "https://www.youtube.com/watch?v=c4Jo8QoOTQ4")
#print terminator.show_trailer()
#terminator.show_trailer()
spaceodyssey = media.Movie("2001: a space odyssey",
                     "2001: a space odyssey is a story of evolution. The race is between man and machine",
                     "https://durnmoosemovies.files.wordpress.com/2014/03/2001-1.jpg",
                     "https://www.youtube.com/watch?v=gSoGSeuxdTs")
#print spaceodyssey.show_trailer()
#spaceodyssey.show_trailer()

movies = [star_wars, matrix, prometheus, bladerunner, terminator, spaceodyssey]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print media.Movie.__doc__
