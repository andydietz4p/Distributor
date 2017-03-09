from os.path import dirname, basename, isfile
import glob

for f in glob.glob(dirname(__file__) + "/*.py"):
    if basename(f) != '__init__.py':
        exec("from .%s import %s" % (basename(f)[:-3], basename(f)[:-3]))
