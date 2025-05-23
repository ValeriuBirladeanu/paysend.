

class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_element(self, selector: str, timeout: int = 5000):
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)

    def get_text(self, selector: str, wait_before: bool = False) -> str:
        self.wait_for_element(selector)
        if wait_before:
            self.page.wait_for_timeout(1000)
        return self.page.locator(selector).inner_text().strip()