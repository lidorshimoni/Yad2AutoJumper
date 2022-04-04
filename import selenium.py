from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(executable_path="webdriver/chromedriver.exe", options=chrome_options )

driver.get("https://my.yad2.co.il")

email =     element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
email.send_keys("lidor.shim@gmail.com")

password =      element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "password"))
    ) 
password.send_keys("L556622076l")

login_submit=     element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/main/div/section[1]/div[1]/form/fieldset/div/button'))
    )
login_submit.click()

time.sleep(3)

driver.get("https://my.yad2.co.il/newOrder/index.php?action=personalAreaFeed&CatID=2&SubCatID=1")

ad = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id=\"feed\"]/tbody/tr[2]"))
    )
ad.click()

jumper_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "bounceRatingOrderBtn"))
    )
jumper_button.click()

print("DONE!")
exit()