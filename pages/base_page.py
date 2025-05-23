

class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_element(self, selector: str, timeout: int = 5000):
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)

    def wait_after_selection(self):
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(300)