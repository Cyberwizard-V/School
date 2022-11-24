import pytest
from bankaccount import BankAccount

def broke():
    account = BankAccount(1)
    account.deposit(50)
    assert account.withdraw(60) == False

broke()
