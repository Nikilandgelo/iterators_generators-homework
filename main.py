import types

list_of_lists = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

class FlatIterator:

    def __init__(self, nested_list: list):
        self.nested_list = nested_list

    def __iter__(self):
        self.list_counter = 0
        self.items_counter = 0
        return self

    def __next__(self):
        index_current_item = self.items_counter

        if index_current_item < len(self.nested_list[self.list_counter]):
            self.items_counter += 1
            return self.nested_list[self.list_counter][index_current_item]
        else:
            self.list_counter += 1
            if self.list_counter >= len(self.nested_list):
                raise StopIteration
            else:
                self.items_counter = 1
                return self.nested_list[self.list_counter][self.items_counter - 1]
    
def flat_generator(nested_list: list):
    for list_ in nested_list:
        for item in list_:
            yield item

def test1():
    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

def test_2():
    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    
    assert list(flat_generator(list_of_lists)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists), types.GeneratorType)

if __name__ == '__main__':
    test1()
    test_2()