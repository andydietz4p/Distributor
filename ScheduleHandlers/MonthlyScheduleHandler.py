from ScheduleHandler import ScheduleHandler


class MonthlyScheduleHandler(ScheduleHandler):
    def __init__(self, report):
        self.report = report

    @staticmethod
    def handles():
        return "MONTHLY"

    def should_run(self):

        import time
        import calendar
        dayNumber = int(time.strftime('%d'))
        year = int(time.strftime('%Y'))
        month = int(time.strftime('%m'))
        dayrange = calendar.monthrange(year, month)
        if 'DAY' in self.report['SCHEDULE']['SETTINGS']:
            day = int(self.report['SCHEDULE']['SETTINGS']['DAY'])
        else:
            day = 0
        if dayNumber == day:
            return True
        elif 'relative' in self.report['SCHEDULE']['SETTINGS']:
            relative = self.report['SCHEDULE']['SETTINGS']['RELATIVE'].upper()
            if relative == 'LAST' and dayNumber == dayrange[1]:
                return True
            if relative == 'FIRST' and dayNumber == dayrange[0]:
                return True
            if relative == 'FIRSTWEEKDAY' and dayNumber == calendar.firstweekday() and dayNumber <= 3:
                return True
        else:
            return False
        return False

    @staticmethod
    def document():
        doc = ScheduleHandler.document()
        doc['SCHEDULE'] = 'MONTHLY'
        doc['SETTINGS'] = {
            'RELATIVE': 'var_oneof:First>First Day of Month|Last>Last Day of Month|FirstWeekday>First Weekday of Month',
            'DAY': 'var_number'}
        return doc
