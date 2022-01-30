from datetime import datetime
from src.data.entities import Product
from random import randint, random, choice


MATERIALS = ['Cotton', 'Polyesters', 'Silk', 'Leather']
TYPES = ['Gloves', 'Shorts', 'Pants', 'Shoes', 'Socks', 'Boxers']
DEMOGRAPHICS = ['Men', 'Women', 'Kids']
HEX_CODES = ['b0160b', '16f7d2', '870bb0', '0b81b0']


def build_products(count: int):
    return [build_product() for _ in range(count)]


def build_product():
    product = Product()

    material = build_random_material()
    type = build_random_type()
    name = build_name(material, type)
    hex_code = build_random_hex_code()

    product.name = name
    product.type = type
    product.demographic = build_random_demographic()
    product.description = build_description(name)
    product.material = material
    product.hex_code = hex_code
    product.color = build_color(hex_code)
    product.price = build_random_price()
    product.available_quantity = build_random_quantity()
    product.status = build_random_status()
    product.launch_date = build_random_launch_date()


    return product


def build_name(material: str, type: str):
    return '{} {}'.format(material, type)


def build_random_type():
    return choice(TYPES)


def build_description(name: str):
    return 'These are some awesome {}! These guys are definitely a steal!'.format(name)


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

def build_random_demographic():
    return choice(DEMOGRAPHICS)

def build_random_hex_code():
    return choice(HEX_CODES)

def build_color(hex_code: str):
    if hex_code == 'b0160b':
        return 'Dark Red'

    if hex_code == '16f7d2':
        return 'Purple'

    if hex_code == '870bb0':
        return 'Turquoise'

    if hex_code == '0b81b0':
        return 'Blue'

    return 'Unknown'

def build_random_launch_date():
    start = datetime(1995, 1, 1)
    end = datetime.now()

    return start + (end - start) * random()
