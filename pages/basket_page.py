from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_basket_link(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LINK), "Отсутствует кнопка корзины"

    def go_to_basket(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def should_be_not_product(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_VOTE_BASKET), "В корзине есть товар"

    def should_be_message_vote(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_VOTE_BASKET).text == "Ваша корзина пуста Продолжить покупки", "Отсутствует сообщение:'Ваша корзина пуста Продолжить покупки'"