from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage


@given(u'I got navigated to Home page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.get("https://tutorialsninja.com/demo/")
    expected_page_title = "Your Store"
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_home_page_title(expected_page_title)


@when(u'I enter valid product say "{product}" into the Search box field')
def step_impl(context, product):
    # context.driver.find_element(By.NAME, "search").send_keys("HP")
    context.home_page.enter_product_into_search_box_field(product)


@when(u'I click on Search button')
def step_impl(context):
    # context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()
    context.search_page = context.home_page.click_on_search_button()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    # assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    # context.driver.quit()
    assert context.search_page.display_status_of_product()


@when(u'I enter invalid product say "{product}" into the Search box field')
def step_impl(context, product):
    # context.driver.find_element(By.NAME, "search").send_keys("Honda")
    context.home_page.enter_product_into_search_box_field(product)


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria.aaaaa"
    # assert context.driver.find_element(
    #     By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    # context.driver.quit()

    assert context.search_page.display_status_of_message(expected_text)

@when(u'I dont enter anything into Search box field')
def step_impl(context):
    # context.driver.find_element(By.NAME, "search").send_keys("")
    context.home_page.enter_product_into_search_box_field("")