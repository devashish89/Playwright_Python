class IframeHandling:
    edit_locator = "button[role=\"menuitem\"]:has-text(\"Edit\")"
    select_all_locator = "text=Select allCtrl+A"
    cut_locator = "text=Cut"
    iframe1_id = "mce_0_ifr"
    iframe1_para_locator = "p"
    bold_text_locator = "[aria-label=\"Bold\"]"

    @staticmethod
    def navigate_to_iframe_menu(page):
        # Go to https://the-internet.herokuapp.com/iframe
        page.goto("https://the-internet.herokuapp.com/iframe")

    @staticmethod
    def select_all(page):
        page.click(IframeHandling.edit_locator)
        page.click(IframeHandling.select_all_locator)

    @staticmethod
    def cut_text(page):
        page.click(IframeHandling.edit_locator)
        page.click(IframeHandling.cut_locator)

    @staticmethod
    def bold_text(page):
        page.click(IframeHandling.bold_text_locator)

    @staticmethod
    def enter_text_iframe(page, text):
        locator = page.frame(IframeHandling.iframe1_id).click(IframeHandling.iframe1_para_locator)
        page.keyboard.insert_text(text)

