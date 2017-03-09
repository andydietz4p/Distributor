from PlaceholderHandler import PlaceholderHandler


class DatePlaceholderHandler(PlaceholderHandler):
    def process(self, string):
        import time
        return string.replace('<Date>', time.strftime('%Y-%m-%d'))

    @staticmethod
    def document():
        doc = {}
        doc['PLACEHOLDER'] = 'Date'
        doc['DESCRIPTION'] = 'Replaces <Date> with a YYYY-MM-DD formatted date'
        return doc
