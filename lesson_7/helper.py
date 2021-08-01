from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['hw7']


def insert_some(data):
    db.yandexmail.insert_one(data)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F' \
                        '%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1 '

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)


class Locators:
    locator_email = (By.CLASS_NAME, 'Textinput-Control')
    locator_passw = (By.ID, 'passp-field-passwd')
    locator_search_field = (By.CLASS_NAME, 'textinput__control')
    locator_count_m = (By.XPATH, "//span[@class='mail-MessagesSearchInfo-Title_misc nb-with-xs-left-gap']")
    locator_message = (By.CLASS_NAME, "mail-MessageSnippet-Item")
    locator_answer = (By.CLASS_NAME, 'mail-Toolbar-Item_reply')
    locator_topic_area = (By.XPATH, "//input[@class='composeTextField ComposeSubject-TextField']")
    locator_text_field = (By.XPATH,
                          "//div[@class='cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr']/div[1]")
    locator_send_button = (By.XPATH,
                           "//button[@class='control button2 button2_view_default button2_tone_default button2_size_l button2_theme_action button2_pin_circle-circle ComposeControlPanelButton-Button ComposeControlPanelButton-Button_action']")
    locator_from = (By.XPATH, "//span[@class='mail-MessageSnippet-FromText']")
    locator_topic = (By.XPATH, "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subject']/span")
    locator_message_text = (By.XPATH,
                            "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_firstline js-message-snippet-firstline']/span")


class MailChecker(BasePage):

    def auth(self, login, password):
        email = self.find_element(Locators.locator_email)
        email.send_keys(login)
        email.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        passw = self.find_element(Locators.locator_passw)
        self.driver.implicitly_wait(10)
        passw.send_keys(password)
        return passw.send_keys(Keys.ENTER)

    def find_messages(self, from_who):
        search_field = self.find_element(Locators.locator_search_field)
        search_field.send_keys(from_who)
        search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        count_m = self.find_element(Locators.locator_count_m)
        count_m = count_m.text
        return count_m

    def parse_info(self):
        message_from = self.driver.find_elements_by_xpath("//span[@class='mail-MessageSnippet-FromText']")
        topic = self.driver.find_elements_by_xpath(
            "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subject']/span")
        message = self.driver.find_elements_by_xpath(
            "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_firstline "
            "js-message-snippet-firstline']/span")
        return message_from, topic, message

    def save_info(self, info):
        insert_some(info)


class OpenDataPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://data.gov.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_section_electronic(self):

        self.driver.find_element_by_xpath("/html/body/div[5]/div/a[2]").click()
        self.driver.find_elements_by_xpath("//div[@class='field-item even']/a")[14].click()

    def download_all_files(self):
        cty_pages = len(self.driver.find_elements_by_xpath("//div[@class='item-list']/ul/li")[:-2])
        count_poblications = len(self.driver.find_elements_by_xpath("//div[@class='field-item even']/h2/a"))
        for page in range(cty_pages - 2):

            for post in range(count_poblications):
                self.driver.implicitly_wait(20)
                self.driver.find_elements_by_xpath("//div[@class='field-item even']/h2/a")[post].click()
                try:
                    self.driver.find_element_by_xpath("//div[@class='multi-download-link-wrapper']/div[@class='main-download-link-wrapper']/a").click()
                    self.driver.find_element_by_xpath("//div[@class='dropdown-links state-expanded']/div[@class='download']/a").click()
                    self.driver.back()
                except NoSuchElementException:
                    self.driver.back()
                    continue
            self.driver.find_elements_by_xpath("//div[@class='item-list']/ul/li")[:-2][page + 1].click()

