import allure
import pytest
from pages.paysend_page import PaysendPage

@pytest.mark.screenshot
@allure.title("Verify that commission is correctly displayed and matches expected value")
@allure.description("This test compares the actual commission displayed on Paysend.com with the expected commission reference, based on random country and currency selection.")
def test_commission_display_and_value(page):
    paysend = PaysendPage(page)
    paysend.go_to()

    send_country, send_currency = paysend.select_random_country_and_currency_for_send()
    receive_country, receive_currency = paysend.select_random_country_and_currency_for_receive()

    print(f"[INFO] Send: {send_country} {send_currency}")
    print(f"[INFO] Receive: {receive_country} {receive_currency}")

    paysend.wait_after_selection()

    commission = paysend.get_commission()
    print(f"[DEBUG] Actual commission text: {commission}")
    expected_commission = paysend.get_expected_commission_for_selection()
    print(f"[DEBUG] Expected commission text: {expected_commission}")

    commission_amount, commission_currency = paysend.extract_fee(commission)
    expected_amount, expected_currency = paysend.extract_fee(expected_commission)

    print(f"Commission: {commission_amount} {commission_currency}")
    print(f"Expected: {expected_amount} {expected_currency}")

    assert commission_amount == expected_amount and commission_currency == expected_currency, \
        f"Expected '{expected_amount} {expected_currency}', got '{commission_amount} {commission_currency}'"