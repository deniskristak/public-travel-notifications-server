from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DATE_STRING = "utorok, 24. január 2023"
DEPARTURE_ARRIVAL_TIME_STRING = "10:45 - 15:18"

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://regiojet.sk/?departureDate=2023-01-23&tariffs=REGULAR&fromLocationId=10202003&fromLocationType=CITY&toLocationId=10202001&toLocationType=CITY")

# Wait for the page to fully load
wait = WebDriverWait(driver, 10)
p = wait.until(EC.presence_of_element_located((By.XPATH, f"//p[contains(text(), '{DATE_STRING}')]")))

# Find the div that comes after the <p> element2
parent_div = p.find_element(By.XPATH, "following-sibling::div[contains(@class, 'w-full flex flex-col')]")

# Find the divs with attribute 'data-id' starting with 'connection-card-'
divs = parent_div.find_elements(By.CSS_SELECTOR, "div[data-id^='connection-card-']")

for div in divs:
    # Find the h2 element inside the div
    h2 = div.find_element(By.CSS_SELECTOR, "h2.h3")
    if h2.get_attribute("aria-label") == f"Spoj {DEPARTURE_ARRIVAL_TIME_STRING}":
        # Print the div if the h2 element has the expected aria-label
        span = div.find_element(By.CSS_SELECTOR, "span.sr-only")
        print(f"Pre spoj v dátume '{DATE_STRING}', ktorý pôjde {DEPARTURE_ARRIVAL_TIME_STRING} mám tento výsledok:")
        print(span.text)
        pass

# Close the browser
driver.quit()
