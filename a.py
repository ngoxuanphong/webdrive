from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

wd.get("https://market.sec.or.th/public/idisc/en/FinancialReport/FS-0000001153/19900101-20220103")


def Link_All_Company(company):
    symbol = company
    element = wd.find_element_by_id("BsCompany")
    element.clear()
    element.send_keys(symbol)
    time.sleep(2)

    element_button_search_company = wd.find_element_by_xpath(
        '//*[@id="aspnetForm"]/div[2]/div/div[3]/div[3]/div[2]/div/div/span/button/i')
    element_button_search_company.click()
    time.sleep(2)

    element_button_search_all = wd.find_element_by_id('ctl00_CPH_btSearch')
    element_button_search_all.click()
    time.sleep(2)
    element_button_search_all = wd.find_element_by_id('ctl00_CPH_btSearch')
    element_button_search_all.click()

    element_button_search_all_ = wd.find_element_by_id('ctl00_CPH_btSearch')
    ActionChains(wd).key_down(Keys.CONTROL).click(
        element_button_search_all_).key_up(Keys.CONTROL).perform()
    wd.switch_to.window(wd.window_handles[1])
    print(wd.current_url)

  # return wd.current_url
print(Link_All_Company('ADD'))
# return element_button_search_all_click_all.get_attribute('href')
