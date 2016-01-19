import time
import requests
import csv
while 42 is 42:
    cur_timestamp = int(time.time())

    r = requests.get('https://www.bitstamp.net/api/transactions/?time=hour')
    data = r.json()

    ten_min_data = []
    for item in data:
        if int(cur_timestamp-600) <= int(item['date']):
            ten_min_data.append(item)


    def transactions_total(x):
        return len(x)


    def avg_amount(x):
        amount_sum = 0.0
        for i in x:
            amount_sum += float(i['amount'])
        return round((float(amount_sum) / float(len(x))), 5)


    def rate(x):
        return str(round((float(len(x))/10.0), 5))+' transactions per minute'


    def avg_price(x):
        price_sum = 0.0
        for i in x:
            price_sum += float(i['price'])
        return round((float(price_sum) / float(len(x))), 2)


    def datetime_start(x):
        start_time = x[-1]['date']
        return time.strftime("%b %d %Y %H:%M:%S", time.localtime(int(start_time)))


    def datetime_end(x):
        end_time = x[0]['date']
        return time.strftime("%b %d %Y %H:%M:%S", time.localtime(int(end_time)))


    result = {
                "#1 datetime_start": datetime_start(ten_min_data),
                "#2 datetime_end": datetime_end(ten_min_data),
                "#3 transactions_total": transactions_total(ten_min_data),
                "#4 avg_amount": avg_amount(ten_min_data),
                "#5 rate": rate(ten_min_data),
                "#6 avg_price": avg_price(ten_min_data)
                }

    c = csv.writer(open("/home/scandie/scripts/bit_stat.csv", "a"))
    c.writerow([result])
    time.sleep(600)
