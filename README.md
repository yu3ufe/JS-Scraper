# JS-Scraper

JS-Scraper is a Python script that uses Selenium and BeautifulSoup to scrape JavaScript files from a given website. The script opens the website using a headless Chrome browser, scrolls down the page to trigger the loading of JavaScript files, and then downloads each file to a specified folder. The script is easy to use and can be customized to fit your needs.

## Support

If you find this project useful and would like to support its development, you can buy me a coffee by clicking the button below:

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/yu3ufe)

Your support is greatly appreciated!

## Usage

To use JS-Scraper, you will need to have Python 3 installed on your computer, as well as the following Python packages:

- Selenium
- BeautifulSoup
- requests
- tqdm

You can install these packages using `pip` by running the following command:

```
pip install selenium beautifulsoup4 requests tqdm
```

You will also need to have the Chrome browser installed on your computer and download the appropriate version of the Chrome driver for your operating system from [here](https://sites.google.com/chromium.org/driver/).

Once you have installed the required packages and downloaded the Chrome driver, you can run the script from the command line by navigating to the directory where the script is located and running the following command:

```
python js_scraper.py [URL] [EXPORT_PATH]
```

Replace `[URL]` with the URL of the website you want to scrape and `[EXPORT_PATH]` with the path where you want to export the resulting folder. If you don't provide these arguments, the script will prompt you for them at runtime.

The script will open the website using a headless Chrome browser, scroll down the page to trigger the loading of JavaScript files, and then download each file to a folder named after the site's domain name in the specified export path. A progress bar will show the progress of downloading the JavaScript files.

## Customization

You can customize JS-Scraper to fit your specific needs by modifying the code. For example, you can change the number of times the page is scrolled or the delay between scrolls by modifying the values in this loop:

```python
# Scroll down the page to trigger the loading of the JS files
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
```

You can also add support for downloading other types of files, such as CSS files or images, by modifying this part of the code:

```python
# Find all script tags
script_tags = soup.find_all("script")

# Download each JavaScript file
for script in tqdm(script_tags, desc="Downloading JavaScript files"):
    src = script.get("src")
    if src and src.endswith(".js"):
        ...
```

You can add error handling for cases where the website is not accessible or the page source cannot be obtained by wrapping relevant parts of code in try-except blocks.

Feel free to experiment with different modifications to make JS-Scraper work best for your needs.

## Contributions

Contributions are welcome! If you find any bugs or have suggestions for improving the script, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
