from ScheduleHandler import ScheduleHandler


class DailyScheduleHandler(ScheduleHandler):
    def __init__(self, report):
        self.report = report

    @staticmethod
    def handles():
        return "DAILY"

    def should_run(self):
        return True

    @staticmethod
    def document():
        doc = ScheduleHandler.document()
        doc['SCHEDULE'] = 'DAILY'
        doc['SETTINGS'] = {}
        return doc
