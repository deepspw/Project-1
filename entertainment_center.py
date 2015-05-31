import media
import fresh_tomatoes


# Movies
birdman = media.Movie(
	"Birdman",
	"A fading actor best known for his portrayal of a popular superhero "
	"attempts to mount a comeback by appearing in a Broadway play.",
	"http://upload.wikimedia.org/wikipedia/en/a/a3/Birdman_poster.jpg",
	"https://youtu.be/uJfLoE6hanc",
	"119"
	)

her = media.Movie(		
	"Her",
	"In the not so distant future, Theodore, a lonely writer purchases a "
	"newly developed operating system designed to meet the user's every needs. ",
	"http://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
	"https://youtu.be/ne6p6MfLBxc",
	"126"
	)

coherence = media.Movie(
	"Coherence",
	"On the night of an astronomical anomaly, eight friends at a dinner party"
	" experience a troubling chain of reality bending events. ",
	"http://upload.wikimedia.org/wikipedia/en/9/9d/Coherence_2013_theatrical_"
	"poster.jpg",
	"https://youtu.be/sEceDz1Rodc",
	"89"
	)

grandbudapest = media.Movie(
	"The Grand Budapest Hotel",
	"The Grand Budapest Hotel tells of a legendary concierge at a famous "
	"European hotel between the wars and his friendship with a young employee"
	" who becomes his trusted protege.",
	"http://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_"
	"Poster.jpg",
	"https://youtu.be/1Fg5iWmQjwk",
	"100"
	)

frank = media.Movie(
	"Frank",
	"A comedy about a young wannabe musician (Domhnall Gleeson) who discovers"
	" he has bitten off more than he can chew when he joins an eccentric pop"
	" band led by the mysterious and enigmatic Frank (Michael Fassbender).",
	"http://www.filmequals.com/wp-content/uploads/2014/06/frank-movie-poster.jpg",
	"https://youtu.be/1A7iVIg_ry8",
	"95"
	)

walle = media.Movie(
	"Wall-E",
	"WALL-E is the last robot left on an Earth that has been overrun with "
	"garbage and all humans have fled to outer space.",
	"http://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
	"https://youtu.be/alIq_wG9FNk",
	"98"
	)

# TV series
got = media.Tv(			
	"Game of Thrones",
	"The series is based on George R.R. Martin's novel about a fantasy world"
	" where royal houses battle for the Iron Throne.",
	"http://www.movieposter.com/posters/archive/main/117/MPW-58919.jpg",
	"https://youtu.be/iGp_N3Ir7Do"
	)

breakingbad = media.Tv(	
	"Breaking Bad",
	"A chemistry teacher decides to start a Meth lab.",
	"http://meetinthelobby.com/wp-content/uploads/2013/09/Breaking-Bad-Poster"
	"-Season-4-Large.jpg",
	"https://youtu.be/5NpEA2yaWVQ"
	)

twinpeaks = media.Tv(	
	"Twin Peaks",
	"Homecoming Queen Laura Palmer is found dead, washed up on a riverbank,"
	" wrapped in plastic sheeting.",
	"http://i.huffpost.com/gen/926049/thumbs/o-TWIN-PEAKS-REVIVAL-facebook.jpg",
	"https://youtu.be/UXjTEw9Qm0k"
	)

# Lists of both movies and tv
movies = [birdman,her,coherence,grandbudapest,frank,walle]
tv = [got,breakingbad,twinpeaks]

# Uses the open_movies_page module to construct html pages for both
fresh_tomatoes.open_movies_page(movies, "movie")
fresh_tomatoes.open_movies_page(tv, "tv")