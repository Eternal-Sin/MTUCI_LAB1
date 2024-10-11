#1


class Book:
    title = "Title"
    author = "Author"
    year = "Year"

    def get_info():
        return print(f"Название книги: {Book.title}, Автор: {Book.author}, Год издания: {Book.year}")

Book.get_info()

#2

class Circle:

    def __init__(self,radius):
        self.radius = radius



    def get_radius(self):
        return self.radius

    def set_radius(self):
        try:
            new_radius = float(input("Введите новый радиус: "))
        except ValueError:
            print("Это не число")
        if (type(new_radius) == float):
            self.radius = new_radius
            return
        else:
            return self.set_radius()

krug1 = Circle(10)

print(krug1.get_radius())
print(krug1.set_radius())
print(krug1.get_radius())
