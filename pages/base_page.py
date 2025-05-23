

class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_element(self, selector: str, timeout: int = 5000):
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)