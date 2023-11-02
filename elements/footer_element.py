from helpers import BasePage
from locators import FooterLocators
from data import *


class FooterElement(BasePage, FooterLocators):

    def open(self):
        self.driver.get('https://5element.by/')

    def click_on_youtube(self):
        self.click_on(self.YOUTUBE_LOCATOR)

    def click_on_instagram(self):
        self.click_on(self.INSTAGRAM_LOCATOR)

    def click_on_facebook(self):
        self.click_on(self.FACEBOOK_LOCATOR)

    def click_on_vk(self):
        self.click_on(self.VK_LOCATOR)

    def click_on_telegram(self):
        self.click_on(self.TELEGRAM_LOCATOR)

    def click_on_ok(self):
        self.click_on(self.OK_LOCATOR)

    def switch_to_social_media_window(self):
        self.switch_to_new_window()

    def switch_to_google_play_window(self):
        self.switch_to_new_window()

    def switch_to_app_store_window(self):
        self.switch_to_new_window()

    def switch_to_app_gallery_window(self):
        self.switch_to_new_window()

    def click_on_about_us_page(self):
        self.click_on(self.ABOUT_US_LOCATOR)

    def click_on_store_addresses_page(self):
        self.click_on(self.STORE_ADDRESSES_LOCATOR)

    def click_on_news_page(self):
        self.click_on(self.NEWS_LOCATOR)

    def click_on_reviews_page(self):
        self.click_on(self.REVIEWS_LOCATOR)

    def click_on_vacancy_page(self):
        self.click_on(self.VACANCY_LOCATOR)

    def click_on_contacts_page(self):
        self.click_on(self.CONTACTS_PAGE)

    def fill_footer_email(self, user):
        self.fill(self.FOOTER_EMAIL, user['email'])

    def check_footer_policy_agree(self):
        self.check_checkbox(self.FOOTER_POLICY_AGREE)

    def subscribe_footer_newsletter(self):
        self.click_on(self.FOOTER_SUBSCRIBE_NEWSLETTER_BUTTON)

    def assert_if_footer_subscription_is_done(self):
        self.assert_element_is_displayed(self.FOOTER_SUBSCRIBE_NEWSLETTER_SUCCESS, True)

    def click_on_footer_contacts(self):
        self.click_on(self.CONTACTS_FOOTER)

    def assert_mts_number(self):
        self.assert_text_in_element(self.MTS_NUMBER, CONTACTS['mts'])

    def assert_a1_number(self):
        self.assert_text_in_element(self.A1_NUMBER, CONTACTS['a1'])

    def assert_life_number(self):
        self.assert_text_in_element(self.LIFE_NUMBER, CONTACTS['life'])

    def assert_city_number(self):
        self.assert_text_in_element(self.CITY_NUMBER, CONTACTS['city_number'])

    def assert_email_footer_contact(self):
        self.assert_text_in_element(self.EMAIL_FOOTER_CONTACT, CONTACTS['email'])

    def assert_footer_contacts(self):
        self.assert_mts_number()
        self.assert_a1_number()
        self.assert_life_number()
        self.assert_city_number()

    def click_on_google_play(self):
        self.click_on(self.GOOGLE_PLAY)

    def click_on_app_store(self):
        self.click_on(self.APP_STORE)

    def click_on_app_gallery(self):
        self.click_on(self.APP_GALLERY)
