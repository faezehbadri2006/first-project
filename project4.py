class Book:
    def init(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Onvan: {self.title}")
        print(f"Nevisandeh: {self.author}")
        print(f"Gheymat: {self.price} Toman")

    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount

# Sakht do shey az class Book
book1 = Book("Shazdeh Koochooloo", "Antoine de Saint-Exupéry", 120000)
book2 = Book("Symphony-ye Mardegan", "Abbas Maroufi", 150000)

# Namayesh etela'at-e ketab-e aval
print("Etela'at-e ketab-e aval:")
book1.display_details()

# E'mal takhfif rooye ketab-e dovom
book2.apply_discount(20)

# Namayesh etela'at-e har do ketab ba'd az taghirat
print("\nEtela'at-e ketab-e aval (bedoon taghir):")
book1.display_details()

print("\nEtela'at-e ketab-e dovom (ba'd az takhfif):")
book2.display_details()