import media
import fresh_tomatoes

#Add a couple of movies 
thor = media.Movie('Thor',
                   'Thor and his company',
                   'http://t3.gstatic.com/images?q=tbn:ANd9GcST1uigGrukMvSAVUefFNuQ0NMZAR-FjfFIwSZFCR5ZkyMSgCyj',
                   'https://www.youtube.com/watch?v=ue80QwXMRHg') # NOQA 
wonder = media.Movie('Wonder',
                     'Wonder how?',
                     'https://upload.wikimedia.org/wikipedia/en/0/03/Wonder_Cover_Art.png',
                     'https://www.youtube.com/watch?v=ZDPEKXx_lAI') # NOQA
geostorm = media.Movie('Geostorm',
                       'Natual disaster',
                       'http://cdn.hoyts.com.au/mediafiles/images/AUposters/HO00004000.jpg',
                       'https://www.youtube.com/watch?v=EuOlYPSEzSc') # NOQA
LBJ = media.Movie('LBJ',
                  'politics',
                  'http://t0.gstatic.com/images?q=tbn:ANd9GcTm6EpOegHtfvu-9u03BR6WgY_iUnzgKDnzdEWst1cIdfKwP3i1',
                  'https://www.youtube.com/watch?v=xrnEp8WLH0g') # NOQA

#combine the movies into a movie list
movies = [thor, wonder, geostorm, LBJ]

#construct a static web page for the movies
fresh_tomatoes.open_movies_page(movies)

