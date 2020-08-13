import requests
import sys
from lxml import html

data={
    'log': 'admin', 
    'pwd': '123456aA',
    'wp_submit':'Log In',
    'redirect_to':'http://45.79.43.178/source_carts/wordpress/wp-admin/',
    'testcookie':'1'
    }
jar=requests.cookies.RequestsCookieJar()
jar.set('wordpress_test_cookie','WP+Cookie+check')
jar.set('tk_ai','woo%3Aif%2BZOxwi5PZuZCKOOqMrX0Ux')


with requests.Session() as s:
    s.cookies=jar
    url_login='http://45.79.43.178/source_carts/wordpress/wp-login.php'
    url_users='http://45.79.43.178/source_carts/wordpress/wp-admin/users.php'
    res_login=s.post(url_login,data=data)
    res_users=s.get(url_users)
    doc = html.fromstring(res_users.content)
    xpartUsername='//td[@class="username column-username has-row-actions column-primary"]//strong/a'
    xpartName='//td[@class="name column-name"]'
    rawUsername=doc.xpath(xpartUsername)
    rawName=doc.xpath(xpartName)
    for i in range(len(rawUsername)):
        if str(rawUsername[i].text) == data.get('log'):
            print(str(rawName[i].text))
            break