from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("1.Sign in at gihub.\n2.Sing in at instagram.\n13.Sign in at Facebook")
choice=int(input("Enter your choice: "))

while(1):
    service=Service(executable_path="chromedriver.exe")
    match choice:
        case 1:
            print("Signing in at gihub")
            username=input("Enter your username: ")
            password=input("enter your password: ")
            
            
            driver=webdriver.Chrome(service=service)
            
            driver.get("https://github.com/login")

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID,"login_field"))
            )
            login_id_field=driver.find_element(By.ID,"login_field")
            login_id_field.send_keys(username)
            

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID,"password"))
            )

            password_field=driver.find_element(By.ID,"password")
            password_field.send_keys(password)

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME,"commit"))
            )
            sign_in=driver.find_element(By.NAME,"commit")
            sign_in.click()
            time.sleep(10)
            break

        case 2:
            print("sigining in at instagram: ")
            username=input("Enter your username: ")
            password=input("enter your password: ")
            
            
            driver=webdriver.Chrome(service=service)
            
            driver.get("https://www.instagram.com/")

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input"))
            )
            login_id_field=driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
            login_id_field.send_keys(username)
            

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input"))
            )

            password_field=driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
            password_field.send_keys(password)

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id='loginForm']/div/div[3]/button"))
            )
            sign_in=driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button")
            sign_in.click()
            time.sleep(5)
            break

        case 3:
            print("signing in at facebook: ")
            username=input("enter your facebook username: ")
            password=input("enter your facebook password: ")
            driver=webdriver.Chrome(service=service)

            driver.get("https://www.facebook.com/")
            
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID,"email"))
            )
            login_field=driver.find_element(By.ID,"email")
            login_field.send_keys(username)

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID,"pass"))
            )
            password_field=driver.find_element(By.ID,"pass")
            password_field.send_keys(password)

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID,"loginbutton"))
            )
            sign_in=driver.find_element(By.ID,"loginbutton")
            sign_in.click()

            time.sleep(10)
            break



            
