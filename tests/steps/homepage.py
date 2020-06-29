import allure
from behave import given, when, then
from pages.homepage import homepage
from tests.framework.website import website
import selenium.webdriver.chrome


@when(u'I click "Request a Demo" link')
@allure.step("Click request demo link")
def step_impl(context):
    homepage.click_request_a_demo_link()


@when(u'I click "What is SASE" link')
@allure.step("Click what is SASE link")
def step_impl(context):
    homepage.click_what_is_SASE_link()


@when(u'I click "What is CASB" link')
@allure.step("Click what is CASB link")
def step_impl(context):
    homepage.click_what_is_CASB_link()


@when(u'I click "CASB Architecture" link')
@allure.step("Click CASB Architecture link")
def step_impl(context):
    homepage.click_CASB_architecture_link()


@when(u'I click "Free Trial" link')
@allure.step("Click Free Trial link")
def step_impl(context):
    homepage.click_free_trial()


@when(u'I click Contact link')
def step_impl(context):
    print("hello")


@when(u'I click Partner Login link')
def step_impl(context):
    homepage.click_partner_login()


@when(u'I click Customer Login link')
def step_impl(context):
    print("hello")


@when(u'I click "CASB Magic Quadrant" link')
def step_impl(context):
    homepage.click_CASB_magic_quadrant()


@when(u'I click "All Cloud Apps" link')
def step_impl(context):
    homepage.click_all_cloud_apps()


@when(u'I click "Office 365" link')
def step_impl(context):
    homepage.click_office_365()


@when(u'I click "G Suite" link')
def step_impl(context):
    homepage.click_g_suite()


@when(u'I click "Salesforce" link')
def step_impl(context):
    homepage.click_salesforce()


@when(u'I click "Box" link')
def step_impl(context):
    homepage.click_box()


@when(u'I click "Dropbox" link')
def step_impl(context):
    homepage.click_dropbox()


@when(u'I click "Exchange" link')
def step_impl(context):
    homepage.click_exchange()


@when(u'I click "Slack" link')
def step_impl(context):
    homepage.click_slack()


@when(u'I click "Amazon (AWS)" link')
def step_impl(context):
    homepage.click_amazon_aws()


@when(u'I click "Cisco Spark" link')
def step_impl(context):
    homepage.click_cisco_spark()


@when(u'I click "JIRA/Confluence" link')
def step_impl(context):
    homepage.click_jira_confluence()


@when(u'I click "Workday" link')
def step_impl(context):
    homepage.click_workday()


@then(u'I can see "Free Trial" registration page')
def step_impl(context):
    homepage.verify_free_trial_registration_page()

@then(u'I can see "Contact" page')
def step_impl(context):
    homepage.verify_contact_page()

@then(u'I can see Request a Demo page')
def step_impl(context):
    homepage.verify_request_a_demo_page()


@then(u'I can see What is SASE page')
def step_impl(context):
    homepage.verify_what_is_SASE_page()




@then(u'I can see "Partner Login" page')
def step_impl(context):
    homepage.verify_partner_login_page()


@then(u'I can see "Customer Login" page')
def step_impl(context):
    homepage.verify_customer_login_page()


@then(u'I can see "Request a Demo" registration page')
def step_impl(context):
    print("hello")


@then(u'I can see "What is SASE" page')
def step_impl(context):
    print("hello")


@then(u'I can see website title')
def step_impl(context):
    print("hello")


@then(u'I can see the company logo')
def step_impl(context):
    homepage.verify_company_logo()


@then(u'I can see "What is CASB" page')
def step_impl(context):
    print("hello")


@then(u'I can see "CASB Architecture" page')
def step_impl(context):
    print("hello")


@then(u'I can see "CASB Magic Quadrant" page')
def step_impl(context):
    print("hello")


@then(u'I can see "All Cloud Apps" page')
def step_impl(context):
    print("hello")


@then(u'I can see "Office 365" page')
def step_impl(context):
    print("hello")


@then(u'I can see "G Suite" page')
def step_impl(context):
    print("hello")


@then(u'I can see "Salesforce" page')
def step_impl(context):
    print("hello")


@then(u'I can see "Box" page')
def step_impl(context):
    print("hello")


@then(u'I can see "Dropbox" page')
def step_impl(context):
    print("hello")


@then(u'I can see "Exchange" page')
def step_impl(context):
    print("hello")


@then(u'I can see "Amazon (AWS)" page')
def step_impl(context):
    print("hello")


@then(u'I can see "Slack" page')
def step_impl(context):
    print("hello")


@then(u'I can see "JIRA/Confluence" page')
def step_impl(context):
    print("hello")


@then(u'I can see "Cisco Spark" page')
def step_impl(context):
    homepage.click_cisco_spark()


@then(u'I can see "Workday" page')
def step_impl(context):
    print("hello")
