# Отслеживание цены криптопары

## Системные требования
```commandline
python 3.7
```

## Принцип работы
Программа разработа с целью предупреждения пользователя об изменении цены криптопары на 1% и более.

Программа использует **API Binance** на основе [документации](https://binance-docs.github.io/apidocs/#signed-trade-and-user_data-endpoint-security)


1. выподтися сообщение о старте программы:
```
program start
```

2. программа запрашивает актульную цену с помощью специального [эндпоинта]('https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT'), доп параметр 'symbol' позволяет получить доступ к определенной криптопаре и получить ответ, который возвращаетс данные в json формате, цена достпна по ключу **price**. 

3. программа запрашивает время биржи с помощью специального [эндпоинта]('https://api.binance.com/api/v1/time')

4. программа высчитывает отнимает от акутального времени один час, и делает запрос на [эндпоинт]('https://api.binance.com/api/v1/klines?symbol=XRPUSDT&interval=1m&limit=1&startTime=') позволяющий получить данные определенной свечи.
Для реализации функционала была выбрана минутная свеча.
   
    **используемые параметры для эндпоинта:**
    ```
   symbol      #выбор криптопары (XRPUSDT)
   interval    #выбор интревала свечи (1m)
   limit       #количесво возвращаемых свечей
   startTime   #время открытия свечи
   ```
   
5. после получения необходимых данных, программа сравнивает значение цены при открытии свечи час назад и актулаьной цены. В случае снижения цены на 1% и более, программа возвращет сообщение

```
alert
```

## Запуск на локальной машине:
- закгрузить проект с GitHub на локальную машину
- отккрыть терминал bash
- перейти в директорию с проектом
- ввести команду:
```bash
python main.py
```
*в случае использования MacOS или Linux всесто python нужно вписать python3*


## Доработка проекта

### пункт является ответом на второй вопрос:

для обработки всех пар, а не только одной, целесообразно было бы использовать асинхронные запросы к эндпоинтам.
Таким образом программа будет "одновременно" следить за нужным количесвом пар, и возвращать сообщение об измении конретой цены криптопары