from pages.paysend_page import PaysendPage



def test_commission_display_and_value(page, run):
    paysend = PaysendPage(page)
    paysend.go_to()
    paysend.select_random_country_and_currency_for_send()
    paysend.select_random_country_and_currency_for_receive()

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