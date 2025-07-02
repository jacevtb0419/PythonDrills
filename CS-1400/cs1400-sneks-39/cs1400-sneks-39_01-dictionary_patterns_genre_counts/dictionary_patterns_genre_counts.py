books_genres = ["Horror", "Sci-Fi", "Horror", "Comedy",
                "Comedy", "Horror", "Horror", "Comedy"]
genre_counts = {}
for genre in books_genres:
    if genre in genre_counts:
        genre_counts[genre] = genre_counts[genre] + 1
    else:
        genre_counts[genre] = 1

print(genre_counts)
