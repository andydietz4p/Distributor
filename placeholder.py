#
# Available placeholders
# Date - 2017-01-01
# Year - 2017
# Month - 01
# Day - 01
# GroupNumber

import time


def placeholder_process(replacestring, GroupNumber):
    outstring = replacestring \
        .replace('<Month>', time.strftime('%m')) \
        .replace('<Day>', time.strftime('%d')) \
        .replace('<GroupNumber>', GroupNumber)
    return outstring
