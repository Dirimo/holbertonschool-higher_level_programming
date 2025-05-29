#!/usr/bin/python3
class VerboseList(list):
    """
    A custom list class that prints a notification message
    every time an item is added or removed.
    """

    def append(self, item):
        """
        Appends an item to the list and prints a notification.
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """
        Extends the list with an iterable and prints a notification.
        """
        num_items = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with {num_items} items.")

    def remove(self, item):
        """
        Removes an item from the list and prints a notification.
        """
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item from the list and prints a notification.
        """
        if index == -1:
            item = super().pop()
        else:
            item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item


if __name__ == "__main__":
    verbose_list = VerboseList()

    verbose_list.append("apple")
    verbose_list.extend(["banana", "cherry"])
    verbose_list.remove("apple")
    verbose_list.pop()
    verbose_list.append("date")
    verbose_list.pop(0)

    print(f"Current list: {verbose_list}")
