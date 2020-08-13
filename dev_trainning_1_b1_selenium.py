from selenium import webdriver
from getpass import getpass
username='admin'
pwd='123456aA'
driver=webdriver.Chrome('chromedriver.exe')

driver.get('http://45.79.43.178/source_carts/wordpress/wp-admin')

user_tBox=driver.find_element_by_id('user_login')
user_tBox.send_keys(username)
pwd_tBox=driver.find_element_by_id('user_pass')
pwd_tBox.send_keys(pwd)

login_btn=driver.find_element_by_id('wp-submit')
login_btn.submit()
driver.get('http://45.79.43.178/source_carts/wordpress/wp-admin/users.php')

users=driver.find_elements_by_xpath('//td[@class="username column-username has-row-actions column-primary"]//strong/a')
names=driver.find_elements_by_xpath('//td[@class="name column-name"]')
for i in range(len(users)):
    if(str(users[i].text)==username): 
        print(str(names[i].text))
        break
