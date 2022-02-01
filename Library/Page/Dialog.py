class Dialog:
    alert_box_btn = "text=Click me!"
    confirm_box_btn = ":nth-match(:text(\"Click me!\"), 2)"
    prompt_box_btn = "text=Click for Prompt Box"
    prompt_message = None

    @staticmethod
    def init_dialog_accept(page):
        page.on("dialog", Dialog.handle_dialog)

    @staticmethod
    def handle_dialog(dialog):
        print("dialog type: ", dialog.type)
        print("dialog message: ", dialog.message)
        dialog.accept(Dialog.prompt_message)

    @staticmethod
    def set_prompt_message(message):
        Dialog.prompt_message = message

    @staticmethod
    def click_alert_box_btn(page):
        page.click(Dialog.alert_box_btn)

    @staticmethod
    def click_confirm_box_btn(page):
        page.click(Dialog.confirm_box_btn)

    @staticmethod
    def click_prompt_box_btn(page):
        page.click(Dialog.prompt_box_btn)