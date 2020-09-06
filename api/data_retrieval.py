from json import loads, JSONDecodeError

from requests import ConnectTimeout
from requests import get

FOOD_BOXES_URL = 'https://stepik.org/media/attachments/course/73594/foodboxes.json'
RECIPIENTS_URL = 'https://stepik.org/media/attachments/course/73594/recipients.json'


def get_data(url):
    """ Получаем боксы с едой. """
    try:
        data = loads(get(url).content)
    except ConnectTimeout:
        raise ConnectTimeout()
    except JSONDecodeError:
        raise JSONDecodeError
    except TypeError:
        raise TypeError()

    return data


def get_recipients():
    """ Данные получателей. """
    return get_data(RECIPIENTS_URL)


def get_food_boxes(min_price=None, min_weight=None):
    """ Фуд боксы. """
    food_boxes = get_data(FOOD_BOXES_URL)
    if min_price:
        return filter_boxes('price', min_price, food_boxes)
    if min_weight:
        return filter_boxes('weight_grams', min_weight, food_boxes)
    return food_boxes


def filter_boxes(param, value, data):
    """ Фильтруем данные по параметру. """
    filtered_data = []
    if param == 'price':
        for box in data:
            if box['price'] >= value:
                filtered_data.append(box)
    if param == 'weight_grams':
        for box in data:
            if box['weight_grams'] >= value:
                filtered_data.append(box)
    return filtered_data
