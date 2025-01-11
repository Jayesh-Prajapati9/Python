from imdb import IMDb

def search_movie(movie_name):
    # Create an IMDb object
    ia = IMDb()
    
    # Search for the movie
    search_results = ia.search_movie(movie_name)
    
    if search_results:
        # The first result is usually the best match
        movie = search_results[0]
        
        # Fetch detailed information about the movie using its ID
        ia.update(movie)
        
        # Print movie details
        print(f"Title: {movie.get('title')}")
        print(f"Year: {movie.get('year')}")
        print(f"Rating: {movie.get('rating')}")
        print(f"Votes: {movie.get('votes')}")
        print(f"Genres: {', '.join(movie.get('genres', []))}")
        print(f"Plot: {movie.get('plot', ['No plot available'])[0]}")
        
        # Get Directors
        directors = movie.get('directors', [])
        if directors:
            print(f"Directors: {', '.join([director['name'] for director in directors])}")
        else:
            print("Directors: Not available")
        
        # Get Cast
        cast = movie.get('cast', [])
        if cast:
            print(f"Cast: {', '.join([actor['name'] for actor in cast])}")
        else:
            print("Cast: Not available")
    else:
        print("Movie not found!")

# Example usage
movie_name = input("Enter the movie name: ")
search_movie(movie_name)
