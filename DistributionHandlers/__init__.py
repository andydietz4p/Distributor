# from .EmailDistributionHandler import EmailDistributionHandler
# from .FileDistributionHandler import FileDistributionHandler
# from .SFTPDistributionHandler import SFTPDistributionHandler
from os.path import dirname, basename, isfile
import glob

modulenames = glob.glob(dirname(__file__) + "/*.py")
disthandlers = {}
for f in modulenames:
    if basename(f) != '__init__.py':
        exec("from .%s import %s" % (basename(f)[:-3], basename(f)[:-3]))
