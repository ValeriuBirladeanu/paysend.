import random
import re
import allure
from pages.base_page import BasePage
from playwright.sync_api import expect


class PaysendPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://paysend.com"

        self.from_country_dropdown = 'a[data-testid="amount-label-from"]'
        self.to_country_dropdown = 'a[data-testid="amount-label-to"]'
        self.dropdown_selector = '//a[@class="styles__DropdownListItem-sc-16fw3cn-6 hA-dnua"]'
        self.commission_selector = 'div[data-testid="fee-span-fee-info"] span.PromoText__TextSpan-sc-oncfto-5'
        self.commission_reference_selector = 'p[class="title3"]'

    @allure.step("Navigate to Paysend homepage")
    def go_to(self):
        self.page.goto(self.url)

    @allure.step("Select a random country and currency")
    def select_random_option_with_currency(self, button_selector, option_selector):
        self.page.locator(button_selector).click()
        options = self.page.locator(option_selector)
        all_options = options.all_text_contents()

        if not all_options:
            raise ValueError(f"No country options found for selector: {option_selector}")

        selected_index = random.randint(0, len(all_options) - 1)
        selected_option = all_options[selected_index]
        print(f"[INFO] Selected country: {selected_option}")
        options.nth(selected_index).click()

        currency_options = self.page.locator(option_selector)
        if currency_options.count() > 0:
            all_currencies = currency_options.all_text_contents()
            selected_currency_index = random.randint(0, len(all_currencies) - 1)
            selected_currency = all_currencies[selected_currency_index]
            currency_options.nth(selected_currency_index).click()
        else:
            selected_currency = None

        return selected_option, selected_currency

    @allure.step("Select random SEND country and currency")
    def select_random_country_and_currency_for_send(self):
        return self.select_random_option_with_currency(self.from_country_dropdown , self.dropdown_selector)

    @allure.step("Select random RECEIVE country and currency")
    def select_random_country_and_currency_for_receive(self):
        return self.select_random_option_with_currency(self.to_country_dropdown , self.dropdown_selector)

    @allure.step("Get displayed commission")
    def get_commission(self):
        element = self.page.locator(self.commission_selector)
        expect(element).to_be_visible()
        return element.inner_text().strip()

    @allure.step("Get expected commission reference")
    def get_expected_commission_for_selection(self):
        element = self.page.locator(self.commission_reference_selector)
        expect(element).to_be_visible()
        return element.inner_text().strip()

    @allure.step("Extract fee from text: {text}")
    def extract_fee(self, text):
        euro_symbol_match = re.search(r'[€]\s?(\d+(?:\.\d+)?)', text)
        code_match = re.search(r'(\d+(?:\.\d+)?)\s*([A-Z]{3})', text)

        if code_match:
            amount = float(code_match.group(1))
            currency = code_match.group(2)
            return amount, currency
        elif euro_symbol_match:
            amount = float(euro_symbol_match.group(1))
            return amount, 'EUR'
        else:
            print(f"[ERROR] Could not extract fee from text: {text}")
            return None, None