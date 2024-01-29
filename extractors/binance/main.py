from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--headless')  # Ejemplo de argumento para modo sin cabeza
# Añade aquí otros argumentos si es necesario

driver = webdriver.Remote(
		command_executor='http://selenium-docker:4444/wd/hub',
		options=options
)

# Navega a Google
driver.get("http://www.google.com")

# Encuentra el campo de búsqueda y escribe algo
elem = driver.find_element(by="name", value="q")
elem.clear()
elem.send_keys("OpenAI")
elem.send_keys(Keys.RETURN)

# No olvides cerrar el navegador después de tu prueba
driver.quit()
