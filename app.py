import time
import pyautogui
import os
import pyperclip
import random
import xlrd
import expressvpn

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests import get

from modules.read_file import read_file_line_by_line, select_random_msg, random_string, update_file

expressvpn.api_key = "EETW9T3BSDUZ4PYCSJMR7CJ"
locations = ['us_newyork', 'us_chicago', 'us_losangeles', 'uk_london', 'ca_toronto']
location_index = 0

current_dir = os.path.dirname(os.path.abspath(__file__))

mainpath = "./assets/links"
url_gmails = "./assets/gmails.txt"

def set_clipboard(text):
    pyperclip.copy(text)


def driver_chrome_incognito():
    from undetected_chromedriver import Chrome, ChromeOptions
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    driver = Chrome(options=chrome_options, version_main = 114)

    return driver

def sign_up_create_links(driver, user_name, e_mail, passwd, url_link):
    num = 0
    driver.get("https://bitly.com/a/sign_up")
    time.sleep(2)
    username = driver.find_element(by=By.NAME, value="username")
    ActionChains(driver=driver).move_to_element(username).click().perform()
    username.send_keys(user_name)
    email = driver.find_element(by=By.NAME, value="email")
    password = driver.find_element(by=By.NAME, value="password")
    submit = driver.find_element(by=By.ID, value="submit")
    time.sleep(1)
    email.send_keys(e_mail)  
    time.sleep(1)
    password.send_keys(passwd)  
    time.sleep(1)
    try:
        submit.submit()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "link-button")))
            time.sleep(1)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Close']")))
                time.sleep(1)
                close_button = driver.find_element(by=By.XPATH, value="//button[@aria-label='Close']")
                time.sleep(1)
                close_button.click()
                time.sleep(1)
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='orb-button create-btn']")))
                    while num < 10:
                        remaining_links = read_file_line_by_line(url_link)
                        if len(remaining_links) == 0:
                            print("Generated for all links!")
                            return driver
                        else:
                            create_new = driver.find_element(by=By.XPATH, value="//button[@class='orb-button create-btn']")
                            ActionChains(driver=driver).move_to_element(create_new).click().perform()
                            time.sleep(1)
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='create-link']")))
                            create_link = driver.find_element(by=By.XPATH, value="//div[@class='create-link']")
                            create_link.click()
                            time.sleep(1)
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='https://example.com/my-long-url']")))
                            links = driver.find_element(by=By.XPATH, value="//input[@placeholder='https://example.com/my-long-url']")
                            try:
                                links.send_keys(read_file_line_by_line(url_link)[0].strip())
                                update_file(url_link, 1)
                                time.sleep(1)
                                try:
                                    links.send_keys(Keys.ENTER)
                                    time.sleep(1)
                                    num += 1
                                    try:
                                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "bitlink--MAIN")))
                                    except:
                                        links.send_keys(Keys.CONTROL + "a")
                                        time.sleep(1)
                                        links.send_keys(Keys.BACKSPACE)
                                        time.sleep(3)
                                except:
                                    pass
                            except:
                                pass
                except:
                    pass
            except:
                print("!!!!!!!!!!")
                pass
        except:
            print("-------There is account with this email already!!!------ ")
            update_file(url_gmails, 1)
            pass
    except:
        pass
    return driver

def save_to_file(driver, url_created_link):   
    try:
        generated_links_button = driver.find_element(by=By.XPATH, value="//div[@aria-label='Links Icon']")
        generated_links_button.click()
        try:
            bitly_links = driver.find_elements(by=By.CLASS_NAME, value="bitlink--MAIN")
            num_bitly_links = len(bitly_links)
            for link in bitly_links:
                shortend_url = link.get_attribute("title")
                with open(url_created_link, "a", encoding="utf-8") as created_links:
                    created_links.write("https://" + shortend_url + "\n")
                # print(shortend_url)
        except:
            pass
    except:
        pass
    driver.close()

def main():
    gmails = read_file_line_by_line(url_gmails)
    links_names = os.listdir(path=mainpath)
    bitly_links_folder = mainpath + "/bitly_links"
    # os.makedirs(bitly_links_folder)
    for links_name in links_names:
        gmails = read_file_line_by_line(url_gmails)
        url_links = mainpath + "/" + links_name
        print(url_links)
        url_created_links = bitly_links_folder + "/" + links_name
        print(url_created_links)
        for gmail in gmails:
            print(gmail)
            ip = get("https://api.ipify.org").content.decode("utf-8")
            print("--------------------------------------------------------------")
            print("----------My public IP address is " + ip + "------------------")
            num_remain_links = len(read_file_line_by_line(url_links))
            print(format(num_remain_links) + " links remained.")
            if num_remain_links == 0:
                break
            else:
                username = random_string()
                email = gmail.strip()
                password = random_string()
                driver = driver_chrome_incognito()
                print("k")
                try:
                    sign_up_create_links_driver = sign_up_create_links(driver=driver, user_name=username, e_mail=email, passwd=password, url_link=url_links)
                    time.sleep(2)
                    try:
                        save_to_file(driver=sign_up_create_links_driver, url_created_link=url_created_links)
                        time.sleep(2)
                        try:
                            update_file(url_gmails, 1)
                        except ValueError:
                            print(ValueError)
                            pass
                    except ValueError:
                        driver.close()
                        pass
                except:
                    pass
        print("Created bitly links for all of " + links_name + "!")
    print("Created all links")

if __name__ == '__main__':
    main()