from ScheduleHandler import ScheduleHandler


class YearlyScheduleHandler(ScheduleHandler):
    def __init__(self, report):
        self.report = report

    @staticmethod
    def handles():
        return "YEARLY"

    def should_run(self):
        import time
        import datetime
        dayNumber = int(time.strftime('%j'))
        day = self.report['SCHEDULE']['SETTINGS']['DAY'] or None
        month = self.report['SCHEDULE']['SETTINGS']['MONTH'] or None
        year = int(time.strftime('%Y'))
        scheduleddayofyear = int(time.strftime('%j', datetime.date(year, month, day).timetuple()))
        return dayNumber == scheduleddayofyear

    @staticmethod
    def document():
        doc = ScheduleHandler.document()
        doc['SCHEDULE'] = 'YEARLY'
        doc['SETTINGS'] = {'DAY': 'var_number', 'MONTH': 'var_number'}
        return doc
