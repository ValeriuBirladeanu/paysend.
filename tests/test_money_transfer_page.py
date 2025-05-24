import allure
import pytest
from pages.money_transfer_page import SendMoneyPage

@pytest.mark.screenshot
@allure.title("Verify that commission is correctly displayed and matches expected value")
@allure.description("This test compares the actual commission displayed on Paysend.com with the expected commission reference, based on random country and currency selection.")
def test_commission_display_and_value(page):
    transfer_money = SendMoneyPage(page)
    transfer_money.go_to()

    send_country, send_currency = transfer_money.select_random_country_and_currency_for_send()
    receive_country, receive_currency = transfer_money.select_random_country_and_currency_for_receive()

    print(f"[INFO] Send: {send_country} {send_currency}")
    print(f"[INFO] Receive: {receive_country} {receive_currency}")

    transfer_money.wait_after_selection()

    commission = transfer_money.get_commission()
    print(f"[DEBUG] Actual commission text: {commission}")
    expected_commission = transfer_money.get_expected_commission_for_selection()
    print(f"[DEBUG] Expected commission text: {expected_commission}")

    commission_amount, commission_currency = transfer_money.extract_fee(commission)
    expected_amount, expected_currency = transfer_money.extract_fee(expected_commission)

    print(f"Commission: {commission_amount} {commission_currency}")
    print(f"Expected: {expected_amount} {expected_currency}")

    assert commission_amount == expected_amount and commission_currency == expected_currency, \
        f"Expected '{expected_amount} {expected_currency}', got '{commission_amount} {commission_currency}'"