# 1. Expanded Database (Hollywood + Bollywood)
""" Project: Movie Recommendation System
Description: This is a simple content-based recommender that takes user interests as input 
and matches them with movies in our database. 
How it works:
1. It uses a dictionary to store Hollywood and Bollywood movies with their genres.
2. It calculates a 'match score' using Jaccard Similarity logic 
   (Intersection of interests / Union of genres).
3. It sorts the results so the best matches show up first with a star rating.
4. It's designed to be dynamic, so adding new movies to the 'movies_db' 
   automatically updates the available genres."""
movies_db = {
    # Hollywood
    "Interstellar": ["sci-fi", "drama", "space"],
    "The Dark Knight": ["action", "crime", "drama"],
    "Inception": ["action", "sci-fi", "thriller"],
    "The Avengers": ["action", "sci-fi"],
    "The Lion King": ["animation", "adventure", "drama"],
    "John Wick": ["action", "thriller"],
    
    # Bollywood & Others
    "Dhurandar": ["action", "thriller", "crime"], # Added as requested!
    "3 Idiots": ["comedy", "drama", "education"],
    "Dangal": ["biography", "sports", "drama"],
    "Zindagi Na Milegi Dobara": ["adventure", "comedy", "drama"],
    "Drishyam": ["thriller", "crime", "mystery"],
    "Lagaan": ["sports", "drama", "history"],
    "Gangs of Wasseypur": ["action", "crime", "drama"]
}

def recommend():
    # Collect all unique genres from the DB to show the user
    all_genres = set()
    for g_list in movies_db.values():
        all_genres.update(g_list)
    
    print("--- 🎬 Welcome to the AI Movie Matcher ---")
    print(f"Available Genres: {', '.join(sorted(list(all_genres)))}")
    
    # User Input Logic i.e what they are interested in..
    raw_input = input("\nEnter your interests (e.g. Action, Drama, Crime): ")
    
    # Logic: Clean the input
    user_interests = [i.strip().lower() for i in raw_input.split(",")]

    results = []
    for movie, genres in movies_db.items():
        # Jaccard Similarity Logic: (Intersection / Union)
        intersection = set(user_interests).intersection(set(genres))
        union = set(user_interests).union(set(genres))
        
        score = len(intersection) / len(union)
        results.append((movie, score))

    # Sort by highest match score
    results.sort(key=lambda x: x[1], reverse=True)

    print("\n--- 🍿 Your Personalized Recommendations ---")
    found = False
    for movie, score in results:
        if score > 0:
            match_percent = int(score * 100)
            star_rating = "⭐" * (match_percent // 20) # Simple visual UI logic
            print(f"{star_rating} {movie}: {match_percent}% Match")
            found = True
    
    if not found:
        print("❌ Sorry, no matches found. Try using genres like 'Action' or 'Drama'.")

# Run the program
if __name__ == "__main__":
    recommend()

"""Now, the question is: Where did I use AI in this?
The "AI" part here is the 'Content-Based Filtering' logic. Instead of just 
searching for an exact word, the code uses a similarity algorithm to rank 
results. By calculating the mathematical overlap between what the user 
wants and what the database has, the system "decides" which movies are 
most relevant—which is the fundamental building block of how real 
recommendation engines (like Netflix or YouTube) work."""
