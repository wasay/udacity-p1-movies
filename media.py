#import webbrowser class
import webbrowser

class Movie():
    #This init method will initialize the class Movie
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    #method show_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
