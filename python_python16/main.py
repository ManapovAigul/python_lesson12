class Person:
    def __init__(self, name, surname, ago, id):
        self.__name = name
        self.__surname = surname
        self.__ago = ago
        self.__id = id
    def age(self):
        return self.__age

    def age(self, age):
        if age in range(1, 150):
            self.__age = age
        else:
            print('недопустимый возраст')

    def name(self):
        return self.__name

class Director(Person):

    def set_age(self, age):
        if age in range(1, 150):
            self.__age = age

        else:
            print('недопустимый возраст')

    def get_age(self):
        print(self.__age)


    def get_area(self):
        return self.name + self.surname

    if __name__ == '__main__':
        print()



    class Person:
        def __init__(self, name, surname, age, id):
            self.__name = name
            self.__surname = surname
            self.__age = age
            self.__id = id

        def age(self):
            return self.__age

        def age(self, age):
            if age in range(1, 100):
                self.__age = age
            else:
                print("Недопустимый возраст")

        @property
        def name(self):
            return self.__name

        def display_info(self):
            print("Имя: ", self.__name, "\nФамилия: ", self.__surname, "\nВозраст: ", self.__age, "\nID: ", self.__id)


class Director(Person):
    def about(self):
        print(self.name, "директор")


class Student(Person):
    def about(self):
        print(self.name, "студент")


class Teacher(Person):
    def about(self):
        print(self.name, "учитель")


def main():
    d = Director("1", "2", 3, 4)
    d.about()
    s = Student("1", "2", 3, 4)
    s.about()
    t = Teacher("1", "2", 3, 4)
    t.about()

if __name__ == "__main__":
    main()






