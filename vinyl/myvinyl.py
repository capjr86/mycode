#!/usr/bin/python3

#message = "Welcome to my vinyl collection"

vinyl = {"rap": ["A Tribe Called Quest-Midnight Marauders",
        "Master P-Ghetto D","UGK-Ridin Dirty", "Nas-Stillmatic","Madlib-Shades of Blue"],
        "rock": ["Sublime-40oz to Freedom", "Fleetwood Mac-Rumours","Pink Floyd-Dark Side of the Moon" ],
        "r&b": ["Minnie Ripperton-Adventures in Paradise","Al Green-Greatest Hits", "Sade-Greatest Hits", 
        "Erykah Badu-Mamas Gun"]}

        genre = input("Please choose one of these genres. Rap, R&B, Rock: ").lower().strip()

if genre == "rap":
        print(vinyl["rap"])

elif genre == "rock":
    print(vinyl["rock"])
    
elif genre == "r&b": 
    print(vinyl["r&b"])

else:
    print("Please choose from the options given")
