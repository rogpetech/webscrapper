# pluralsight.py
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options



def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")

    # This is not needed if chromedriver is already on your path:
    chromedriver_path = "/Users/rodolfopeixoto/bin/chromedriver"

    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    # options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows
    driver = webdriver.Chrome(options=options, chromedriver_path=executable_path)
    return driver


def getCourses(driver, search_keyword):
    # Step 1: Go to pluralsight.com, category section with selected search keyword
    driver.get("https://www.inm.gob.mx/sae/publico/pt/solicitud.html")
    # wait for the element to load
    try:
        WebDriverWait(driver, 5).until(lambda s: s.find_element_by_id("autorizacionElectronicaForm").is_displayed())
    except TimeoutException:
        print("TimeoutException: Element not found")
        return None

    # Step 2: Create a parse tree of page sources after searching
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # Step 3: Iterate over the search result and fetch the course
    nombre = driver.find_element_by_id('nombre').send_keys("Rodolfo")
    apellidos = driver.find_element_by_id('nombre').send_keys("Gomes Peixoto")
    sexo = Select(driver.find_element_by_id("sexo"))
    sexo.select_by_value('1')

# create the driver object.
driver = configure_driver()
search_keyword = "Web Scraping"
getCourses(driver, search_keyword)
# close the driver.
driver.close()
