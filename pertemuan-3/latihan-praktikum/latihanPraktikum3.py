class HouseGenre:
    def __init__(self, subgenre, artist, popular):
        self.subgenre = subgenre
        self.artist = artist
        self.popular = popular

    def text(self):
        print(self.artist + " is one of " + self.subgenre + " artist" )

    def is_house(self):
        print(self.subgenre + " is a House sub-genre")


x = HouseGenre("Progressive House", "Avicii", True)
y = HouseGenre("Big Room House", "W&W", True)
z = HouseGenre("Tropical House", "Kygo", True)
print(x.subgenre, x.artist, x.popular)
print(y.subgenre, y.artist, y.popular)
print(z.subgenre, z.artist, z.popular)

x.text()
y.is_house()

y.artist = "Hardwell"
y.text()
