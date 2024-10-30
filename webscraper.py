from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Set up Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\ROOT\Desktop\chromedriver\chromedriver.exe", options=chrome_options)

# Navigate to the quote website
driver.get("https://www.brainyquote.com/")

# Wait for the quote to load
quote_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='quote']"))
)

# Get the quote text
quote_text = quote_element.text

# Print the quote
print("Quote of the day:")
print(quote_text)

# Close the browser
driver.quit()