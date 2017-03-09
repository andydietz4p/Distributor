from ScheduleHandler import ScheduleHandler


class WeeklyScheduleHandler(ScheduleHandler):
    def __init__(self, report):
        self.report = report

    @staticmethod
    def handles():
        return "WEEKLY"

    def should_run(self, report):
        import time
        dayNumber = int(time.strftime('%w'))
        days = self.report['SCHEDULE']['SETTINGS']['DAYS']
        if dayNumber in days:
            return True

    @staticmethod
    def document():
        doc = ScheduleHandler.document()
        doc['SCHEDULE'] = 'WEEKLY'
        doc['SETTINGS'] = {'DAYS': 'var_listof:0>Sunday|1>Monday|2>Tuesday|3>Wednesday|4>Thursday|5>Friday|6>Saturday'}
        return doc
