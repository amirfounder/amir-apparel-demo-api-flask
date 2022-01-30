from src.data.entities import Product
from random import randint, random, choice


MATERIALS = ['Cotton', 'Polyesters', 'Silk', 'Leather']
TYPES = ['Gloves', 'Shorts', 'Pants', 'Shoes', 'Socks', 'Boxers']


def build_products(count: int):
    return [build_product() for _ in range(count)]


def build_product():
    product = Product()

    material = build_random_material()
    type = build_random_type()
    name = build_random_name(material, type)

    product.name = name
    product.type = type
    product.description = build_random_description(name)
    product.material = material
    product.price = build_random_price()
    product.available_quantity = build_random_quantity()
    product.status = build_random_status()

    return product


def build_random_name(material: str, type: str):
    return "{} {}".format(material, type)


def build_random_type():
    return choice(TYPES)


def build_random_description(name: str):
    return "These are some awesome {}! These guys are definitely a steal!".format(name)


def build_random_material():
    return choice(MATERIALS)


def build_random_price():
    min = 10
    max = 100
    random_double = random()

    return min + (random_double * (max - min))


def build_random_quantity():
    return randint(100, 500)


def build_random_status():
    return randint(0, 1) == 1
