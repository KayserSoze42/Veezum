from typing import List

import requests
import schedule
import time
from selenium.common.exceptions import TimeoutException

from Veezum.pages.status_page import StatusPage


class Veezum:
    """Veezum Bot Manager Class

    Attributes
    ----------------------
    ids: List[str]
        list with ids given by the Embassy

    times: List[str]
        list with times when the bot is to be executed

    Methods
    ----------------------
    checkerBot()
        checks all ids, formats and sends the result via Telegram API and returns bool

    checkOnce()


    """

    def __init__(self, ids: List[str], times: List[str], token: str) -> None:
        self.statusPage = StatusPage()

        self.ids = ids
        self.times = times

        if len(self.times) > 2:
            raise ValueError("Invalid length of times, consult the README")

        self.token = token
        self.chatID = self.getChatID()

        self.decisions = []


    def getChatID(self) -> str:

        response = requests.get(f"https://api.telegram.org/bot{self.token}/getUpdates").json()

        return response["result"][0]["message"]["chat"]["id"]


    def checkVizum(self, id: str) -> str:

        decision = ""

        # Get Embassy's Application Status Page
        self.statusPage.goto()

        # Fill in the ID input box
        self.statusPage.enterID(id)

        time.sleep(2.5)

        # Submit the ID
        self.statusPage.submit()

        # Wait for the decision, scrape the text and return the result as string
        decision = self.statusPage.getResult()

        return decision


    def scheduleBot(self) -> None:
        for time in self.times:
            schedule.every().day.at(time).do(self.checkerBot)


    def checkerBot(self) -> bool:

        if self.checkOnce():

            time.sleep(2.5)

            messageAllApproved = "All IDs Have been Approved!"
            self.sendMessage(messageAllApproved)

            schedule.clear()

            return True

        time.sleep(2.5)

        message = self.formatMessage()
        self.sendMessage(message)

        return False


    def keepChecking(self):

        # Good Ol' while True
        while True:
            schedule.run_pending()
            time.sleep(1)


    def checkOnce(self) -> bool:

        allDecided = True

        self.statusPage.map.setDriver()

        tempDecisions = []

        for id in self.ids:

            try:
                decision = self.checkVizum(id)

            except TimeoutException as e:
                decision = "N/A"

            except Exception as e:
                print(e)
                self.statusPage.map.tearDown()
                schedule.clear()
                raise

            if decision == "In Process":
                allDecided = False


            tempDecisions.append([id, decision])
            print("Decisions: ")
            print(tempDecisions)

        self.statusPage.map.tearDown()
        self.decisions = tempDecisions

        return allDecided


    def formatMessage(self) -> str:
        formattedMessage = 'Decisions\n'
        for decision in self.decisions:
            formattedMessage+= f'\n{decision[0]}\n{decision[1]}\n--\n'
        return formattedMessage


    def sendMessage(self, message: str) -> None:
        print(requests.get(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chatID}&text={message}").json())


