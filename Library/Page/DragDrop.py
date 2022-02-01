class DragDrop:
    drag_item_locator = "text=Draggable NO"
    drop_location = "#mydropzone"
    dropped_items = "//div[@id='droppedlist']/span[contains(text(),'Draggable')]"

    @staticmethod
    def drag_item(page, element_number):
        drag_item = DragDrop.drag_item_locator.replace("NO", element_number)
        page.drag_and_drop(drag_item, DragDrop.drop_location)

    @staticmethod
    def get_dropped_items(page):
        dropped_list_values = []
        element_list = page.query_selector_all(DragDrop.dropped_items)
        for element in element_list:
            data = element.text_content()
            dropped_list_values.append(data)

        return dropped_list_values