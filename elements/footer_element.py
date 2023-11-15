from helpers import BasePage


class FooterElement(BasePage):
    YOUTUBE_LOCATOR = '//a[@href="https://www.youtube.com/user/5elementBelarus"]'
    INSTAGRAM_LOCATOR = '//a[@aria-label="instagram"]'
    FACEBOOK_LOCATOR = '//a[@aria-label="facebook"]'
    VK_LOCATOR = '//a[@aria-label="vk"]'
    TELEGRAM_LOCATOR = '//a[@aria-label="telegram"]'
    OK_LOCATOR = '//a[@aria-label="ok"]'
    ABOUT_US_LOCATOR = '//a[text()="О нас"]'
    STORE_ADDRESSES_LOCATOR = '//a[text()="Адреса магазинов"]'
    NEWS_LOCATOR = '//a[text()="Новости"]'
    REVIEWS_LOCATOR = '//a[text()="Статьи и обзоры"]'
    VACANCY_LOCATOR = '//a[text()="Вакансии"]'
    CONTACTS_PAGE = '//a[text()="Контакты"]'
    FOOTER_EMAIL = '//input[@placeholder="Электронная почта"]'
    FOOTER_POLICY_AGREE = '//label[@data-v-88f64d10=""]//div[@class="inp-box__view"]'
    FOOTER_SUBSCRIBE_NEWSLETTER_BUTTON = '//span[text()="Подписаться"]'
    FOOTER_SUBSCRIBE_NEWSLETTER_SUCCESS = '//div[text()="Благодарим Вас"]'

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


