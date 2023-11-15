from data import *
from elements import FooterElement


# 10
def test_check_about_us_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_about_us_page()
    footer.assert_actual_url(ABOUT_US_PAGE_URL)


# 11
def test_check_store_addresses_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_store_addresses_page()
    footer.assert_actual_url(STORE_ADDRESSES_PAGE_URL)


# 12
def test_check_news_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_news_page()
    footer.assert_actual_url(NEWS_PAGE_URL)


# 13
def test_check_reviews_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_reviews_page()
    footer.assert_actual_url(REVIEWS_PAGE_URL)


# 14
def test_check_vacancy_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_vacancy_page()
    footer.assert_actual_url(VACANCY_PAGE_URL)


# 15
def test_contacts_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_contacts_page()
    footer.assert_actual_url(CONTACTS_PAGE_URL)


# 16
def test_youtube_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_youtube()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(YOUTUBE_PAGE_URL)


# 17
def test_instagram_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_instagram()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(INSTAGRAM_PAGE_URL)


# 18
def test_facebook_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_facebook()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(FACEBOOK_PAGE_URL)


# 19
def test_vk_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_vk()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(VK_PAGE_URL)


# 20
def test_telegram(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_telegram()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(TELEGRAM_PAGE_URL)


# 21
def test_ok_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_ok()
    footer.switch_to_social_media_window()
    footer.assert_actual_url(OK_PAGE_URL)


# 22
def test_footer_subscribe_to_newsletter(driver, open_main_page):
    footer = FooterElement(driver)
    footer.fill_footer_email(TEST_USER)
    footer.check_footer_policy_agree()
    footer.subscribe_footer_newsletter()
    footer.assert_if_footer_subscription_is_done()


def test_footer_phone_numbers(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_footer_contacts()
    footer.assert_footer_contacts()


def test_footer_email_contact(driver, open_main_page):
    footer = FooterElement(driver)
    footer.assert_email_footer_contact()


def test_google_play_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_google_play()
    footer.switch_to_google_play_window()
    footer.assert_actual_url(GOOGLE_PLAY_URL)


def test_app_store_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_app_store()
    footer.switch_to_app_store_window()
    footer.assert_actual_url(APP_STORE_URL)


def test_app_gallery_page(driver, open_main_page):
    footer = FooterElement(driver)
    footer.click_on_app_gallery()
    footer.switch_to_app_gallery_window()
    footer.assert_actual_url(APP_GALLERY_URL)
