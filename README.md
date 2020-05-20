# MoneyBank

![Tests](https://github.com/dimensi0n/MoneyBank/workflows/Python%20application/badge.svg)
![Python version](https://img.shields.io/badge/Python%20version-3.8-yellow)

CashMachine for supermarket software 💰

## How to test it

* Clone the repository
* Run `tests.py`

## How to use it

```python
import src.main as bank
machine = bank.MoneyBank([1, 1, 0.5, 0.5, 0.2]) # Pieces available in your cash machine

# Make a payment
machine.pay([2, 1], 2.5) # Pieces the customer gave, price of the product

"""
Will return (0, [0.5])  
  O is the money you still have to give if you does not have enough money in your machine
  [0.5] is/are the piece(s) you have to give back
"""
```

## To do

* Add products management
* Add tkinter
