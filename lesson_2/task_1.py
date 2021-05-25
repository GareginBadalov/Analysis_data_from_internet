from bs4 import BeautifulSoup
import lxml
import requests


vacancy_hh = 'developer' #input("Введите вакансию")
page = 2 #input("Введите количество")
final_dict = {'hh.ru': [], 'suoerjob': []}
for pg in range(page):
    url_hh = f'https://krasnodar.hh.ru/search/vacancy?clusters=true&area=53&enable_snippets=true&salary=&only_with_salary=true&st=searchVacancy&text={vacancy_hh}&page={pg}'.encode('utf-8')
    url_sj = f'https://www.superjob.ru/vacancy/search/?keywords={vacancy_hh}&payment_defined=1&geo%5Bt%5D%5B0%5D=4&click_from=fastFilter&page={pg + 1}'.encode('utf-8')
    resourse_hh = url_hh[:24]
    resourse_sj = url_sj[:24]
    response_hh = requests.get(url_hh, headers={
          'User-Agent': 'PostmanRuntime/7.28.0',
          'Content-Type': 'application/json'
        })
    response_sj = requests.get(url_sj, headers={
        'User-Agent': 'PostmanRuntime/7.28.0',
        'Content-Type': 'application/json'
    })
    soup_hh = BeautifulSoup(response_hh.text, 'lxml')
    link_hh = [x for x in soup_hh.findAll('a', 'bloko-link') if 'krasnodar.hh.ru' in x["href"]]
    vacancy_hh = soup_hh.findAll('a', {"class": "bloko-link",
                                 "data-qa": "vacancy-serp__vacancy-title"}, limit=100)
    lenght_hh = len(vacancy_hh)
    salary_hh = [x for i, x in enumerate(soup_hh.findAll('span', 'bloko-section-header-3 bloko-section-header-3_lite')) if i % 2 > 0]

    for item in range(lenght_hh):
        if pg == 0:
            final_dict['hh.ru'].append({'Наименнование вакансии': vacancy_hh[item].text})
            final_dict['hh.ru'][item]['зарплата'] = salary_hh[item].text
            final_dict['hh.ru'][item]['ссылка'] = link_hh[item]['href']
            final_dict['hh.ru'][item]['сайт-источник'] = resourse_hh
        else:
            final_dict['hh.ru'][item]['Наименнование вакансии'] = vacancy_hh[item].text
            final_dict['hh.ru'][item]['зарплата'] = salary_hh[item].text
            final_dict['hh.ru'][item]['ссылка'] = link_hh[item]['href']
            final_dict['hh.ru'][item]['сайт-источник'] = resourse_hh


print(final_dict)


