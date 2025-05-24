

class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_after_selection(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)