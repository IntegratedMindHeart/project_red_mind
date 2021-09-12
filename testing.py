import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r'C:\Users\Tranzita Systems\Downloads\chromedriver_win32\chromedriver.exe')
time.sleep(2)
driver.maximize_window()
# driver.get('http://projectredmind.herokuapp.com')
driver.get('http://127.0.0.1:8000')

def page_down():
    body = driver.find_element_by_css_selector('body')
    body.click()
    body.send_keys(Keys.PAGE_DOWN)

def page_up():
    body = driver.find_element_by_css_selector('body')
    body.click()
    body.send_keys(Keys.PAGE_UP)

# Home Page

time.sleep(2)
page_down()
time.sleep(2)
page_up()
time.sleep(2)
movie_name_input=driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div/input')
movie_name_input.send_keys('Aliens')
time.sleep(2)
search_btn=driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div/button')
search_btn.click()
time.sleep(2)

# # Search Result 

driver.execute_script("window.scrollBy(0,300)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,640)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,190)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,765)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,770)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,800)")
time.sleep(5)
detailed_view_btn=driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/div[11]/div/div[2]/a/small')
detailed_view_btn.click()
time.sleep(2)

# Cast Page

driver.execute_script("window.scrollBy(0,80)")
time.sleep(5)
driver.back()
time.sleep(2)

# Bcak to Home Page

driver.execute_script("window.scrollBy(0,700)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,500)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,650)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,150)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,750)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,750)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,750)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,880)")
time.sleep(5)
detailed_view_btn=driver.find_element_by_xpath('/html/body/div[1]/div/div[9]/div[15]/div/div[2]/form/input[3]')
detailed_view_btn.click()
time.sleep(2)

# Search Result

driver.execute_script("window.scrollBy(0,300)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,640)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,190)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,765)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,770)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,800)")
time.sleep(2)
detailed_view_btn=driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/div[10]/div/div[2]/a/small')
detailed_view_btn.click()
time.sleep(2)

# Cast Page

driver.execute_script("window.scrollBy(0,80)")
time.sleep(2)
driver.back()
time.sleep(2)

# Bcak to Home Page

driver.execute_script("window.scrollBy(0,700)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,350)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,650)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,150)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,750)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,750)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,750)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,900)")
time.sleep(2)
driver.execute_script("scroll(0, 0)")
time.sleep(5)

movie_name_input=driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div/input')
movie_name_input.send_keys('cjkbjscbhjdv')
time.sleep(2)
search_btn=driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div/button')
search_btn.click()
time.sleep(5)

api_link=driver.find_element_by_xpath('/html/body/nav/div/div/ul/li[2]/a')
api_link.click()
time.sleep(5)

# API Page

recommendation_api_link=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/a')
recommendation_api_link.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
driver.execute_script("window.scrollBy(0,500)")
time.sleep(5)
review_api_link=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/a')
review_api_link.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.execute_script("scroll(0, 0)")
time.sleep(5)

api_link=driver.find_element_by_xpath('/html/body/nav/div/div/ul/li[3]/a')
api_link.click()
time.sleep(5)

# Admin Panel Login Page

driver.switch_to.window(driver.window_handles[1])
username_input=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/form/div[1]/input')
username_input.send_keys('root')
time.sleep(2)
password_input=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/form/div[2]/input[1]')
password_input.send_keys('root')
time.sleep(2)
login_btn=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/form/div[3]/input')
login_btn.click()
time.sleep(5)

# Admin Show Tables Panel Page

movies_records_link=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr/th/a')
movies_records_link.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
about_link=driver.find_element_by_xpath('/html/body/nav/div/div/ul/li[4]/a')
about_link.click()
time.sleep(3)

# About Page

driver.execute_script("window.scrollBy(0,105)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,710)")
time.sleep(5)

# Youtube Page

youtube_link=driver.find_element_by_css_selector('body > footer > div > div > a:nth-child(1) > svg')
youtube_link.click()
time.sleep(10)
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
github_link=driver.find_element_by_css_selector('body > footer > div > div > a:nth-child(2) > svg')
github_link.click()
time.sleep(10)

# quit

driver.quit()