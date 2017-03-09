from PlaceholderHandler import PlaceholderHandler


class YearPlaceholderHandler(PlaceholderHandler):
    def process(self, string):
        import time
        return string.replace('<Year>', time.strftime('%Y'))

    @staticmethod
    def document():
        doc = {}
        doc['PLACEHOLDER'] = 'Year'
        doc['DESCRIPTION'] = 'Replaces <Year> with the current YYYY formatted year'
        return doc
