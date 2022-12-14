from .base_page import BasePage
from .locators import ProductPagesLocator
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_cart(self):
        btn_basket = self.browser.find_element(*ProductPagesLocator.BTN_BASKET)
        btn_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPagesLocator.BTN_BASKET), "Кнопки 'Добавить в корзину' не существует, или неверный селектор"
    
    def should_be_success_message(self):
        is_book = self.browser.find_element(*ProductPagesLocator.NAME_BOOK).text in self.browser.find_element(*ProductPagesLocator.MESSAGE).text
        assert is_book, "Нет сообщения о добавления книги в корзину или название книги в сообщении не совпадает с названием товара"

    def should_be_success_price(self):
        is_price = self.browser.find_element(*ProductPagesLocator.PRICE_BOOK).text in self.browser.find_element(*ProductPagesLocator.MESSAGE_PRICE).text
        assert is_price, "Нет сообщения со стоимостью корзины или стоимость корзины не совпадает с ценой товара"