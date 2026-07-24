from DataReader import DataReader
from FilterFunctions import FilterFunctions
class SignalProcessor:
    def process(self):
        d=DataReader();f=FilterFunctions();d.read();f.filter();print('Signal Processed')
