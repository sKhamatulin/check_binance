from functions import alarm_change_price

key_now_price = ('https://api.binance.com/api/v3/ticker/price?'
                 'symbol=XRPUSDT')
key_time = 'https://api.binance.com/api/v1/time'
key_hour_ago_price = ('https://api.binance.com/api/v1/klines?'
                      'symbol=XRPUSDT'
                      '&interval=1m'
                      '&limit=1'
                      '&startTime=')

if __name__ == '__main__':
    print('program start')
    while True:
        try:
            alarm_change_price(key_now_price, key_hour_ago_price, key_time)
        except Exception as e:
            print(f'error {e}')
