from lesson_7.helper import MailChecker, OpenDataPage
from selenium import webdriver
import lesson_7.cfg as cfg
driver = webdriver.Chrome()
main_page = MailChecker(driver)
main_page.go_to_site()
main_page.auth(cfg.login, cfg.password)
text_message = main_page.find_messages('Гарик Бадалов')
message_from, topic, message = main_page.parse_info()
for i in range(len(main_page.parse_info()[0])):
    res = {"От": message_from[i].text, "Тема": topic[i].text, "Текст Сообщения": message[i].text}
    main_page.save_info(res)
open_data = OpenDataPage(driver)
open_data.go_to_site()
driver.implicitly_wait(60)
open_data.go_to_section_electronic()
driver.implicitly_wait(60)
open_data.download_all_files()

