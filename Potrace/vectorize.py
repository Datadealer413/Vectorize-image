from pathlib import Path
from genericpath import isdir
import time, os, glob
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


cwd = os.getcwd()
#parent_folder = os.path.abspath(os.path.join(cwd, os.pardir))
image_folder = cwd + "\\images"
vec_folder = cwd + "\\processed"

if os.path.isdir(vec_folder):
    pass
else:
    os.mkdir(vec_folder)

chrome_options = webdriver.ChromeOptions() 
prefs = {"download.default_directory" : vec_folder}
chrome_options.add_experimental_option("prefs", prefs)
print("download.default_directory={}".format(vec_folder))
driver = webdriver.Chrome(
        options=chrome_options,
        service=Service(ChromeDriverManager().install())
    )

driver.get("https://vectorizer.ai/")
driver.maximize_window()

def upload_file(url):    
    field = driver.find_element(by=By.ID, value="FileInput-Field")
    driver.execute_script("arguments[0].style.display = 'block';", field)
    field.send_keys(url)
    time.sleep(5)

def download_file(entry):
    download_button = driver.find_element(by=By.XPATH, value="//*[@id='App-DownloadLink']")
    download_button.click()
    close_button = driver.find_element(by=By.XPATH, value="//*[@id='App-Toolbar-Exit']")
    close_button.click()
    newest = max(glob.glob(vec_folder+"\\*.*"), key=os.path.getmtime)
    newest_loc = Path(newest)
    newest_loc.rename(vec_folder + "\\" + os.path.splitext(entry)[0] + ".svg")

if __name__ == "__main__":

    cnt = 0
    for entry in os.listdir(image_folder):
        if os.path.isfile(os.path.join(image_folder, entry)):
            upload_file(image_folder + "\\" + entry)
            download_file(entry)
            cnt += 1
            print("Processed {}".format(cnt))
