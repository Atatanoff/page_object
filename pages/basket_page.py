from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_link(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LINK), "Отсутствует кнопка корзины"

    def go_to_basket(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def should_be_not_product(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_VOID_BASKET), "В корзине есть товар"

    def should_be_message_void(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_VOID_BASKET).text == "Your basket is empty. Continue shopping", "Отсутствует сообщение:'Ваша корзина пуста Продолжить покупки'"
