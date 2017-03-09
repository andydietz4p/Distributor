class DistributionHandler():
    def handles(self):
        raise NotImplementedError("Subclass must implement this method")

    def distribute(self, tempfile, report):
        raise NotImplementedError("Subclass must implement this method")

    @staticmethod
    def factory(report):
        subclasses = DistributionHandler.__subclasses__()
        available_distributors = {}
        for subclass in subclasses:
            available_distributors[subclass.handles()] = subclass
        distributor = available_distributors[report['DISTRIBUTION']['METHOD'].upper()]
        return distributor(report)

    @staticmethod
    def document():
        doc = {}
        doc['HANDLERTYPE'] = 'DISTRIBUTION'
        doc['METHOD'] = ''
        doc['SETTINGS'] = ''

        return doc
