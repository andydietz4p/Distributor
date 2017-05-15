from PlaceholderHandler import PlaceholderHandler


class PrevYearMonthPlaceholderHandler(PlaceholderHandler):
    def process(self, string):
        import datetime
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        yearmonth = lastMonth.strftime("%Y-%m")
        return string.replace('<PrevYearMonth>', yearmonth)

    @staticmethod
    def document():
        doc = {}
        doc['PLACEHOLDER'] = 'PREVYEARMONTH'
        doc['DESCRIPTION'] = 'Replaces <PrevYearMonth> with the previous 4 digit year and 2 digit month i.e. 2017-05'
        return doc
