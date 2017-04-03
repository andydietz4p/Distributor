from DistributionHandler import DistributionHandler


class FileDistributionHandler(DistributionHandler):
    def __init__(self, report):
        self.report = report

    @staticmethod
    def handles():
        return "FILE"

    def clean_folder(self, folderpath):
        import os
        import shutil
        for i in os.walk(folderpath, topdown=False):
            if (i[2] is not None):
                shutil.rmtree(i[0])
                continue
            os.rmdir(i[0])
        return

    def distribute(self, tempfile):
        import os
        import ntpath
        import shutil

        originalfilepath = ntpath.dirname(tempfile)
        newfilepath = self.report['DISTRIBUTION']['SETTINGS']['LOCATION'] + ntpath.basename(tempfile)
        if os.path.exists(newfilepath):
            os.remove(newfilepath)
        shutil.copy2(tempfile, newfilepath)
        self.clean_folder(originalfilepath)

        if os.path.exists(originalfilepath):
            shutil.rmtree(originalfilepath, ignore_errors=True)
        return True

    @staticmethod
    def document():
        doc = DistributionHandler.document()
        doc['METHOD'] = 'SSRS'
        doc['SETTINGS'] = {'LOCATION': 'var_string'}
        return doc
