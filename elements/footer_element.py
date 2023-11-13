import allure
from helpers import BasePage
from locators import FooterLocators
from data import *


class FooterElement(BasePage, FooterLocators):

    @allure.step('Open main page')
    def open(self):
        self.driver.get(DOMAIN)

    @allure.step('Click on youtube page')
    def click_on_youtube(self):
        self.click_on(self.YOUTUBE_LOCATOR)

    @allure.step('Click on instagram page')
    def click_on_instagram(self):
        self.click_on(self.INSTAGRAM_LOCATOR)

    @allure.step('Click on facebook page')
    def click_on_facebook(self):
        self.click_on(self.FACEBOOK_LOCATOR)

    @allure.step('Click on vk page')
    def click_on_vk(self):
        self.click_on(self.VK_LOCATOR)

    @allure.step('Click on telegram page')
    def click_on_telegram(self):
        self.click_on(self.TELEGRAM_LOCATOR)

    @allure.step('Click on ok page')
    def click_on_ok(self):
        self.click_on(self.OK_LOCATOR)

    @allure.step('Switch to social media window')
    def switch_to_social_media_window(self):
        self.switch_to_new_window()

    @allure.step('Switch to google play window')
    def switch_to_google_play_window(self):
        self.switch_to_new_window()

    @allure.step('Switch to app store window')
    def switch_to_app_store_window(self):
        self.switch_to_new_window()

    @allure.step('Switch to app gallery window')
    def switch_to_app_gallery_window(self):
        self.switch_to_new_window()

    @allure.step('Click on about us page')
    def click_on_about_us_page(self):
        self.click_on(self.ABOUT_US_LOCATOR)

    @allure.step('Click on store addresses page')
    def click_on_store_addresses_page(self):
        self.click_on(self.STORE_ADDRESSES_LOCATOR)

    @allure.step('Click on news page')
    def click_on_news_page(self):
        self.click_on(self.NEWS_LOCATOR)

    @allure.step('Click on reviews page')
    def click_on_reviews_page(self):
        self.click_on(self.REVIEWS_LOCATOR)

    @allure.step('Click on vacancy page')
    def click_on_vacancy_page(self):
        self.click_on(self.VACANCY_LOCATOR)

    @allure.step('Click on contacts page')
    def click_on_contacts_page(self):
        self.click_on(self.CONTACTS_PAGE)

    @allure.step('Fill footer email')
    def fill_footer_email(self, user):
        self.fill(self.FOOTER_EMAIL, user['email'])

    @allure.step('Check footer policy agree')
    def check_footer_policy_agree(self):
        self.check_checkbox(self.FOOTER_POLICY_AGREE)

    @allure.step('Subscribe footer newsletter')
    def subscribe_footer_newsletter(self):
        self.click_on(self.FOOTER_SUBSCRIBE_NEWSLETTER_BUTTON)

    @allure.step('Assert footer subscription')
    def assert_if_footer_subscription_is_done(self):
        self.assert_element_is_displayed(self.FOOTER_SUBSCRIBE_NEWSLETTER_SUCCESS, True)

    @allure.step('Click on footer contacts')
    def click_on_footer_contacts(self):
        self.click_on(self.CONTACTS_FOOTER)

    @allure.step('Assert mts number')
    def assert_mts_number(self):
        self.assert_text_in_element(self.MTS_NUMBER, CONTACTS['mts'])

    @allure.step('Assert A1 number')
    def assert_a1_number(self):
        self.assert_text_in_element(self.A1_NUMBER, CONTACTS['a1'])

    @allure.step('Assert LIFE number')
    def assert_life_number(self):
        self.assert_text_in_element(self.LIFE_NUMBER, CONTACTS['life'])

    @allure.step('Assert City number')
    def assert_city_number(self):
        self.assert_text_in_element(self.CITY_NUMBER, CONTACTS['city_number'])

    @allure.step('Assert footer email')
    def assert_email_footer_contact(self):
        self.assert_text_in_element(self.EMAIL_FOOTER_CONTACT, CONTACTS['email'])

    @allure.step('Assert footer contacts')
    def assert_footer_contacts(self):
        self.assert_mts_number()
        self.assert_a1_number()
        self.assert_life_number()
        self.assert_city_number()

    @allure.step('Click on google play')
    def click_on_google_play(self):
        self.click_on(self.GOOGLE_PLAY)

    @allure.step('Click on app store')
    def click_on_app_store(self):
        self.click_on(self.APP_STORE)

    @allure.step('Click on app gallery')
    def click_on_app_gallery(self):
        self.click_on(self.APP_GALLERY)
