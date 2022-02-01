class FileDownload:
    textarea = "textarea"
    generate_file_btn = "button:has-text(\"Generate File\")"
    download_file_link = "#link-to-download"

    @staticmethod
    def enter_text(page, val):
        page.fill(FileDownload.textarea, val)
        ## IMP. Page fill not enabling the button
        page.keyboard.press(" ")

    @staticmethod
    def generate_download_link(page):
        page.click(FileDownload.generate_file_btn)

    @staticmethod
    def download_file(page, save_as_file_name):
        with page.expect_download() as download_info:
            page.click(FileDownload.download_file_link)

        download = download_info.value
        filepath = str(download.path())
        save_file_path = filepath.split('download-dir')[0]+"download-dir/"+save_as_file_name
        download.save_as(save_file_path)
        return save_file_path
