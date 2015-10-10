#import fresh_tomatoes and media file
import fresh_tomatoes
import media

#set details regarding toy story movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#set details regarding school of rock
school_of_rock = media.Movie("School of Rock", "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

#set details regarding ratatouille movie
ratatouille = media.Movie("Ratatouille", "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

#set details regarding hunger games movie
hunger_games = media.Movie("Hunger Games", "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=PbA63a7H0bo")

#set details regarding avatar movie
avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

#set details regarding midnight in paris movie
midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                          "https://www.youtube.com/watch?v=atLg2wQQxvU")

#Add the individual movies to the array called movies
#Movies will be displayed in the web page in the order being set up in this array
movies = [toy_story, school_of_rock, ratatouille, hunger_games, avatar, midnight_in_paris]

#calling fresh_tomatoes file's open_movies_page defination with variable movies as input
fresh_tomatoes.open_movies_page(movies)
