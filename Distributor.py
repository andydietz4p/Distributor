from pprint import pprint

import json
from tasks import ProcessReport
import uuid
import placeholder
import settings

def to_upper(dictionary):
    def try_iterate(k):
        return upper_by_level(k) if isinstance(k, dict) else k

    def try_upper(k):
        return k.upper() if isinstance(k, str) else k

    def upper_by_level(data):
        return dict((try_upper(k), try_iterate(v)) for k, v in data.items())

    return upper_by_level(dictionary)


def main():
    reportRepository = settings.getReportRepository()
    reports = reportRepository.getAllReports()
    for report in reports:
        report['uuid'] = str(uuid.uuid4())
        report['distribution'] = json.loads(report['distribution'])
        report['schedule'] = json.loads(report['schedule'])
        report['retrieval'] = json.loads(report['retrieval'])

        if report['parameters'] != '':
            report['parameters'] = json.loads(report['parameters'])

        # report.update({k.upper(): v for k, v in report.items()})

        finalreport = to_upper(report)

        # ProcessReport.delay(finalreport)
        ProcessReport(finalreport)


if __name__ == "__main__":
    main()
