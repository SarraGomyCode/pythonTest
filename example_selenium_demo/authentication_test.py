from selenium import webdriver
from behave import *


@given("I am on the login page")
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://yourwebsite.com/login")


@when("I enter my valid credentials")
def step_impl(context):
    username_field = context.driver.find_element_by_name("username")
    password_field = context.driver.find_element_by_name("password")

    username_field.send_keys("testuser")
    password_field.send_keys("testpassword")
    context.driver.find_element_by_name("submit").click()


@then("I am successfully logged in")
def step_impl(context):
    assert "Welcome, testuser" in context.driver.page_source


@then("I log out")
def step_impl(context):
    context.driver.find_element_by_link_text("Logout").click()
    assert "You have been logged out." in context.driver.page_source
    context.driver.close()