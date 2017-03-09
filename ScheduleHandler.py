class ScheduleHandler():
    def handles(self):
        raise NotImplementedError("Subclass must implement this method")

    def should_run(self):
        raise NotImplementedError("Subclass must implement this method")

    @staticmethod
    def factory(report):
        subclasses = ScheduleHandler.__subclasses__()
        available_schedules = {}
        for subclass in subclasses:
            available_schedules[subclass.handles()] = subclass
        handler = available_schedules[report['SCHEDULE']['SCHEDULE'].upper()]
        return handler(report)

    @staticmethod
    def document():
        doc = {}
        doc['HANDLERTYPE'] = 'SCHEDULER'
        doc['SCHEDULE'] = ''
        doc['SETTINGS'] = ''
        return doc
