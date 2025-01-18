from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass 

class QuickSort(SortingStrategy):
    def sort(self, data):
        print('Quick Sort: Sorting Strategy')
        return sorted(data)

class MergeSort(SortingStrategy):
    def sort(self, data):
        print('Merge Sort: Sorting Strategy')
        return sorted(data)

# Context
class DataProcessor:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy):
        self._strategy = strategy 

    def process_strategy(self, data):
        return self._strategy.sort(data)

if __name__=='__main__':
    data = [5, 2, 9, 1, 5, 6]
    processor = DataProcessor(QuickSort())
    print('Result Using Quick Sort: ', processor.process_strategy(data))

    processor = DataProcessor(MergeSort())
    print('Result Using Merge Sort: ', processor.process_strategy(data))