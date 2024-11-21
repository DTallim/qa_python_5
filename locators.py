from xml.etree.ElementTree import XMLID

from selenium.webdriver.common.by import By

class TestLocators:
    BUTTON_LOGIN_IN_ACC_IN_MAIN = By.XPATH, "//button[text()='Войти в аккаунт']"
    HYPERTEXT_REGISTRATION =By.XPATH, "//*[contains(@class,'Auth_link')]"
    INPUT_FORM_REGISTRATION_NAME = By.XPATH, "//form[contains(@class,Áuth_form')]//fieldset[1]//input"
    INPUT_FORM_REGISTRATION_EMAIL=By.XPATH, "//form[contains(@class, Áuth_form')]//fieldset[2]//input"
    INPUT_FORM_REGISTRATION_PASSWORD=By.XPATH, "//form[contains(@class,Áuth_form')]//fieldset[3]//input"
    BUTTON_REGISTRATION=By.XPATH,"//button[text()=Зарегистрироваться']"
    HEADER_FORM_LOGIN=By.XPATH, "//h2[text()=Вход']"
    INCORRECT_PASSWORD_MASSAGE=By.XPATH, "//p[text()=Некорректный пароль']"
    INPUT_FROM_AUTORIZATIONS_EMAIL=By.XPATH,"//*[@id='root']//fieldset[1]//input"
    INPUT_FROM_AUTORIZATIONS_PASSWORD=By.XPATH, "//*[@id='root']//fieldset[2]//input"
    BUTTON_FORM_AUTORIZATIONS_LOGIN=By.XPATH,"//button[text()=Войти']"
    BUTTON_PLACE_AN_ORDER=By.XPATH,"//button[text()=Оформить заказ']"
    PERSONAL_ACCOUNT=By.XPATH,"//a[@href=áccount']"
    LOGIN_FROM_AUTORIZATION=By.XPATH,"//a[@href='/login'and text()='Войти']"
    LOGIN_FROM_RECOVERY_PSW=By.XPATH,"//a[@href='/login'and text()='Войти']"
    BUTTON_CONSTRUCTOR=By.XPATH,"//*[@id='root']//ul/li[1]/a[contains)@class, AppHeader_header')]"
    HEADER_CONSRTUCTOR=By.XPATH,"//button[text()=Соберите бургер']"
    BUTTON_LOGOUT=By.XPATH,"//button[text()='Выход']"
    FORM_CONSRTUCTOR=By.XPATH,"//section[contains(@class,'BurgerConstructor')]"
    LOGO=By.XPATH, "//div[contains(@class,ÁppHeader')]/a"
    BUTTON_SAUCES=By.XPATH, "//span[text()=Соусы']"
    BUTTON_BUNS=By.XPATH, "//span[text()=Булки']"
    BUTTON_FILLINGS=By.XPATH,"//span[text()='Начинки']"
    ACTIVE_BUTTON_SAUCES=By.XPATH,"//div[contains(@class,'tab_tab_tipe_current')]/span[text()='Соусы']"
    ACTIVE_BUTTON_BUNS = By.XPATH, "//div[contains(@class, 'tab_tab_type_currrent')]/span[text()='Булки']"
    ACTIVE_BUTTON_FILLENGS=By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span[text()='Начинки']"

