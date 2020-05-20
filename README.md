# MoneyBank

CashMachine for supermarket software 💰

## How to test it

* Clone the repository
* Run `tests.py

## How to use it

```python
import src.main as bank
machine = bank.MoneyBank([1, 1, 0.5, 0.5, 0.2]) // Pieces available in your cash machine

// Make a payment
machine.pay([2, 1], 2.5) // Pieces the customer gave, price of the product

## To do

* Add bills management
* Add products management
