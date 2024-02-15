
class PageResponse:

    def __init__(self):
        self.page_number = 0
        self.page_size = 0
        self.total_count = 0
        self.total_page = 0
        self.items = []


def build_page_response(items, page_number, page_size, total_count):
    page_response = PageResponse()
    page_response.page_number = page_number
    page_response.page_size = page_size
    page_response.total_count = total_count
    page_response.total_page = total_count // page_size + (1 if total_count % page_size > 0 else 0)
    page_response.items = items

    return page_response
