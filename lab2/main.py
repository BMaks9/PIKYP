import requests 
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 2, 2)
    c = Circle("зеленого", 2)
    s = Square("красного", 2)
    print(r)
    print(c)
    print(s)
    print(requests.get("https://ya.ru/"))

if __name__ == "__main__":
    main()