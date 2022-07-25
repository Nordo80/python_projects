"""KTdx1."""


def positive_or_not(nums: list, pos: bool) -> list:
    """
    Given a list of integers and a boolean pos.

    If pos is True, return a new list containing only positive numbers of the first list.
    Otherwise return a new list containing all the other numbers but positive of the given list.

    print(positive_or_not([9, 5, 0, 6, -5, -1], True))  => [9, 5, 6]
    print(positive_or_not([3, 4, -2, 1, -78, 0], False))  => [-2, -78, 0]

    :param nums:
    :return:
    """
    list_list = []
    if pos:
        for a in nums:
            if a >= 1:
                list_list.append(a)
        return list_list
    else:
        for a in nums:
            if a <= 0:
                list_list.append(a)
        return list_list


def sum_half_evens(nums: list) -> int:
    """
    Return the sum of first half of even ints in the given array.

    If there are odd number of even numbers, then include the middle number.

    sum_half_evens([2, 1, 2, 3, 4]) => 4
    sum_half_evens([2, 2, 0, 4]) => 4
    sum_half_evens([1, 3, 5, 8]) => 8
    sum_half_evens([2, 3, 5, 7, 8, 9, 10, 11]) => 10
    """
    list_list = []
    for a in nums:
        if a % 2 == 0:
            list_list.append(a)
    indexx = len(list_list) // 2
    counter = list_list[0: indexx]
    if len(counter) >= 1:
        if len(list_list) % 2 != 0:
            a = list_list[len(list_list) // 2]
            for al in counter:
                al += al
            b = al + a
            return b
        else:
            for al in counter:
                al += al
            b = al
            return b
    else:
        if len(list_list) % 2 != 0:
            a = list_list[len(list_list) // 2]
            return a
        else:
            return 0


def max_block(s: str) -> int:
    """
    Get full name of the person.

    Return firstname and lastname separated by space.
    If the lastname is empty, then return only the firstname.
    """
    counter = 0
    if len(s) >= 1:
        for char in s:
            count = s.count(char)
            if count >= counter:
                counter = count
        return counter
    return counter


class Person:
    """Person class."""

    def __init__(self, firstname: str, lastname: str, phone_number: str):
        """Constructor."""
        self._firstname = firstname
        self._lastname = lastname
        self._phone_number = phone_number

    def get_full_name(self) -> str:
        """
        Get full name of the person.

        Return firstname and lastname separated by space.
        If the lastname is empty, then return only the firstname.
        """
        return self._firstname + " " + self._lastname

    @property
    def firstname(self):
        """
        Get full name of the person.

        Return firstname and lastname separated by space.
        If the lastname is empty, then return only the firstname.
        """
        return self._firstname

    @property
    def lastname(self):
        """
        Get full name of the person.

        Return firstname and lastname separated by space.
        If the lastname is empty, then return only the firstname.
        """
        return self._lastname


class ContactBook:
    """Contacat book class."""

    def __init__(self):
        """Constructor."""
        self.contacts = []

    def add_person_to_contacts(self, person: Person) -> None:
        """Add person to contact book if phone number and firstname are not empty strings."""

    def find_contact_by_number(self, number) -> Person:
        """
        Return person who has the given number.

        If there are several people with the given number, return the first.
        If there is no person with the given number, return None.
        """
        pass

    def get_sorted_contacts(self) -> list:
        """Sort contacts alphabetically by full name."""
        pass


class FridgeItem:
    """Fridge item class."""

    def __init__(self, name: str, type: str, days_till_expiration: int):
        """Constructor."""
        pass

    def __repr__(self):
        """
        Return FridgeItem in nice string form.

        For example:
        name = "apple", type = "fruit", days_till_expiration = 4
        "Name: apple, type: fruit, expires in 4 days."

        If the item expires today (expires in 0 days):
        name = "apple", type = "fruit", days_till_expiration = 0
        "Name: apple, type: fruit, expires today."

        If the item has already expired:
        name = "apple", type = "fruit", days_till_expiration = -2
        "Name: apple, type: fruit, expired 2 days ago."

        If the item expired yesterday (one day ago):
        name = "apple", type = "fruit", days_till_expiration = -1
        "Name: apple, type: fruit, expired 1 day ago."

        If the item expires tomorrow (in one day):
        name = "apple", type = "fruit", days_till_expiration = 1
        "Name: apple, type: fruit, expires in 1 day."

        :return:
        """
        pass


class Fridge:
    """Fridge class."""

    def __init__(self):
        """Constructor."""
        pass

    def add_items(self, items: list):
        """
        Add given items to items list.

        If an item is in the list already, don't add it.
        """
        pass

    def get_items(self) -> list:
        """Return items in the fridge."""
        pass

    def remove_item(self, item: FridgeItem) -> None:
        """Remove FridgeItem from items list if it's there."""
        pass

    def clean_the_fridge(self) -> None:
        """Remove all the items from the fridge that have expired."""
        pass

    def get_items_that_wont_have_expired_in_n_days(self, n: int) -> list:
        """
        Return list of items that won't have expired in given n days.

        An item hasn't expired on its 0. day till expiration.

        Example:
        item 1 expires in 3 days
        item 2 expires in 4 days
        item 3 expires in 5 days
        calling this method with n = 4 returns items 2 and 3.
        """
        pass

    def get_sorted_items(self) -> list:
        """
        Sort FridgeItems by days till expiration (first should be expired items, then first expiring).

        If they have the same amount of days till expiration, sort them by name (descending).
        :return: sorted list of FridgeItems
        """
        pass

    def get_items_of_type(self, type: str) -> list:
        """Return list of items that are the given type (case-sensitive)."""
        pass

    def get_items_with_name(self, name: str):
        """
        Return list of items with which name you can form the required name by re-arranging letters in the name.

        Capital and non-capital letters are equal here (case-insensitive).
        Example:
        if the parameter name = "milk" then items with names "Milk" and "LIMK" will be returned.
        """
        pass


if __name__ == '__main__':
    print(sum_half_evens([2]))
    print("------------------")
    print(max_block("hoopla"))
    print(max_block("abbCCCddBBBxx"))
    print(max_block(""))
    print(positive_or_not([9, 5, 0, 6, -5, -1], True))
    print(positive_or_not([3, 4, -2, 1, -78, 0], False))
    p1 = Person("Peeter", "Mets", "12345678")
    print(p1.get_full_name())  # Peeter Mets

    p2 = Person("Kaarel", "", "54323456")
    print(p2.get_full_name())  # Kaarel

    contact_book = ContactBook()
    contact_book.add_person_to_contacts(p1)
    contact_book.add_person_to_contacts(p2)
    print(len(contact_book.contacts))  # 2

    for contact in contact_book.get_sorted_contacts():
        print(contact.get_full_name())
    """Kaarel
       Peeter Mets"""

    print(contact_book.find_contact_by_number("12345678").get_full_name())  # Peeter Mets
