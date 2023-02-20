import sqlite3
from foods import food_list
from food import Food


def main():
    try:
        conn = sqlite3.connect("foods.db")
        cursor = conn.cursor()
        # print("Connect success")
        _cntr = 0
        for food in list(food_list.keys()):
            food_image = list(food_list.keys()).index(food) + 1
            _food = Food(food, list(food_list.get(food))[0], str(food_image))
            # print(f"Add {_food.name}")
            query = f"INSERT INTO Foods (id, name, image_src, description) VALUES ({_cntr}, '{_food.name}', '{_food.image}.jpg', '{_food.description}');"
            cursor.execute(query)
            print(f"{query}")
            _cntr += 1

        cursor.close()
    except sqlite3.Error as er:
        print(er)
    finally:
        conn.close()
        # print("Connect die")


if __name__ == "__main__":
    main()
