"""Bank."""

import datetime
import random


class PersonError(Exception):
    """Person error."""

    pass


class TransactionError(Exception):
    """Transaction error."""

    pass


class Person:
    """Person class."""

    def __init__(self, first_name: str, last_name: str, a: int):
        """
        Person constructor.

        :param first_name: first name
        :param last_name: last name
        :param age: age, must be greater than 0
        """
        self.first_name = first_name
        self.last_name = last_name
        if a >= 1:
            self._age = a
        else:
            raise PersonError
        self.bank_account = None

    @property
    def full_name(self) -> str:
        """Get person's full name. Combination of first and last name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> int:
        """Get person's age."""
        return self._age

    @age.setter
    def age(self, value: int):
        """Set person's age. Must be greater than 0."""
        self._age = value
        if self._age <= 0:
            raise PersonError

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name


class Bank:
    """Bank class."""

    def __init__(self, name: str):
        """
        Bank constructor.

        :param name: name of the bank
        """
        self.name = name
        self.customers = []
        self.transactions = []

    def add_customer(self, person: Person) -> bool:
        """
        Add customer to bank.

        :param person: person object
        :return: was customer successfully added
        """
        if person not in self.customers:
            person.bank_account = Account(0, person, self)
            self.customers.append(person)
            return True
        else:
            return False

    def remove_customer(self, person: Person) -> bool:
        """
        Remove customer from bank.

        :param person: person object
        :return: was customer successfully removed
        """
        for i in self.customers:
            if i == person:
                person.bank_account = None
                self.customers.remove(i)
                return True
        return False

    def __repr__(self) -> str:
        """
        Bank representation.

        :return: name of the bank
        """
        return self.name


class Transaction:
    """Transaction class."""

    def __init__(self, amount: float, date: datetime.date, sender_account: 'Account', receiver_account: 'Account',
                 is_from_atm: bool):
        """
        Transaction constructor.

        :param amount: value
        :param date: date of the transaction
        :param sender_account: sender's object
        :param receiver_account: receiver's object
        :param is_from_atm: is transaction from atm
        """
        self.amount = amount
        self.date = date
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.is_from_atm = is_from_atm

    def __repr__(self) -> str:
        """
        Transaction representation.

        :rtype: object's values displayed in a nice format
        """
        if self.is_from_atm:
            return f"({self.amount} €) ATM"
        else:
            return f"({self.amount} €) {self.sender_account.person.full_name} -> {self.receiver_account.person.full_name}"


class Account:
    """Account class."""

    def __init__(self, balance: float, person: Person, bank: 'Bank'):
        """
        Account constructor.

        :param balance: initial account balance
        :param person: person object
        :param bank: bank object
        """
        self._balance = balance
        self.person = person
        self.bank = bank
        self.transactions = []
        self.number = f"EE{random.randint(100000000000000000, 999999999999999999)}"

    @property
    def balance(self) -> float:
        """Get account's balance."""
        return self._balance

    def deposit(self, amount: float, is_from_atm: bool = True):
        """Deposit money to account."""
        if amount <= 0:
            raise TransactionError
        self._balance += amount
        if is_from_atm:
            transaction = Transaction(amount, datetime.date.today(), self, self, is_from_atm)
            self.transactions.append(transaction)
            self.bank.transactions.append(transaction)

    def withdraw(self, amount: float, is_from_atm: bool = True):
        """Withdraw money from account."""
        if amount <= 0 or self._balance < amount:
            raise TransactionError
        self._balance -= amount
        if is_from_atm:
            transaction = Transaction(-amount, datetime.date.today(), self, self, is_from_atm)
            self.transactions.append(transaction)
            self.bank.transactions.append(transaction)

    def transfer(self, amount: float, receiver_account: 'Account'):
        """Transfer money from one account to another."""
        if self._balance >= amount + 5 and self.person != receiver_account.person or receiver_account != self:
            t = Transaction(amount, datetime.date.today(), self, receiver_account, False)
            if self.bank != receiver_account.bank:
                self.withdraw(amount + 5, False)
                receiver_account.bank.transactions.append(t)
            else:
                self.withdraw(amount, False)
            receiver_account.deposit(amount, False)
            receiver_account.transactions.append(t)
            self.bank.transactions.append(t)
            self.transactions.append(t)
        else:
            raise TransactionError

    def account_statement(self, from_date: datetime.date, to_date: datetime.date) -> list:
        """All transactions in given period."""
        account_statement_list = []
        for i in self.transactions:
            if from_date <= i.date <= to_date:
                account_statement_list.append(i)
        return account_statement_list

    def get_debit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total income in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: debit turnover number
        """
        counter = 0
        for i in self.transactions:
            if from_date <= i.date <= to_date:
                if i.amount > 0 and i.is_from_atm or self == i.receiver_account and i.is_from_atm is False:
                    counter += i.amount
        return counter

    def get_credit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total expenditure in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: credit turnover number
        """
        counter = 0
        for i in self.transactions:
            if from_date <= i.date <= to_date:
                if i.amount < 0 or self == i.sender_account and i.is_from_atm is False:
                    counter -= abs(i.amount)
        return counter

    def get_net_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get net turnover (income - costs) in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: net turnover number
        """
        return self.get_debit_turnover(from_date, to_date) + self.get_credit_turnover(from_date, to_date)

    def __repr__(self) -> str:
        """
        Account representation.

        :return: account number
        """
        return self.number
