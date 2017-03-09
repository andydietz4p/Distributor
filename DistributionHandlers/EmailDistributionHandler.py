from DistributionHandler import DistributionHandler


class EmailDistributionHandler(DistributionHandler):
    def __init__(self, report):
        self.report = report

    @staticmethod
    def handles():
        return "EMAIL"

    def distribute(self, tempfile):
        import ntpath
        import smtplib
        import os
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication
        msg = MIMEMultipart()
        msg['Subject'] = "Regional Care Automated Reports <secure>"
        msg['From'] = 'reports@regionalcare.com'
        msg['To'] = self.report['DISTRIBUTION']['SETTINGS']['ADDRESS']
        filename = ntpath.basename(tempfile)
        with open(tempfile, 'rb') as fp:
            attachment = MIMEApplication(fp.read())
            attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)
            msg.attach(attachment)
        s = smtplib.SMTP('rciv-echo.regionalcare.com')
        s.send_message(msg)
        s.quit()
        if os.path.exists(tempfile):
            os.remove(tempfile)
        if os.path.exists(ntpath.dirname(tempfile)):
            os.rmdir(ntpath.dirname(tempfile))
        return True

    @staticmethod
    def document():
        doc = DistributionHandler.document()
        doc['METHOD'] = 'EMAIL'
        doc['SETTINGS'] = {'ADDRESS': 'var_email'}
        return doc
