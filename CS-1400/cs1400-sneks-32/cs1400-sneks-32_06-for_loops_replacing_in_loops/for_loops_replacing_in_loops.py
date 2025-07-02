filenames = ["All-the-Single-Ladies.mp3",
             "Call-Me-Maybe.mp3",
             "Chicken-Dance.mp3"]
for songs in filenames:
    new_song = songs.replace("-", " ")
    print(new_song)