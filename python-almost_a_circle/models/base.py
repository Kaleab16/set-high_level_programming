#!/usr/bin/python3
"""Base module.

Defines the Base class, which manages id attributes
for all future classes in this project.
"""
import json


class Base:
    """Base class that manages id and JSON (de)serialization."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dicts):
        """Return the JSON string representation of a list of dicts."""
        if list_dicts is None or len(list_dicts) == 0:
            return "[]"
        return json.dumps(list_dicts)

    @staticmethod
    def from_json_string(json_string):
        """Return a list represented by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file."""
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance built from a dictionary of attributes."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <ClassName>.json."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of a list of objects to a file."""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="", encoding="utf-8") as f:
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            if list_objs is None:
                list_objs = []
            for obj in list_objs:
                d = obj.to_dictionary()
                row = ",".join(str(d[field]) for field in fields)
                f.write(row + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from <ClassName>.csv."""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="", encoding="utf-8") as f:
                lines = f.read().splitlines()
        except FileNotFoundError:
            return []

        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]

        instances = []
        for line in lines:
            if not line:
                continue
            values = [int(v) for v in line.split(",")]
            d = dict(zip(fields, values))
            instances.append(cls.create(**d))
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all given Rectangles and Squares."""
        import turtle
        import time
        import random

        turtle.Screen().bgcolor("#b7312c")
        turt = turtle.Turtle()
        turt.shape('turtle')
        turt.color("white")
        turt.pensize(3)

        for rect in list_rectangles:
            print(rect)
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            time.sleep(1)
            turt.hideturtle()

        for square in list_squares:
            print(square)
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()

            def r():
                return random.randint(0, 255)

            turt.color('#%02X%02X%02X' % (r(), r(), r()))
            for i in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            time.sleep(1)
            turt.hideturtle()

        turtle.exitonclick()
