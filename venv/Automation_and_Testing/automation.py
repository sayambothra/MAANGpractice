from selenium import webdriver

chrome_browser=webdriver.Chrome('./chromedriver.exe')

#seleniumeasy.com/test
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/')
#assert 'javascript' in chrome_browser.title
# button=chrome_browser.find_element_by_class_name('btn btn-dev btn-grey')
# button=chrome_browser.find_element_by_css_selector('.btn btn-dev btn-grey')
# print(button)

# close a browser
chrome_browser.close()

