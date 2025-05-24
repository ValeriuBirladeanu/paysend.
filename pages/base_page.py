import re

class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_after_selection(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)

    def extract_float_from_text(self, selector: str) -> float:
        text = self.page.locator(selector).inner_text()
        match = re.search(r'(\d+(?:\.\d+)?)', text)
        return float(match.group(1)) if match else 0.0