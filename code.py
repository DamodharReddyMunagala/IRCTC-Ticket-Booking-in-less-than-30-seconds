# IRCTC-Ticket-Booking-in-less-than-30-seconds
from selenium import webdriver
import time
def irctcBooking():
    path_to_chromedriver = "C:/chromedriver.exe"
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)
    url = 'https://www.irctc.co.in/'
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="usernameId"]').clear()
    browser.find_element_by_xpath('//*[@id="usernameId"]').send_keys('damu1863')
    browser.find_element_by_xpath('//*[@id="loginFormId"]/div[1]/div[2]/table[1]/tbody/tr[2]/td[2]/input').clear()
    browser.find_element_by_xpath('//*[@id="loginFormId"]/div[1]/div[2]/table[1]/tbody/tr[2]/td[2]/input').send_keys('djd912')
    # Type the captcha text in these 6 seconds
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="loginbutton"]').click()
    browser.find_element_by_xpath('//*[@id="jpform:fromStation"]').send_keys('HYDERABAD DECAN - HYB')
    browser.find_element_by_xpath('//*[@id="jpform:toStation"]').send_keys('GWALIOR - GWL')
    browser.find_element_by_xpath('//*[@id="jpform:journeyDateInputDate"]').send_keys('24-07-2016')
    browser.find_element_by_xpath('//*[@id="jpform:jpsubmit"]').click()
    # If you want to change the select quota from tatkal to the other you can proceed with that
    browser.find_element_by_xpath('//*[@id="qcbd"]/table/tbody/tr/td[5]/input').click()
    # If you want to change the coach from sleeper to the other you can proceed with that
    browser.find_element_by_xpath('//*[@id="cllink-12723-SL-3"]').click()
    # Click on the Book Now Option in these 5 seconds
    time.sleep(10)
    # Type your name
    browser.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:0:psgnAge"]').send_keys('21')
    # Here I have selected Male if you want to change that You can proceed changing option[2] to option[3]
    browser.find_element_by_xpath('//*[@id="addPassengerForm:psdetail:0:psgnGender"]/option[2]').click()
    # Here I am considering the auto upgradation
    browser.find_element_by_xpath('//*[@id="addPassengerForm:autoUpgrade"]').click()
    ## Here I am also considering the book only if confirmed berths are allocated option
    #browser.find_element_by_xpath('//*[@id="addPassengerForm:onlyConfirmBerths"]').click()
    browser.find_element_by_xpath('//*[@id="addPassengerForm:mobileNo"]').send_keys('8332010182')
    # Scroll down to enter the captcha
    # Here I am making the code to wait to enter the captch if you want more time then you can change it
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="validate"]').click()
    # Next is payment you can now proceed with this
irctcBooking()
