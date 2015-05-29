import urllib
import inspect
import codecs


def printit(libname, path):
    print('')
    print('# ' * 40)
    print(libname + ' source is at : ' + path)
    print('')


path = inspect.getfile(urllib)
printit('urllib', path)

path = inspect.getfile(codecs)
printit('codecs', path)
