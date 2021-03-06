from decimal import Decimal
from pony.orm import *

db = Database()
# set_sql_debug(True)
db.bind(provider='sqlite', filename='ambrosia.sqlite', create_db=True)


class Product(db.Entity):
    name = Required(str, unique=True)
    calories = Required(Decimal, default=0)
    proteins = Required(Decimal, default=0)
    fats = Required(Decimal, default=0)
    carbohydrates = Required(Decimal, default=0)
    weightOfPack = Required(Decimal, default=0)
    weightOfPiece = Required(Decimal, default=0)
    dish = Set("ProductInDish")


class Dish(db.Entity):
    name = Required(str)
    products = Set("ProductInDish")


class ProductInDish(db.Entity):
    dishName = Required(Dish)
    productName = Required(Product)
    weight = Required(Decimal, default=0)
    piece = Required(Decimal)
    PrimaryKey(dishName, productName)


db.generate_mapping(create_tables=True)


@db_session
def print_products():
    print(select(p for p in Product).show())


@db_session
def add_product(name, **kwargs):
    p = Product.get(name=name)
    if p is None:
        Product(name=name, **kwargs)
    else:
        p.set(**kwargs)


@db_session
def remove_product(name):
    p = Product.get(name=name)
    if p is not None:
        p.delete()


@db_session
def print_dishes():
    print(select(p for p in Dish).show())


@db_session
def add_dish(name, **kwargs):
    d = Dish.get(name=name)
    if d is None:
        Dish(name=name, **kwargs)
    else:
        d.set(**kwargs)


@db_session
def remove_dish(name):
    d = Dish.get(name=name)
    if d is not None:
        d.delete()    # вместе с блюдом удаляются данные в таблице ProductInDish


@db_session
def add_product_to_dish(dish_name, product_name, weight, **kwargs):
    d = Dish.get(name=dish_name)
    p = Product.get(name=product_name)
    if d is not None and p is not None:
        # Надо добавить проверку на соответствие
        ProductInDish(dishName=dish_name, productName=product_name, weight=weight, **kwargs)


@db_session
def print_product_in_dish(name):
    dish = Dish.get(name=name)
    if dish is not None:
        print("Состав блюда: " + name)
        for p in dish.products:
            print(p.productName.name, p.weight)


@db_session
def print_dishes_composition():
    print("Состав блюд:")
    for p in select(p for p in Dish):
        print_product_in_dish(p.name)


@db_session
def print_product_in_dishes():
    print(select(p for p in ProductInDish).show())


@db_session
def test_queries():
    print("0")
    foo = Product[1].to_dict()
    print(foo)
    print("1")
    foo = [p.to_dict() for p in Product.select()]
    print(foo)


if __name__ == "__main__":
    add_product("соль")
    add_product("сахар", calories=1.02, proteins=1.1, fats=2, carbohydrates=3, weightOfPack=4, weightOfPiece=5)

    print("\nтаблица продуктов:")
    print_products()

    print("\nтаблица блюд:")
    print_dishes()

    print("\nтаблица состава:")
    print_product_in_dishes()

    test_queries()




