from math import ceil


class Pagination(object):
    """Pagination"""

    def __init__(self, page, per_page, total_count, list_in):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count
        self.list_in = list_in

    @property
    def pages(self):
        # Return
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        # Return
        return self.page > 1

    @property
    def has_next(self):
        # Return
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=3, right_edge=2):
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

    @property
    def rows(self):
        list_start = self.per_page * (self.page - 1)
        end_list = list_start + self.per_page
        list_out = [i for i in self.list_in[list_start:end_list]]
        # Return
        return list_out
