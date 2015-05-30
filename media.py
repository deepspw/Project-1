import webbrowser

class Media:
	def __init__(self, title, storyline, poster_image_url, trailer_youtube):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class Movie(Media):
	def __init__(self, title, storyline, poster_image_url, trailer_youtube, runtime):
		Media.__init__(self, title, storyline, poster_image_url, trailer_youtube)
		self.runtime = runtime

class Tv(Media):
	def __init__(self, title, storyline, poster_image_url, trailer_youtube):
		Media.__init__(self, title, storyline, poster_image_url, trailer_youtube)