from playwright.sync_api import sync_playwright
import os
import configparser

# --- IMP !!! - classname should be same as filename --- #


class PlaywrightCore:
    browser = "chromium"
    pwSync = None
    context = None
    page = None
    page1 = None

    @staticmethod
    def launch_browser():
        config = configparser.RawConfigParser()
        config.read(os.getcwd()+"/config.txt")
        browser_name = config.get("Browser", "browser_name")
        record_video = eval(config.get("Browser", "record_video"))
        head_less = eval(config.get("Browser", "head_less"))
        slow_mo = int(config.get("Browser", "slow_mo"))
        print("Opening Browser: " + browser_name)
        PlaywrightCore.pwSync = sync_playwright().start()

        if browser_name.lower() == 'chromium':
            PlaywrightCore.browser = PlaywrightCore.pwSync.chromium.launch(headless=head_less, slow_mo=slow_mo, downloads_path='download-dir')

        elif browser_name.lower() == 'firefox':
            PlaywrightCore.browser = PlaywrightCore.pwSync.firefox.launch(headless=head_less, slow_mo=slow_mo, downloads_path='download-dir')

        elif browser_name.lower() == 'webkit':
            PlaywrightCore.browser = PlaywrightCore.pwSync.webkit.launch(headless=head_less, slow_mo=slow_mo, downloads_path='download-dir')

        if record_video:
            PlaywrightCore.context = PlaywrightCore.browser.new_context(
                viewport={'width': 1280, 'height': 1024},
                record_video_dir="videos/",
                record_video_size={'width': 640, 'height': 480},
                accept_downloads=True
            )

        else:
            PlaywrightCore.context = PlaywrightCore.browser.new_context()

    @staticmethod
    def close_browser():
        PlaywrightCore.context.close()
        PlaywrightCore.browser.close()
        PlaywrightCore.pwSync.stop()

    @staticmethod
    def open_application():
        print("Opening website .........")
        PlaywrightCore.page = PlaywrightCore.context.new_page()
        PlaywrightCore.page.goto("http://demo.seleniumeasy.com/")
        if PlaywrightCore.page.query_selector("text=No, thanks!"):
            PlaywrightCore.page.click("text=No, thanks!")

    @staticmethod
    def open_application_herokuapp():
        print("Opening https://the-internet.herokuapp.com/")
        PlaywrightCore.page1 = PlaywrightCore.context.new_page()
        PlaywrightCore.page1.goto("https://the-internet.herokuapp.com/")




    @staticmethod
    def close_application():
        PlaywrightCore.page.close()

    @staticmethod
    def close_application_herokuapp():
        PlaywrightCore.page1.close()

    @staticmethod
    def get_page_object():
        return PlaywrightCore.page

    @staticmethod
    def get_herokuapp_page():
        return PlaywrightCore.page1

    @staticmethod
    def take_screenshot():
        PlaywrightCore.page.screenshot(path="form.png")


