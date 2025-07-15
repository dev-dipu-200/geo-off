class Paginator:
    def __init__(self, page: int = 1, page_size: int = 10):
        self.page = page
        self.page_size = page_size

    def paginate(self, items: list):
        start_index = (self.page - 1) * self.page_size
        end_index = start_index + self.page_size
        return items[start_index:end_index]

    def total_pages(self, total_items: int):
        return (total_items + self.page_size - 1) // self.page_size

    def has_next(self, total_items: int):
        return self.page < self.total_pages(total_items)

    def has_previous(self):
        return self.page > 1

    def next_page(self, total_items: int):
        if self.has_next(total_items):
            return self.page + 1
        return self.page

    def previous_page(self):
        if self.has_previous():
            return self.page - 1
        return self.page

    def to_dict(self, items: list):
        total_items = len(items)
        return {
            "items": self.paginate(items),
            "total_pages": self.total_pages(total_items),
            "current_page": self.page,
            "total_items": total_items,
            "items_per_page": self.page_size,
            "has_next": self.has_next(total_items),
            "has_previous": self.has_previous(),
            "next_page": self.next_page(total_items),
            "previous_page": self.previous_page()
        }
