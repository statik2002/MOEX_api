import requests


def get_securities(securities: str = '', language: str = 'ru', is_trading: bool = 0):
    url = f'https://iss.moex.com/iss/securities.json'

    params = {
        'q': securities,
        'lang': language,
        'is_trading': is_trading,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_security(security: str, language='ru'):
    url = f'https://iss.moex.com/iss/securities/{security}.json'

    params = {
        'lang': language,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_index(language: str = 'ru'):
    url = f'https://iss.moex.com/iss/index.json'

    params = {
        'lang': language,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_engines(language: str = 'ru'):
    url = f'https://iss.moex.com/iss/engines.json'

    params = {
        'lang': language,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_engine_description(engine: str, language: str = 'ru'):
    url = f'https://iss.moex.com/iss/engines/{engine}.json'

    params = {
        'lang': language,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_engine_markets(engine: str, language: str = 'ru'):
    url = f'https://iss.moex.com/iss/engines/{engine}/markets.json'

    params = {
        'lang': language,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_market_fields_description(engine: str, market: str, language: str = 'ru'):
    url = f'https://iss.moex.com/iss/engines/{engine}/markets/{market}/trades/columns.json'

    params = {
        'lang': language,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_trades_modes(engine: str, market: str, language: str = 'ru'):
    url = f'https://iss.moex.com/iss/engines/{engine}/markets/{market}.json'

    params = {
        'lang': language,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_all_securities(engine: str, market: str, securities: list = None, language: str = 'ru'):
    if securities is None:
        securities = []
    url = f'https://iss.moex.com/iss/engines/{engine}/markets/{market}/securities.json'

    params = {
        'lang': language,
        'securities': ','.join(securities)
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_spec_security(engine: str, market: str, securities: list, language: str = 'ru'):
    url = f'https://iss.moex.com/iss/engines/{engine}/markets/{market}/securities.json'

    params = {
        'lang': language,
        'securities': ','.join(securities)
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_security_candles(engine: str, market: str, security: str, till: str = '2037-12-31', start_from: str = '1995-01-01', interval: int = 24, reverse: bool = False):
    url = f'https://iss.moex.com/iss/engines/{engine}/markets/{market}/securities/{security}/candles.json'

    params = {
        'till': till,
        'from': start_from,
        'interval': interval,
        'reverse': reverse
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_ticket_history(ticker: str, from_date: str, till_date: str, interval: int):
    url = f'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{ticker}/candles.json'

    page = 0

    response_data = []

    params = {
        'from': from_date,
        'till': till_date,
        'start': page,
        'interval': interval,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    for line in response.json()['candles']['data']:
        response_data.append(line)

    page += 500

    while response:
        params = {
            'from': from_date,
            'till': till_date,
            'start': page,
            'interval': interval,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()

        if not response.json()['candles']['data']:
            break

        for line in response.json()['candles']['data']:
            response_data.append(line)
        page += 500

    return response_data


