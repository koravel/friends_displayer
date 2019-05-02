from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SeleniumService:
    __error_start = "could not get {} element"
    __error_start_many = "{}{}".format(__error_start, "s")

    def __init__(self, logger, browser):
        self._logger = logger
        self._browser = browser

    def get_clickable_element(self, wait_time, search_rule, search_item):
        try:
            wait = WebDriverWait(self._browser, wait_time)
            return wait.until(expected_conditions.element_to_be_clickable((search_rule, search_item)))
        except TimeoutException:
            self._logger.log_error(
                f"{self.__error_start.format('clickable')} [ {search_item} ] after {wait_time} sec")
            return None

    def get_text_element(self, wait_time, search_rule, search_item):
        try:
            wait = WebDriverWait(self._browser, wait_time)
            return wait.until(expected_conditions.presence_of_element_located((search_rule, search_item)))
        except TimeoutException:
            self._logger.log_error(
                f"{self.__error_start.format('text')} element [ {search_item} ] after {wait_time} sec")
            return None

    def get_element_list(self, wait_time, search_rule, search_item):
        try:
            wait = WebDriverWait(self._browser, wait_time)
            return wait.until(expected_conditions.presence_of_all_elements_located((search_rule, search_item)))
        except TimeoutException:
            self._logger.log_error(
                f"{self.__error_start_many.format('list of')} elements [ {search_item} ] after {wait_time} sec")
            return None
