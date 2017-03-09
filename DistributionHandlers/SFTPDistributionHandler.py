from DistributionHandler import DistributionHandler


class SFTPDistributionHandler(DistributionHandler):
    def __init__(self, report):
        self.report = report

    @staticmethod
    def handles():
        return "SFTP"

    def distribute(self, tempfile):
        import pysftp
        import ntpath
        import os
        hostname = self.report['DISTRIBUTION']['SETTINGS']['SERVER']
        username = self.report['DISTRIBUTION']['SETTINGS']['USERNAME']
        password = self.report['DISTRIBUTION']['SETTINGS']['PASSWORD']
        location = self.report['DISTRIBUTION']['SETTINGS']['UPLOADPATH']
        hostkey = self.report['DISTRIBUTION']['SETTINGS']['HOSTKEY']
        filename = ntpath.basename(tempfile)
        cnopts = pysftp.CnOpts()
        # cnopts.hostkeys = None
        with pysftp.Connection(hostname, username=username, password=password, cnopts=cnopts) as sftp:
            sftp.cd(location)
            sftp.put(tempfile, remotepath=location + filename, preserve_mtime=False, confirm=True)
        if os.path.exists(tempfile):
            os.remove(tempfile)
        if os.path.exists(ntpath.dirname(tempfile)):
            os.rmdir(ntpath.dirname(tempfile))

        return true

    @staticmethod
    def document():
        doc = DistributionHandler.document()
        doc['METHOD'] = 'SFTP'
        doc['SETTINGS'] = {'SERVER': 'var_string', 'USERNAME': 'var_string', 'PASSWORD': 'var_string',
                           'UPLOADPATH': 'var_string', 'HOSTKEY': 'var_string'}
        return doc
