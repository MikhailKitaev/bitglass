import allure
from pages.homepage import homepage
from behave import given, when, then
from tests.framework.website import website


@given(u'I load the website')
@allure.step("Load the website")
def step_impl_load_website(context):
    website.load_website()


@when(u'I go to "{page}" page')
def step_impl_goto_page(context, page):
    website.goto_page(page)


@then(u'I see this component "{component}"')
@allure.step(u'I see this component "{component}"')
def step_impl_verify_component(context, component):
    website.verify_component_exists(component)


@when(u'I click "SASE"')
def step_impl(context):
        homepage.click_SASE()

@when(u'I click "Products"')
def step_impl(context):
        homepage.click_products()





