# page_object
Домашнее задание к курсу Автоматизание тестирования с помощью Selenium и Python
https://stepik.org/course/575


base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

Файл test_main_page.py - тут мы выполняем сами тесты? по префиксу "test_" я понимаю что это для PyTest. Тут вызванные функции будут запускаться.

Здесь мы будем создавать функции, которым:

выдаём нужный для проверки линк
созаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
добавляем проверки, которые создавали методами в main_page.py