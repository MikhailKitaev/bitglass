from framework.website import website
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from tests.data import links_header


class Homepage():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Homepage()
        return cls.instance

    def __init__(self):
        self.driver = website.get_driver()

    def verify_company_logo(self):
        # Ex:
        try:
            self.driver.find_element_by_link_text("logo")
        except NoSuchElementException:
            return False
        return True

    def verify_website_header(self, row):
        # Ex:
        header = self.driver.find_element_by_xpath('//*[@id="hs_cos_wrapper_module_15556240492822395"]/div/ul').text
        assert row in header, "{} not present in header".format(row)

    def verify_website_menu(self, row):
        # Ex:
        menu = self.driver.find_element_by_xpath('//*[@id="hs_menu_wrapper_module_157886483963326_"]/ul').text
        assert row in menu, "{} not present in menu".format(row)

    def click_request_a_demo_link(self):
        try:
            self.driver.find_element_by_xpath("//*[@id='hs_menu_wrapper_module_157886483963326_']/ul/li[1]/a").click()
        except NoSuchElementException:
            return False
        return True

    def verify_request_a_demo_page(self):
        try:
            assert "Free Trial" in self.driver.title
        except NoSuchElementException:
            return False
        return True

    def click_what_is_SASE_link(self):
        try:
            element_to_hover_over = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/span/div[2]/ul/li[2]/a")

            hover = ActionChains().move_to_element(element_to_hover_over)
            hover.perform()
            self.driver.find_element_by_link_text("What Is SASE?").click()
        except NoSuchElementException:
            return False
        return True

    def click_free_trial(self):
        try:
            self.driver.find_element_by_xpath(links_header.free_trial["xpath"]).click()
        except NoSuchElementException:
            return False
        return True

    def verify_what_is_SASE_page(self):

        try:
            dropArrow = self.driver.find_element_by_xpath('//*[@id="hs_menu_wrapper_module_157886483963326_"]/ul/li[2]/a')
            dropArrow.click()

            dropdown1 = self.driver.find_element_by_xpath(
                '//*[@id="hs_menu_wrapper_module_157886483963326_"]/ul/li[2]/ul/li[1]/a')
            dropdown1.click()
        except NoSuchElementException:
            return False
        return True

    def click_SASE(self):
        try:
            self.driver.find_element_by_xpath(links_header.SASE).click()
        except NoSuchElementException:
            return False
        return True

    def click_products(self):
        try:
            self.driver.find_element_by_xpath(links_header.products).click()
        except NoSuchElementException:
            return False
        return True

    def click_what_is_SASE_link(self):
        try:
            self.driver.find_element_by_xpath(links_header.what_is_sase).click()
        except NoSuchElementException:
            return False
        return True

    def click_partner_login(self):
        try:
            self.driver.find_element_by_xpath(links_header.partner_login["xpath"]).click()
        except NoSuchElementException:
            return False
        return True

    def click_partner_login(self):
        try:
            self.driver.find_element_by_xpath(links_header.customer_login["xpath"]).click()
        except NoSuchElementException:
            return False
        return True


    def click_what_is_CASB_link(self):
        try:
            self.driver.find_element_by_xpath(links_header.what_is_casb).click()
        except NoSuchElementException:
            return False
        return True

    def click_request_a_demo_link(self):
        try:
            self.driver.find_element_by_xpath(links_header.request_a_demo).click()
        except NoSuchElementException:
            return False
        return True

    def click_what_is_CASB_link(self):
        try:
            self.driver.find_element_by_xpath(links_header.casb_magic_quadrant).click()
        except NoSuchElementException:
            return False
        return True

    def click_CASB_architecture_link(self):
        try:
            self.driver.find_element_by_xpath(links_header.casb_architecture).click()
        except NoSuchElementException:
            return False
        return True

    def click_CASB_magic_quadrant(self):
        try:
            self.driver.find_element_by_xpath(links_header.casb_magic_quadrant).click()
        except NoSuchElementException:
            return False
        return True

    def click_all_cloud_apps(self):
        try:
            self.driver.find_element_by_xpath(links_header.all_cloud_apps).click()
        except NoSuchElementException:
            return False
        return True

    def click_office_365(self):
        try:
            self.driver.find_element_by_xpath(links_header.office_365).click()
        except NoSuchElementException:
            return False
        return True

    def click_g_suite(self):
        try:
            self.driver.find_element_by_xpath(links_header.g_suite).click()
        except NoSuchElementException:
            return False
        return True

    def click_salesforce(self):
        try:
            self.driver.find_element_by_xpath(links_header.salesforce).click()
        except NoSuchElementException:
            return False
        return True

    def click_box(self):
        try:
            self.driver.find_element_by_xpath(links_header.box).click()
        except NoSuchElementException:
            return False
        return True

    def click_dropbox(self):
        try:
            self.driver.find_element_by_xpath(links_header.dropbox).click()
        except NoSuchElementException:
            return False
        return True

    def click_exchange(self):
        try:
            self.driver.find_element_by_xpath(links_header.exchange).click()
        except NoSuchElementException:
            return False
        return True

    def click_amazon_aws(self):
        try:
            self.driver.find_element_by_xpath(links_header.amazon_aws).click()
        except NoSuchElementException:
            return False
        return True

    def click_slack(self):
        try:
            self.driver.find_element_by_xpath(links_header.slack).click()
        except NoSuchElementException:
            return False
        return True

    def click_jira_confluence(self):
        try:
            self.driver.find_element_by_xpath(links_header.jira_confluece).click()
        except NoSuchElementException:
            return False
        return True

    def click_cisco_spark(self):
        try:
            self.driver.find_element_by_xpath(links_header.cisco_spark).click()
        except NoSuchElementException:
            return False
        return True

    def click_workday(self):
        try:
            self.driver.find_element_by_xpath(links_header.workday).click()
        except NoSuchElementException:
            return False
        return True

    def verify_free_trial_registration_page(self):
        try:
            assert self.driver.title in links_header.free_trial["title"], "{} not present in title".format()
        except NoSuchElementException:
            return False
        return True

    def verify_contact_page(self):
        try:
            assert self.driver.title in links_header.contact["title"], "{} not present in title".format()
        except NoSuchElementException:
            return False
        return True

    def verify_partner_login_page(self):
        try:
            assert self.driver.title in links_header.partner_login["title"], "{} not present in title".format()
        except NoSuchElementException:
            return False
        return True

    def verify_customer_login_page(self):
        try:
            assert self.driver.title in links_header.customer_login["title"], "{} not present in title".format()
        except NoSuchElementException:
            return False
        return True












homepage = Homepage.get_instance()