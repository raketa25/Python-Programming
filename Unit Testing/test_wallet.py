from wallet import Wallet, InsufficientAmount
import pytest

# # a newly created wallet has a balance of 0 by default.
# def test_wallet_initial_amount():
#     wallet = Wallet()
#     assert wallet.balance == 0

# # a newly created wallet with an initial balance of 100 has a balance of 100.
# def test_wallet_initial_amount_with_value():
#     wallet = Wallet(100)
#     assert wallet.balance == 100

# # a wallet created with an initial balance of 10 to which 90 is added has a balance of 100.
# def test_wallet_add_cash():
#     wallet = Wallet(10)
#     wallet.add_cash(90)
#     assert wallet.balance == 100

# # a wallet created with an initial balance of 20 from which 10 is removed has a balance of 10.
# def test_wallet_spend_cash():
#     wallet = Wallet(20)
#     wallet.spend_cash(10)
#     assert wallet.balance == 10

# # a wallet that tries to spend more than its balance will cause an InsufficientAmount error message.
# def test_wallet_spend_cash_insufficient_amount():
#     wallet = Wallet(20)
#     with pytest.raises(InsufficientAmount):
#         wallet.spend_cash(10)

# =================== Using fixtures to avoid code repetition in the test functions ===================

# @pytest.fixture
# def empty_wallet():
#     """ Returns a Wallet instance with a zero balance."""
#     return Wallet()

# @pytest.fixture
# def wallet():
#     """ Returns a Wallet instance with a balance of 50."""
#     return Wallet(50)

# # New test functions using the fixtures
# def test_default_initial_amount(empty_wallet):
#     assert empty_wallet.balance == 0

# def test_wallet_has_correct_initial_amount(wallet):
#     assert wallet.balance == 50

# def test_wallet_add_cash(wallet):
#     wallet.add_cash(50)
#     assert wallet.balance == 100

# def test_wallet_spend_cash(wallet):
#     wallet.spend_cash(20)
#     assert wallet.balance == 30

# def test_wallet_spend_cash_insufficient_amount(wallet):
#     with pytest.raises(InsufficientAmount):
#         wallet.spend_cash(100)


# Parametrized test functions

@pytest.mark.parametrize("earned,spent,expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected

