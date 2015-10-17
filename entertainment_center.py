######################################
# fresh_tomatoes and media file import
######################################
import fresh_tomatoes
import media

######################################
# set details regarding toy story movie
######################################
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "Tom Hanks,Tim Allen,Don Rickles,Jim Varney,"
                        "Wallace Shawn,John Ratzenberger,Annie Potts,"
                        "John Morris,Erik von Detten,Laurie Metcalf,"
                        "R. Lee Ermey,Sarah Freeman,Penn Jillette",
                        "November 19, 1995")

######################################
# set details regarding school of rock
######################################
school_of_rock = media.Movie("School of Rock",
                             "A guitarist plan to compete in a Battle of "
                             "the Bands tournament",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/"
                             "School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74",
                             "Jack Black,Joan Cusack,Mike White,"
                             "Sarah Silverman,Miranda Cosgrove,"
                             "Joey Gaydos Jr.",
                             "October 3, 2003")

######################################
# set details regarding ratatouille movie
######################################
ratatouille = media.Movie("Ratatouille",
                          "A ambitious young rat gifted with highly developed "
                          "sense of taste and smell with a dream to become a "
                          "cook",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/"
                          "RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          "Patton Oswalt,Ian Holm,Lou Romano,Brian Dennehy,"
                          "Peter Sohn,Peter O'Toole,Brad Garrett,"
                          "Janeane Garofalo",
                          "June 22, 2007")

######################################
# set details regarding hunger games movie
######################################
hunger_games = media.Movie("Hunger Games",
                           "A dystopian nation with glamorous Capitol "
                           "and twelve poorer disticts",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/"
                           "HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo",
                           "Jennifer Lawrence,Josh Hutcherson,Liam Hemsworth,"
                           "Woody Harrelson,Elizabeth Banks,Lenny Kravitz,"
                           "Stanley Tucci,Donald Sutherland",
                           "March 12, 2012")

######################################
# set details regarding avatar movie
######################################
avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io",
                     "Sam Worthington,Zoe Saldana,Stephen Lang,"
                     "Michelle Rodriguez,Sigourney Weaver",
                     "December 18, 2009")

######################################
# set details regarding midnight in paris movie
######################################
midnight_in_paris = media.Movie("Midnight in Paris",
                                "A screenwriter's desier for past era finds a "
                                "transport past midnight",
                                "http://upload.wikimedia.org/wikipedia/en/9/"
                                "9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU",
                                "Kathy Bates,Adrien Brody,Carla Bruni,"
                                "Marion Cotillard,Rachel McAdams,"
                                "Michael Sheen,Owen Wilson",
                                "May 20, 2011")

######################################
# Add the individual movies to the array called movies
# Movies will be displayed in the web page in the order being
# set up in this array
######################################
movies = [toy_story, school_of_rock, ratatouille, hunger_games,
          avatar, midnight_in_paris]

######################################
# calling fresh_tomatoes file's open_movies_page defination with
# variable movies as input
######################################
fresh_tomatoes.open_movies_page(movies)
