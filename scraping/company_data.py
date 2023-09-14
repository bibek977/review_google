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

    def getName():

        try:

            Driver.wait.until(EC.presence_of_element_located((By.XPATH,"//h1/span/parent::h1")))
            name = Driver.driver.find_element(By.XPATH,"//h1/span/parent::h1").text

            Driver.wait.until(EC.presence_of_element_located((By.XPATH,f'//button[contains(@aria-label,"Photo of {name}")]/img')))
            image = Driver.driver.find_element(By.XPATH,f'//button[contains(@aria-label,"Photo of {name}")]/img').get_attribute("src")

            return name,image

        except Exception as e:
            print(e)
        
    def getRating():

        try:
            Driver.wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(@aria-label,"stars") and @role="img"][1]/parent::span/span[1]')))
            # stars = Driver.driver.find_element(By.XPATH,'//span[contains(@aria-label,"stars") and @role="img"][1]/parent::span/span[1]').get_attribute('aria-label')
            stars = Driver.driver.find_element(By.XPATH,'//span[contains(@aria-label,"stars") and @role="img"][1]/parent::span/span[1]').text

            Driver.wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(@aria-label,"reviews")]')))
            total = Driver.driver.find_element(By.XPATH,'//span[contains(@aria-label,"reviews")]').get_attribute('aria-label')
            totals = total.split(" ")[0]
            return stars, totals
        
        except Exception as e:
            print(e)

    

star = Driver.getRating()[0]
print(star)
stars = float(star)
print(type(stars))
totals = Driver.getRating()[1]
totals = int(totals)


name = Driver.getName()[0]
image = Driver.getName()[1]
print(len(image))

post = "https://www.google.com/search?hl=en-NP&gl=np&q=Nerd+Platoon+Pvt.+Ltd.,+Bhaktapur+44800&ludocid=641487280368394830&lsig=AB86z5VPulQXKb38h8B1YYy85Bqr#lrd=0x39eb1a9a5951d641:0x8e70548624a224e,3"

show = "https://www.google.com/search?hl=en-NP&gl=np&q=Nerd+Platoon+Pvt.+Ltd.,+Bhaktapur+44800&ludocid=641487280368394830&lsig=AB86z5VPulQXKb38h8B1YYy85Bqr#lrd=0x39eb1a9a5951d641:0x8e70548624a224e,1"

link = "https://www.google.com/maps/place/Nerd+Platoon+Pvt.+Ltd./@27.6714164,85.409463,17z/data=!3m1!4b1!4m6!3m5!1s0x39eb1a9a5951d641:0x8e70548624a224e!8m2!3d27.6714164!4d85.409463!16s%2Fg%2F11g6xs9njy?entry=ttu"

mydb =mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "root",
    database = "google"
)
print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO core_company (title, rate, person, photo) VALUES (%s, %s, %s, %s)"

values = (name, stars, totals, image)

mycursor.execute(sql,values)

mydb.commit()

print(mycursor.rowcount, f"{name} record inserted")

Driver.driver.quit()