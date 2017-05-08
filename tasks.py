# from celery import Celery
from queueconfig import huey

from pprint import pprint
import json
import settings
import os


from DistributionHandler import DistributionHandler
import DistributionHandlers

from ScheduleHandler import ScheduleHandler
import ScheduleHandlers

from RetrievalHandler import RetrievalHandler
import RetrievalHandlers

from PlaceholderHandler import PlaceholderHandler
import PlaceholderHandlers


#app = Celery('tasks', broker='redis://localhost')



@huey.task()
def ProcessReport(report):
    scheduler = ScheduleHandler.factory(report)
    if not scheduler.should_run():
        print("Report will not run due to scheduler: ", scheduler.handles())
        return
    retriever = RetrievalHandler.factory(report)
    file = retriever.retrieve()
    distributor = DistributionHandler.factory(report)
    distributor.distribute(file)
