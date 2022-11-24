from behave import *
# Given, When,And,But,Then->Gherrkin Synthax
# Given = seteaza situatia curenta
# When = defineste pasii din test
# Then = efectueaza verificarea testului

@Given('sign_in: I am a user on Jules sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()

@When('sign_in: I set my email to "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)

@When('sign_in: I set the password to "{pass}"')
def step_impl(context, pwd):
    context.sign_in_page.set_pass(pwd)

@When('sign_in: I click the login button')
def step_impl(context):
    context.sign_in_page.click_login_button()

@When('sign_in: I click the forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_pwd_link()

@Then('sign_in: I am return to the home page')
def step_impl(context):
    context.sign_in_page.check_current_url()
