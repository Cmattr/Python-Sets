artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set(artist_names)

for i in artist_names:
    if len(artist_names) == len(unique_artists):
        print("Duplicate playlists found: False")
else:
    print("Duplicate playlists found: True")


print(f"here is an updated schedule with no duplicate playlist: {unique_artists}")