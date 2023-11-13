import allure
from data import *
from elements import FooterElement


@allure.title('Check work of about us page')
@allure.feature('Open about us page and check its URL')
def test_check_about_us_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_about_us_page()
    footer.assert_actual_url(ABOUT_US_PAGE_URL)


@allure.title('Check work of store addresses page')
@allure.feature('Open store addresses page and check its URL')
def test_check_store_addresses_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_store_addresses_page()
    footer.assert_actual_url(STORE_ADDRESSES_PAGE_URL)


@allure.title('Check work of news page')
@allure.feature('Open news page and check its URL')
def test_check_news_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_news_page()
    footer.assert_actual_url(NEWS_PAGE_URL)


@allure.title('Check work of reviews page')
@allure.feature('Open reviews page and check its URL')
def test_check_reviews_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_reviews_page()
    footer.assert_actual_url(REVIEWS_PAGE_URL)


@allure.title('Check vacancy page')
@allure.feature('Open vacancy page and check its URL')
def test_check_vacancy_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_vacancy_page()
    footer.assert_actual_url(VACANCY_PAGE_URL)


@allure.title('Check work of store contacts page')
@allure.feature('Open store contacts page and check its URL')
def test_contacts_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_contacts_page()
    footer.assert_actual_url(CONTACTS_PAGE_URL)


@allure.title('Check work of store youtube page')
@allure.feature('Open youtube page switch to it and check its URL')
def test_youtube_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_youtube()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(YOUTUBE_PAGE_URL)


@allure.title('Check work of store instagram page')
@allure.feature('Open instagram page switch to it and check its URL')
def test_instagram_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_instagram()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(INSTAGRAM_PAGE_URL)


@allure.title('Check work of facebook page')
@allure.feature('Open facebook page switch to it and check its URL')
def test_facebook_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_facebook()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(FACEBOOK_PAGE_URL)


@allure.title('Check work of vk page')
@allure.feature('Open vk page switch to it and check its URL')
def test_vk_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_vk()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(VK_PAGE_URL)


@allure.title('Check work of telegram page')
@allure.feature('Open telegram page switch to it and check its URL')
def test_telegram(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_telegram()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(TELEGRAM_PAGE_URL)


@allure.title('Check work of ok page')
@allure.feature('Open ok page switch to it and check its URL')
def test_ok_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_ok()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(OK_PAGE_URL)


@allure.title('Subscribe to newsletter from footer')
@allure.feature('Subscribe to newsletter from 5element footer')
def test_footer_subscribe_to_newsletter(driver, open_main_page):
    footer = FooterElement(driver)
    footer.fill_footer_email(TEST_USER)
    footer.check_footer_policy_agree()
    footer.subscribe_footer_newsletter()
    footer.assert_if_footer_subscription_is_done()


@allure.title('Check relevance of phone numbers in footer')
@allure.feature('Check relevance of 5element phone numbers in footer')
def test_footer_phone_numbers(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_footer_contacts()
    footer.assert_footer_contacts()


@allure.title('Check relevance of email in footer')
@allure.feature('Check relevance of 5element email in footer')
def test_footer_email_contact(driver, open_main_page):
    footer = FooterElement(driver)
    footer.assert_email_footer_contact()


@allure.title('Check work of google play page')
@allure.feature('Open google play  page switch to it and check its URL')
def test_google_play_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_google_play()
    footer.switch_to_google_play_window()
    footer.assert_actual_url(GOOGLE_PLAY_URL)


@allure.title('Check work of app store page')
@allure.feature('Open app store  page switch to it and check its URL')
def test_app_store_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_app_store()
    footer.switch_to_app_store_window()
    footer.assert_actual_url(APP_STORE_URL)


@allure.title('Check work of app gallery page')
@allure.feature('Open app gallery  page switch to it and check its URL')
def test_app_gallery_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_app_gallery()
    footer.switch_to_app_gallery_window()
    footer.assert_actual_url(APP_GALLERY_URL)
