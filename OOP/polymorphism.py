class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Indian is the language of India.")

class USA():
    def capital(self):
        print("Washington is the capital of USA.")

    def language(self):
        print("English is the language of USA.")

country1 = India()
country2 = USA()

def info(*country) -> None:
    for i in country:
        i.language()


info(country1, country2)


