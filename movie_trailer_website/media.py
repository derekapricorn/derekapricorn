import webbrowser
class Movie():
    def __init__(self, title, storyline, poster, youtube):
        """
        A movie

        Relevant information includes title, a blurb of \n
        the story, the URL pointing to its box poster, and \n
        the youtube link of its trailor

        """
        
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = youtube
        
    def play_trailer(self):
        """ Play the trailer on a browser """
        
        webbrowser.open(self.youtube_url)
        
        
    
