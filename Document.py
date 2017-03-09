from pprint import pprint
import json


def document_retrievers():
    from RetrievalHandler import RetrievalHandler
    import RetrievalHandlers

    docs = []
    for handler in RetrievalHandler.__subclasses__():
        try:
            docs.append(handler.document())

        except AttributeError:
            pass
    return docs


def document_distributors():
    from DistributionHandler import DistributionHandler
    import DistributionHandlers

    docs = []
    for handler in DistributionHandler.__subclasses__():
        try:
            docs.append(handler.document())

        except AttributeError:
            pass
    return docs


def document_schedulers():
    from ScheduleHandler import ScheduleHandler
    import ScheduleHandlers

    docs = []
    for handler in ScheduleHandler.__subclasses__():
        try:
            docs.append(handler.document())

        except AttributeError:
            pass

    return docs


outputdocs = document_distributors() + document_schedulers() + document_retrievers()
print(json.dumps(outputdocs))
