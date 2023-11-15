from helpers import BasePage
from data import *


class MainPage(BasePage):

    def open(self):
        self.driver.get(DOMAIN)
