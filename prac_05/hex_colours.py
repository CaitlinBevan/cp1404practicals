"""Hex colours program."""

HEX_COLOUR = {"AliceBlue": "#f0f8ff", "coral": '#ff7f50', "DarkOliveGreen1": "#caff70", "DarkOrchid": "#9932cc",
              "DeepPink1": "#ff1493", "DeepSkyBlue1": "#00bfff", "firebrick1": "#ff3030", "DarkOrange": "#ff8c00",
              "DarkViolet": "#9400d3", "FloralWhite": "#fffaf0"}

colour = input("Enter a colour: ")
while colour != "":
    if colour in HEX_COLOUR:
        print(colour, "is", HEX_COLOUR[colour])
    else:
        print("Invalid colour name.")
    colour = input("Enter a colour: ")
