from PlaceholderHandler import PlaceholderHandler


class MonthPlaceholderHandler(PlaceholderHandler):
    def process(self, string):
        import time
        return string.replace('<Month>', time.strftime('%Y'))

    @staticmethod
    def document():
        doc = {}
        doc['PLACEHOLDER'] = 'Month'
        doc['DESCRIPTION'] = 'Replaces <Month> with the current 2 digit formatted month'
        return doc
