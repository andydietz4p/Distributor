from PlaceholderHandler import PlaceholderHandler


class GroupnumberPlaceholderHandler(PlaceholderHandler):
    def process(self, string):
        return string.replace('<GroupNumber>', self.GroupNumber)

    @staticmethod
    def document():
        doc = {}
        doc['PLACEHOLDER'] = 'GroupNumber'
        doc['DESCRIPTION'] = 'Replaces <GroupNumber> with the 7 character group number'
        return doc
