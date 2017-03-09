class RetrievalHandler():
    def handles():
        """returns a string indicating the type of report retrieval the subclass supports"""
        raise NotImplementedError('Subclass must implement abstract method')

    def retrieve(self):
        """returns a file path to the written file"""
        raise NotImplementedError('Subclass must implement abstract method')

    def get_outputpath(self):
        import os
        path = os.environ['TEMPFOLDERLOCATION'] + self.report['UUID'] + "\\"
        return path

    def get_filename(self):

        GroupNumber = self.report['GROUPNUMBER']
        filename = self.report['DISTRIBUTION']['SETTINGS']['FILENAME'] + '.' + \
                   self.report['RETRIEVAL']['SETTINGS']['FORMAT']
        origfilename = filename
        from PlaceholderHandler import PlaceholderHandler
        import PlaceholderHandlers

        for placeholder in PlaceholderHandler.__subclasses__():
            filename = placeholder(GroupNumber).process(filename)
        print('In Filename Generation,', origfilename, 'became', filename)
        return filename

    @staticmethod
    def factory(report):
        subclasses = RetrievalHandler.__subclasses__()
        available_retrievers = {}
        for subclass in subclasses:
            available_retrievers[subclass.handles()] = subclass
        retriever = available_retrievers[report['RETRIEVAL']['SOURCE'].upper()]

        return retriever(report)

    @staticmethod
    def document():
        doc = {}
        doc['HANDLERTYPE'] = 'RETRIEVER'
        doc['SOURCE'] = ''
        doc['SETTINGS'] = ''

        return doc
