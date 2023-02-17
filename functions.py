import requests
HOUR = 3600000


def get_price_now(key_price):
    """
    функция принимает на вход эндпоинт
    binance api для получения актуальной цены
    цена доступна по ключу price
    возвращает цену (float)
    """
    data_now = requests.get(key_price)
    data_now = data_now.json()
    return float(data_now['price'])


def get_price_hour_ago(key_time, key_price):
    """
    функция принимает на вход эндпоинты
    key_time для получения времени binance
    key_price для получения цены открытия минутной свечи
    возвращает цену (float)
    """
    data_time = requests.get(key_time)
    data_time = data_time.json()
    time_now = data_time['serverTime']
    time_hour_ago = time_now - HOUR

    key_hour_ago_price = key_price + str(time_hour_ago)
    data_hour_ago = requests.get(key_hour_ago_price)
    data_hour_ago = data_hour_ago.json()
    return float(data_hour_ago[0][1])


def alarm_change_price(key_now_price, key_hour_ago_price, key_time):
    """
    функция принимает на вход 3 эндпоинта
    key_now_price для получаения актуальной цены
    key_hour_ago_price для получения цены час назад
    key_time для получения времени binance
    вычисяет отклонение цены, если цена упала на 1% и более
    распечатывает в консоль строку с предупреждением
    """
    if get_price_now(key_now_price) <= (get_price_hour_ago(key_time,
                                        key_hour_ago_price) * 0.99):
        print('alarm')
