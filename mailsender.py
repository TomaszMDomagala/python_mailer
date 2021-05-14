from selenium import webdriver
import smtplib
import time
import sys

username = 'xxx'
password = 'xxx'
email = 'xxx'
credentials = 'xxx'

def open_site():
    driver = webdriver.Chrome()
    driver.get("https://edukacja.pwr.wroc.pl/")
    #opcja student
    student = driver.find_element_by_xpath('//*[@id="size"]/div[1]/a[2]')
    student.click()
    #logowanie
    login = driver.find_element_by_xpath('//*[@id="username"]')
    login.send_keys(username)
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(password)
    button = driver.find_element_by_xpath('//*[@id="id2"]')
    button.click()
    check_email(driver)

def check_email(driver):
    notifications = driver.find_element_by_xpath('//*[@id="paper-top"]/div/div[3]/div/ul/li/div/a/span').text
    if  int(notifications) > 0:
        print(notifications, "Notifications!")
        driver.find_element_by_xpath('//*[@id="paper-top"]/div/div[3]/div/ul/li/div/a/i').click()
        for i in range(0, int(notifications)):
            messages = driver.find_elements_by_xpath('//*[@id="listaWiadomosci"]/tbody/tr')
            messages[i].click()
            contents = driver.find_element_by_xpath('//*[@id="podgladWiadomosci"]')
            send_mail(contents.text)
            driver.find_element_by_xpath('//*[@id="goBack"]').click()
            time.sleep(10)
        driver.close()
    else:
        print('No new notifications')
        driver.close()

def send_mail(contents):
    #connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #login and message
    server.login(mail, credentials)
    subcjet = 'Jsos'
    body = contents

    msg = f"Subject: {subcjet}\n\n{body}"
    #sending mail
    server.sendmail(
        email,
        email,
        msg.encode('cp1250')
    )

    server.quit()

def main(minutes):
        open_site()
        time.sleep(minutes)

#3600
user_input = input("Input intervals: ")

try:
    while True:
        main(int(user_input)*60)
except KeyboardInterrupt:
    sys.exit(0)
