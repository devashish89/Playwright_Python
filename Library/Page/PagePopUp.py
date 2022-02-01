class PagePopUp:
    twitter_popup_btn = "text=Follow On Twitter"
    twitter_sign_up = "text=Sign up for Twitter"
    main_page_demo_home = "text=Demo Home"

    @staticmethod
    def work_within_popup_main_page_also(page):
        with page.expect_popup() as popup_info:
            page.click(PagePopUp.twitter_popup_btn)
        popup_page = popup_info.value

        popup_page.click(PagePopUp.twitter_sign_up)
        page.click(PagePopUp.main_page_demo_home)
