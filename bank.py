# bank.py
def read_bank_amount(default_amount=1000):
    """
    Reads the entry amount from 'bank.txt'. If 'bank.txt' does not exist or an error occurs,
    it returns the default entry amount.
    """
    try:
        with open('bank.txt', 'r') as f:
            entry_amount_on_file = f.read()
            entry_amount = int(entry_amount_on_file)
            return entry_amount
    except (FileNotFoundError, ValueError, OSError):
        return default_amount
