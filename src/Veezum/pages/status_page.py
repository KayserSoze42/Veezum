from typing import Any

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class StatusPageMap:

    def __init__(self):
        self.driver: webdriver.Chrome = self.getDriver()
        self.wait = WebDriverWait(self.driver, 5)

        self.setDriver()


    def getDriver(self) -> Any:
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

    def setDriver(self) -> None:
        if self.driver is None:
            options = Options()
            self.driver = self.getDriver()

    def tearDown(self) -> None:
        if self.driver is not None:
            self.driver.quit()

    def getFormInput(self) -> WebElement:
        try:
            # Wait for the ID input box to appear and then pass through the id
            formInput = self.wait.until(
                EC.presence_of_element_located((By.ID, "edit-ioff-zov"))
            )

        except Exception as e:
            self.tearDown()
            print(e.args)
            raise

        return formInput

    def getSubmitButton(self) -> WebElement:
        try:
            button: WebElement= self.driver.find_element(By.ID, "edit-submit-button")

        except Exception as e:
            self.tearDown()
            print(e.args)
            raise

        return button

    def getResultSpan(self) -> WebElement:
        try:
            spanElement = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.alert")) #/html/body/div[2]/div/section/div[1]/ul/li[1]/p/span
            )

        except Exception as e:
            self.tearDown()
            print(e.args)
            raise

        return spanElement

    def getResultID(self) -> WebElement:
        try:
            resultIDElement = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".placeholder"))
            )

        except Exception as e:
            self.tearDown()
            print(e.args)
            raise

        return resultIDElement


class StatusPage:

    def __init__(self) -> None:
        self.map: StatusPageMap = StatusPageMap()


    def goto(self) -> None:
        self.map.driver.get("https://frs.gov.cz/en/ioff/application-status")

    def enterID(self, id: str) -> None:
        self.map.getFormInput().send_keys(id)

    def submit(self) -> None:
        self.map.getSubmitButton().click()

    def getResult(self) -> str:
        return self.map.getResultSpan().get_attribute("innerText")
