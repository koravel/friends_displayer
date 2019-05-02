from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from service.selenium import SeleniumService
from service.selenium.friends_displayer import *


class FriendsDisplayer(SeleniumService):
    def __init__(self, driver_location, logger, actions_delay):
        logger.log_info("Initializing friends_displayer service...")
        if driver_location == "":
            browser = webdriver.Chrome()
        else:
            browser = webdriver.Chrome(driver_location)
        super().__init__(logger, browser)
        self.__actions_delay = actions_delay

        try:
            self._browser.get(facebook_link)
        except WebDriverException:
            self._logger.log_critical(f"Cannot pass through invalid link:{facebook_link}")
            raise ConnectionError("")

        self._browser.maximize_window()

    def login(self, login, password):
        self.login = login
        self.password = password

        self._logger.log_info("Entering login...")
        self.get_text_element(self.__actions_delay, By.ID, email_box_id).send_keys(login)

        self._logger.log_info("Entering password...")
        self.get_text_element(self.__actions_delay, By.ID, password_box_id).send_keys(password)

        self._logger.log_info("Pushing login button... I can't handle it, help me!")
        self.get_clickable_element(self.__actions_delay, By.ID, login_button_id).click()

        self._logger.log_info("Skipping annoying popup...")
        webdriver.ActionChains(self._browser).send_keys(Keys.ESCAPE).perform()

    def get_friends_dict(self):
        self._logger.log_info("Go to profile...")
        self.get_clickable_element(self.__actions_delay, By.CSS_SELECTOR, profile_css_selector).click()

        self._logger.log_info("Go to friends tab...")
        self.get_clickable_element(self.__actions_delay, By.CSS_SELECTOR, friends_tab_css_selector).click()

        self._logger.log_info("Extracting friend info containers...")
        friend_containers = self.get_element_list(self.__actions_delay, By.CSS_SELECTOR, friend_containers_css_selector)

        friends = dict()

        self._logger.log_info("Formatting data...")
        for item in friend_containers:
            link = item.get_attribute("href").replace(excess_profile_link_data, "")[:-1]
            friends[item.text] = link

        self._logger.log_info("Printing data...")
        text = ""
        for key, value in friends.items():
            text += f"\n{result_separator}{result_format.format(key, value)}"
        text += f"\n{result_separator}"

        self._logger.log_info(f"\n{text}")

    def finalize(self):
        self._logger.log_info("Shutting down friends_displayer service...")
        self._browser.quit()
