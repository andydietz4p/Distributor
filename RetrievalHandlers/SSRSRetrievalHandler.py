from RetrievalHandler import RetrievalHandler
from pprint import pprint


class SSRSRetrievalHandler(RetrievalHandler):
    def __init__(self, report):
        self.report = report

    @staticmethod
    def handles():
        return 'SSRS'

    @staticmethod
    def document():
        doc = {}
        doc['SOURCE'] = 'SSRS'
        doc['SETTINGS'] = {'FORMAT': 'var_oneof:PDF|XLS|CSV', 'REPORTPATH': 'var_string',
                           'PARAMETERS': 'var_paramstring'}
        return doc

    def retrieve(self):

        import urllib
        import requests
        from requests_ntlm import HttpNtlmAuth

        import os

        url = os.environ['SSRSURL'] + "?"
        # reportpath = "/Reporting/Monthly+Reporting/Automated/Aggregate+Minimum+Forecast"
        reportpath = self.report['RETRIEVAL']['SETTINGS']['REPORTPATH']
        formatstring = "&rs:Format=" + self.report['RETRIEVAL']['SETTINGS']['FORMAT']
        if 'PARAMETERS' in self.report['RETRIEVAL']['SETTINGS']:
            parameters = self.report['RETRIEVAL']['SETTINGS']['PARAMETERS']
        else:
            parameters = {}
        parameters['GroupNumber'] = self.report['GROUPNUMBER']

        parameters = urllib.parse.urlencode(parameters, True)

        compiledurl = url + reportpath + formatstring + "&" + parameters

        r = requests.get(compiledurl, auth=HttpNtlmAuth(os.environ['SSRSUSERNAME'], os.environ['SSRSPASSWORD']))
        outpath = self.get_outputpath()
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        filename = self.get_filename()

        outputfile = outpath + self.report['GROUPNUMBER'] + '-' + filename
        with open(outputfile, 'wb') as f:
            for block in r.iter_content(1024):
                f.write(block)
            f.close()

        return outputfile

