# Набор скриптов для работы с данным от биржы MOEX

## Общее описание
Данные берутся по этой инструкции [схема](https://iss.moex.com/iss/reference/) 
## Установка

## Настройка

## Описание

Функции:

### `get_securities` - Список бумаг торгуемых на московской бирже.
`def get_securities(securities: str = '', language: str = 'ru', is_trading: bool = 0)`

---

### `get_security` - Получить спецификацию инструмента.
`get_security(security: str, language='ru'):`

---

### `get_ticket_history` - получение данных свечей по определенному тикеру
`get_ticket_history(ticker: str, from_date: str, till_date: str, interval: int)`

---

### `get_engines()` - Получить доступные торговые системы.
`def get_engines(language: str = 'ru')`

---

### `get_engine_description()` - Получить описание и режим работы торговой системы.
`get_engine_description(engine: str, language: str = 'ru')`
Получить торговые системы можно с помощью `get_engines()`

---

### `get_engine_markets()` - Получить список рынков торговой системы.
`get_engine_markets(engine: str, language: str = 'ru')`
Получить торговые системы можно с помощью `get_engines()`

---

### `get_market_fields_description()` - Получить описание полей для запроса сделок по рынку.
`get_market_fields_description(engine: str, market: str, language: str = 'ru')`
- Получить торговые системы {engine} можно с помощью `get_engines()`
- Получить рынки {market} можно с помощью `get_engine_markets()`

---

### `get_trades_modes()` - Получить описание: словарь доступных режимов торгов, описание полей публикуемых таблиц данных и т.д.
`get_trades_modes(engine: str, market: str, language: str = 'ru')`
- Получить торговые системы {engine} можно с помощью `get_engines()`
- Получить рынки {market} можно с помощью `get_engine_markets()`

---

### `get_all_securities()` - Получить таблицу инструментов торговой сессии по рынку в целом.
`get_all_securities('stock', 'shares', securities=['SBER', 'VTBR'])`
Если `securities` не указан или `None` то выводятся все инструменты.

---

### `get_spec_security()` - Получить данные по конкретному инструменту рынка.
`get_spec_security(engine: str, market: str, securities: list, language: str = 'ru')`
В `securities` необходимо указать список тикетов от 1 до 10

---

### `get_security_candles()` - Получить свечи указанного инструмента по дефолтной группе режимов.
`get_security_candles(engine: str, market: str, security: str, till: str = '2037-12-31', start_from: str = '1995-01-01', interval: int = 24, reverse: bool = False)`

