# 1. Expanded Database (Hollywood + Bollywood)
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
    
    # User Input Logic
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