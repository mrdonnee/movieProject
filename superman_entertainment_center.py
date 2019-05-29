import movie
import website

superman = movie.Movie(movie_title = "Superman", movie_storyline = "Just before the destruction of the planet Krypton, scientist Jor-El sends his infant son Kal-El on a spaceship to Earth. Raised by kindly farmers Jonathan and Martha Kent, young Clark discovers the source of his superhuman powers and moves to Metropolis to fight evil. As Superman, he battles the villainous Lex Luthor, while, as novice reporter Clark Kent, he attempts to woo co-worker Lois Lane."
, poster_image = "https://upload.wikimedia.org/wikipedia/en/6/6d/Superman_ver1.jpg",
trailer_youtube = "https://www.youtube.com/watch?v=grO4OcJ6cgY")  

superman2 = movie.Movie("Superman 2", "Superman foils the plot of terrorists by hurtling their nuclear device into outer space, but the bomb's shock waves free the Kryptonian villain General Zod and his henchmen Ursa and Non from their imprisonment. Traveling to Earth, they threaten the planet with destruction at the same time that Superman decides to renounce his superpowers in order to live a normal life as Clark Kent with his new love, Lois Lane.",
"https://upload.wikimedia.org/wikipedia/en/3/36/Superman_II.jpg",
"https://www.youtube.com/watch?v=lXjIvtr65SI")

superman3 = movie.Movie("Superman 3", "Computer programmer Gus Gorman is hired by financial tycoon Ross Webster to seize control of a weather satellite and annihilate Colombia's coffee crop. When Superman manages to thwart the plan, Webster commands Gorman to use the satellite to locate kryptonite, the Man of Steel's mortal weakness. But a missing unknown element in the kryptonite -- replaced by Gorman with tar -- causes an unintended side effect when presented to Superman.",
"https://upload.wikimedia.org/wikipedia/en/9/9f/Superman_III_poster.jpg",
"https://www.youtube.com/watch?v=f-3fDHfrpHk")

superman4 = movie.Movie("Superman 4","Seeing the United States and the Soviet Union engaged in a nuclear arms race that could lead to Earth's destruction, Superman decides that he must take action. He collects all the nuclear warheads from the world and throws them into space. Meanwhile, Superman's nemesis, Lex Luthor, has broken out of prison with a new scheme. He clones Superman with radioactive material to create Nuclear Man, a being just as powerful as the man of steel.",
"https://upload.wikimedia.org/wikipedia/en/5/5c/Superman_iv.jpg",
"https://www.youtube.com/watch?v=LxR6EWkQj0A")


movies = [superman, superman2, superman3, superman4]
website.open_movies_page(movies)