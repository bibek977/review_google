from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options
import time

import mysql.connector

url = "https://www.google.com/maps/place/Nerd+Platoon+Pvt.+Ltd./@27.6714164,85.4068881,17z/data=!4m16!1m9!3m8!1s0x39eb1a9a5951d641:0x8e70548624a224e!2sNerd+Platoon+Pvt.+Ltd.!8m2!3d27.6714164!4d85.409463!9m1!1b1!16s%2Fg%2F11g6xs9njy!3m5!1s0x39eb1a9a5951d641:0x8e70548624a224e!8m2!3d27.6714164!4d85.409463!16s%2Fg%2F11g6xs9njy?hl=en-US&entry=ttu"


class Driver:

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(url)

    wait = WebDriverWait(driver, 30)

    def reviewRelevant():

        try:
            
            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@aria-label,"Reviews for")]')))
            button = Driver.driver.find_element(By.XPATH, '//button[contains(@aria-label,"Reviews for")]')
            button.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')))
            sort = Driver.driver.find_element(By.XPATH, '//span[contains(text(),"Sort")]//ancestor::button')
            sort.click()

            Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="menu"]/div[@data-index][1]')))
            relevant = Driver.driver.find_element(By.XPATH, '//div[@role="menu"]/div[@data-index][1]')
            relevant.click()


            element = Driver.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label and @role="main"]/div[2]')))

            height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)
            while True:
                Driver.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', element)
                time.sleep(5)

                new_height = Driver.driver.execute_script('return arguments[0].scrollHeight;', element)

                if height == new_height:
                    break
                height = new_height


            reviews = Driver.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@aria-label and @data-review-id]')))
            
            data = []
            for i in reviews:

                image = i.find_element(By.XPATH,'div/div/div/button/img').get_attribute('src')
                name = i.find_element(By.XPATH,'div/div/div[2]/div[2]/div/button/div[1]').text

                try:
                    desc = i.find_element(By.XPATH,'div/div/div[4]/div[2]/div/span[1]').text
                except NoSuchElementException:
                    desc = ""

                stars = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[1]').get_attribute('aria-label')
                date = i.find_element(By.XPATH,'div/div/div[4]/div[1]/span[2]').text

                profile_link =i.find_element(By.XPATH,'div/div/div/button').get_attribute('data-href')

                # print(image)
                # print(name)
                # print(desc)
                # print(stars)
                s = stars.split(" ")[0]
                star = int(s)
                # print(type(star))
                # print(date)
                # print(type(date))


                my_data = {
                    "image" : image,
                    "name" : name,
                    "desc" : desc,
                    "star" : star,
                    "date" : date,
                    "profile" : profile_link,
                    "company" : 1
                }
                data.append(my_data)
            print(data)

            return data

        except Exception as e:
            print(e)
            Driver.driver.quit()


data = Driver.reviewRelevant()

mydb =mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "root",
    database = "google"
)
print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO core_reviewer (name, star, description, date, imageLink, profileLink, comapany_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"

values = []
for i in data:
    val = (
        i["name"],
        i["star"],
        i["desc"],
        i['date'],
        i["image"],
        i["profile"],
        i["company"]
    )
    values.append(val)

mycursor.executemany(sql,values)

mydb.commit()

print(mycursor.rowcount, " record inserted")

Driver.driver.quit()