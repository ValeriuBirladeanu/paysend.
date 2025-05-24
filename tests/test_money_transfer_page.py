import allure
import pytest
from pages.money_transfer_page import SendMoneyPage

@pytest.mark.screenshot
@allure.title("Verify that commission is correctly displayed and matches expected value")
@allure.description("""
This test verifies the correctness of the displayed commission on the Paysend website. 
It performs a random selection of sending and receiving countries (with their respective currencies),
retrieves the actual commission shown on the UI, and compares it against the expected commission 
reference text. The extracted numerical values and currencies are validated for exact match.
""")
def test_commission_display_and_value(page):
    transfer_money = SendMoneyPage(page)
    transfer_money.go_to()

    send_country, send_currency = transfer_money.select_random_country_and_currency_for_send()
    receive_country, receive_currency = transfer_money.select_random_country_and_currency_for_receive()

    print(f"[INFO] Send: {send_country} {send_currency}")
    print(f"[INFO] Receive: {receive_country} {receive_currency}")

    transfer_money.wait_after_selection()

    commission = transfer_money.get_commission_text()
    print(f"[DEBUG] Actual commission text: {commission}")
    expected_commission = transfer_money.get_expected_commission_for_selection()
    print(f"[DEBUG] Expected commission text: {expected_commission}")

    commission_amount, commission_currency = transfer_money.extract_fee(commission)
    expected_amount, expected_currency = transfer_money.extract_fee(expected_commission)

    print(f"Commission: {commission_amount} {commission_currency}")
    print(f"Expected: {expected_amount} {expected_currency}")

    assert commission_amount == expected_amount and commission_currency == expected_currency, \
        f"Expected '{expected_amount} {expected_currency}', got '{commission_amount} {commission_currency}'"

@pytest.mark.screenshot
@allure.title("Check that receive amount is correctly calculated based on commission and exchange rate")
@allure.description("""
This test verifies that the receive amount shown to the user is calculated correctly.
It does this by:
- Selecting random SEND and RECEIVE countries and currencies
- Fetching the send amount input by default
- Getting the commission and current exchange rate
- Calculating the expected receive amount based on the formula:
  (send_amount - commission) * exchange_rate
- Asserting that the displayed receive amount matches the expected value
""")
def test_exchange_rate_updates_correctly_for_selected_currencies(page):
    transfer_money = SendMoneyPage(page)
    transfer_money.go_to()

    transfer_money.select_random_country_and_currency_for_send()
    transfer_money.select_random_country_and_currency_for_receive()

    send_amount = transfer_money.get_send_amount()
    print(f"[INFO] Send amount: {send_amount}")

    commission = transfer_money.get_commission_float()
    print(f"[INFO] Commission: {commission}")

    exchange_rate = transfer_money.get_exchange_rate()
    print(f"[INFO] Exchange rate: {exchange_rate}")

    receive_amount = transfer_money.get_receive_amount()
    print(f"[INFO] Actual receive amount: {receive_amount}")

    expected_receive = transfer_money.calculate_expected_receive(send_amount, commission, exchange_rate)
    print(f"[INFO] Expected receive amount: {expected_receive}")

    assert receive_amount == expected_receive,  f"Expected {expected_receive}, but got {receive_amount}"