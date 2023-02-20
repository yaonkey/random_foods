import sqlite3 as sql
from random import choice
from foods import food_list


class Food:
    name: str
    description: str
    image: str

    def __init__(self, name: str, description: str, image: str):
        self.name = name
        self.description = description
        self.image = image

    def _get_info(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "image": self.image
        }

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> list:
        return self.description.split('\n')

    def get_image(self) -> str:
        return self.image + '.jpg'

    def get_image_path(self) -> str:
        return './static/' + self.get_image()

    def random(self) -> str:
        rnd_food = choice(list(food_list.keys()))
        food_image = list(food_list.keys()).index(rnd_food) + 1
        self.name = rnd_food
        self.description = list(food_list.get(rnd_food))[0]
        self.image = str(food_image)

        return "Сегодня готовим:"


def get_random_food() -> Food:
    food: Food
    conn = sql.connect("foods.db")
    cursor = conn.cursor()
    query = "SELECT name, image_src, description FROM Foods ORDER BY RANDOM() LIMIT 1;"
    cursor.execute(query)
    _food = cursor.fetchall()
    food = Food(_food[0][0], _food[0][1], _food[0][2])
    cursor.close()
    return food

def add_new_food():
    food: Food
