class TableSortAndSearchDemo:
    entriesDropDown = "select[name=\"example_length\"]"
    sortColumn = "text=COLUMN"
    searchBox = "input[type=\"search\"]"

    @staticmethod
    def select_table_entries(page, value):
        page.select_option(TableSortAndSearchDemo.entriesDropDown, value)

    @staticmethod
    def sort_table_by_column(page, column_name):
        page.click(TableSortAndSearchDemo.sortColumn.replace("COLUMN", column_name))

    @staticmethod
    def search_table(page, value):
        page.fill(TableSortAndSearchDemo.searchBox, value)

    @staticmethod
    def get_sorted_data_list(page):
        data_list_values = []
        element_list = page.query_selector_all("//td[@class='sorting_1']")
        for element in element_list:
            data = element.text_content()
            data_list_values.append(data)

        return data_list_values
