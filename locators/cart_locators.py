class CartLocators:

    SEARCH_FORM = '//form[@class="h-search__form"]'
    ITEM_SEARCH = '//input[@maxlength="90"]'
    ADD_TO_CART_BUTTON = '//button[@data-product_id="784765"]'
    MOVE_TO_CART_BUTTON = '//a[@href="/cart"]'
    ADDED_ITEM = '//a[text()="Смартфон Xiaomi Redmi 10C 4GB/128GB Graphite Gray EU"]'
    DELETE_BUTTON = '//a[@data-v-5b8bab08=""]//span[text()="Удалить"]'
    ADD_SERVICE_TRIGGER = '//a[text()="Добавить сервис"]'
    ADD_SERVICE_BUTTON = '//span[text()="Добавить"]'
    ADDED_SERVICE = '//div[2]/div[2]/div/div[2]/a[1]'
    PROMOTIONAL_CODE_FIELD = '//div[2]/div/div/form/input'
    CODE_APPLY_BUTTON = '//div[2]/div/div/form/button'
    CODE_NOT_FOUND = '//div[@class="form-caption form-caption--warning ic-info"]'
