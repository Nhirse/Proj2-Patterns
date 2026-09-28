_tax_rate = 0.08

def calculate_subtotal(items):
    return sum(items)


def calculate_tax(subtotal):
    return subtotal * _tax_rate


def calculate_total(items):
    subtotal = calculate_subtotal(items)
    return subtotal + calculate_tax(subtotal)

"""
MODULE PATTERN
This pattern exports functions from a file but only lets them use specific functions with access.
The internal implementation details remain hidden from the external file.

Use Cases:
1. A shopping application can place all price-calculation functions
   inside one module.
2. A banking application can group account-related utility functions
   into one module.
3. A game can keep score calculations and game-state utilities together.

Benefits:
1. Organization - related functions and data are kept together.
2. Encapsulation - internal implementation details can be separated
   from the public interface.
3. Reusability - the module can be imported and reused by several
   different parts of a program.
"""