import allure
from pages.paysend_page import PaysendPage

@allure.title("Verify that commission is correctly displayed and matches expected value")
@allure.description("This test compares the actual commission displayed on Paysend.com with the expected commission reference, based on random country and currency selection.")
def test_commission_display_and_value(page):
    paysend = PaysendPage(page)

    with allure.step("Navigate to Paysend homepage"):
        paysend.go_to()

    with allure.step("Select random SEND country and currency"):
        paysend.select_random_country_and_currency_for_send()

    with allure.step("Select random RECEIVE country and currency"):
        paysend.select_random_country_and_currency_for_receive()

    with allure.step("Retrieve actual and expected commission values"):
        commission = paysend.get_commission()
        expected_commission = paysend.get_expected_commission_for_selection()

    with allure.step("Extract amount and currency from both values"):
        commission_amount, commission_currency = paysend.extract_fee(commission)
        expected_amount, expected_currency = paysend.extract_fee(expected_commission)

        allure.attach(f"{commission_amount} {commission_currency}", name="Actual Fee", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"{expected_amount} {expected_currency}", name="Expected Fee", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Assert that commission matches expected value"):
        assert commission_amount == expected_amount and commission_currency == expected_currency, \
            f"Expected '{expected_amount} {expected_currency}', got '{commission_amount} {commission_currency}'"