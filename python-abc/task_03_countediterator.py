#!/usr/bin/python3
class CountedIterator:
    """
    A custom iterator class that keeps track of the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initializes a CountedIterator object.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next item from the iterator and increments the counter.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Returns the number of items that have been iterated over.
        """
        return self.count


if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    counted_iterator = CountedIterator(my_list)

    for item in counted_iterator:
        print(f"Item: {item}")
        print(f"Count: {counted_iterator.get_count()}")

    print(f"Total items iterated: {counted_iterator.get_count()}")
