# TP Secret Recovery
```
usage: TP-SecretRecovery.py [-h] --data-leaked DATA_LEAKED [--startsWith STARTSWITH] [--endsWith ENDSWITH] [--number-of-reuses NUMBER_OF_REUSES]

options:
  -h, --help            show this help message and exit
  --data-leaked DATA_LEAKED
                        The string consisting of concatenated pairs of three characters exfiltrated from the string SECRET
  --startsWith STARTSWITH
                        The starting character string of the string SECRET
  --endsWith ENDSWITH   The ending character string of the string SECRET
  --number-of-reuses NUMBER_OF_REUSES
                        The number of reuses of each element in the data_leaked array (default: 3)
```

![TP-SecretRecovery](https://github.com/truocphan/TP-SecretRecovery/blob/0b193bc2d4d331d20d4b796699373daf93d7f539/TP-SecretRecovery.gif)
