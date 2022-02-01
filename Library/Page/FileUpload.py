class FileUpload:
    file_upload_menu_item = "text=File Upload"
    file_upload_locator = "input[name=\"file\"]"
    file_upload_btn = "input:has-text(\"Upload\")"
    file_uploaded_validation_locator = "text=File Uploaded!"
    filepath = None

    @staticmethod
    def navigate_file_upload_page(page):
        page.click(FileUpload.file_upload_menu_item)

    @staticmethod
    def silent_file_upload(page, filepath):
        page.set_input_files(FileUpload.file_upload_locator, filepath)
        page.click(FileUpload.file_upload_btn)

    @staticmethod
    def interactive_file_upload(page, filepath):
        with page.expect_file_chooser() as fc_info:
            page.click(FileUpload.file_upload_locator)
        file_chooser = fc_info.value
        file_chooser.set_files(filepath)
        page.click(FileUpload.file_upload_btn)

    @staticmethod
    def init_listener_file_upload(page):
        page.on("filechooser", FileUpload.upload_listener)

    @staticmethod
    def upload_listener(filechooser):
        filechooser.set_files(FileUpload.filepath)

    @staticmethod
    def click_file_upload(page):
        page.click(FileUpload.file_upload_locator)
        page.click(FileUpload.file_upload_btn)

    @staticmethod
    def set_filepath(filepath):
        FileUpload.filepath = filepath

    @staticmethod
    def check_file_uploaded(page):
        if page.query_selector(FileUpload.file_uploaded_validation_locator):
            return True
        else:
            return False

