from DistributionHandler import DistributionHandler


class FileDistributionHandler(DistributionHandler):
    def __init__(self, report):
        self.report = report

    @staticmethod
    def handles():
        return "FILE"

    def distribute(self, tempfile):
        import os
        import ntpath

        newfilepath = self.report['DISTRIBUTION']['SETTINGS']['LOCATION'] + ntpath.basename(tempfile)
        if os.path.exists(newfilepath):
            os.remove(newfilepath)
        os.rename(tempfile, newfilepath)
        if os.path.exists(ntpath.dirname(tempfile)):
            os.rmdir(ntpath.dirname(tempfile))
        return True

    @staticmethod
    def document():
        doc = DistributionHandler.document()
        doc['METHOD'] = 'SSRS'
        doc['SETTINGS'] = {'LOCATION': 'var_string'}
        return doc
