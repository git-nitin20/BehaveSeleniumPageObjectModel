from behave import *

from features.pages.HomePage import HomePage
from utilities import EmailWithTimeStampGenerator


@given(u'I navigate to Register Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.select_register_option()


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        new_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])


@when(u'I select Privacy Policy option')
def step_impl(context):
    context.register_page.select_privacy_policy()


@when(u'I click on Continue button')
def step_impl(context):
    context.account_success_page = context.register_page.click_on_continue_button()


@then(u'Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert context.account_success_page.display_status_of_account_created_heading(expected_text)


@when(u'I enter below details into all fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        new_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
        context.register_page.select_yes_newsletter_option()


@when(u'I enter below details into all fields except email field')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
        context.register_page.select_yes_newsletter_option()


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    context.register_page.enter_email("amotooriApril202328190133@gmail.com")


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    expected_warning = "Warning: E-Mail Address is already registered!"
    assert context.register_page.display_status_of_duplicate_email_warning(expected_warning)


@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_password_confirm("")


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    expected_privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_first_name_warning = "First Name must be between 1 and 32 characters!"
    expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"
    assert context.register_page.display_status_of_all_warning_messages(expected_privacy_policy_warning,
                                                                        expected_first_name_warning,
                                                                        expected_last_name_warning,
                                                                        expected_email_warning,
                                                                        expected_telephone_warning,
                                                                        expected_password_warning,
                                                                        )
