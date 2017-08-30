COLOURS = {"AliceBlue": "#f0f8ff", "aquamarine1": "#7fffd4", "thistle2": "#cbd5cd", "turquoise1": "#00f5ff",
           "violet": "#ee82ee", "tomato2": "#ee5c42", "chartreuse1": "#7fff00", "tan": "#d2b48c", "tan4": "#8b5a2b",
           "SpringGreen1": "#00ff7f", "SpringGreen2": "#00ee76", "SpringGreen3": "#00cd66", "SpringGreen4": "#008bb45",
           "snow1": "#fffafa", "snow2": "#eee9e9"}

color = input("Input Colour: ")
print("Code: {}".format(COLOURS.get(color)))

