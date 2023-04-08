import os
import requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse
from tqdm import tqdm

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("Enter the URL: ")

if len(sys.argv) > 2:
    export_path = sys.argv[2]
else:
    export_path = input("Enter the path to export the resulting folder (leave blank for current folder): ")
    if not export_path:
        export_path = os.getcwd()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

try:
    driver = webdriver.Chrome(options=options)
    driver.get(url)
except Exception as e:
    print(f"Error accessing {url}: {e}")
    sys.exit(1)

# Scroll down the page to trigger the loading of the JS files
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)

# Get the page source after all JS files are loaded
try:
    page_source = driver.page_source
except Exception as e:
    print(f"Error getting page source: {e}")
    driver.quit()
    sys.exit(1)

driver.quit()

soup = BeautifulSoup(page_source, "html.parser")

# Find all script tags
script_tags = soup.find_all("script")

# Create a folder to store the downloaded files
folder_name = urlparse(url).netloc.replace(".", "_") + "_js_files"
folder_path = os.path.join(export_path, folder_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Download each JavaScript file
for script in tqdm(script_tags, desc="Downloading JavaScript files"):
    src = script.get("src")
    if src and src.endswith(".js"):
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("http"):
            pass
        else:
            src = url + src
        filename = os.path.join(folder_path, os.path.basename(src))
        try:
            response = requests.get(src)
            with open(filename, "wb") as f:
                f.write(response.content)
        except Exception as e:
            print(f"Error downloading {src}: {e}")

print(f"All JavaScript files have been downloaded to {folder_path}.")