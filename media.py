import webbrowser

# Classes
class Media:
	"""
	Parent class to the children Movie and Tv. Takes variables and from a list and assigns
	them attributes.
	"""

	def __init__(self, title, storyline, poster_image_url, trailer_youtube):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


class Movie(Media):
	"""
	Child to Media class. Takes variables from a list and assigns attributes to them.
	"""

	def __init__(self, title, storyline, poster_image_url, trailer_youtube, runtime):
		Media.__init__(self, title, storyline, poster_image_url, trailer_youtube)
		self.runtime = runtime


class Tv(Media):
	"""
	Child to Media class. Takes variables from a list and assigns attributes to them.
	"""

	def __init__(self, title, storyline, poster_image_url, trailer_youtube):
		Media.__init__(self, title, storyline, poster_image_url, trailer_youtube)