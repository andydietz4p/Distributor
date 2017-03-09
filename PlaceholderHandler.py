class PlaceholderHandler():
    def __init__(self, GroupNumber):
        self.GroupNumber = GroupNumber

    def process(self, string):
        """returns a file path to the written file"""
        raise NotImplementedError('Subclass must implement abstract method')

    @staticmethod
    def document():
        doc = {}
        doc['HANDLERTYPE'] = 'PLACEHOLDER'
        doc['PLACEHOLDER'] = ''
        doc['DESCRIPTION'] = ''
        return doc
