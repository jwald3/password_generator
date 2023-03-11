# Secure Password Generator CLI

This command-line interface (CLI) tool generates a random password that meets your desired specifications. You can choose the length of the password and the character set from which the password will be generated. The tool also calculates the strength of the password and provides feedback on how long it would take to crack the password using a brute force attack.

## Installation

1. Clone the repository to your local machine.
2. Install the required packages: `pip install -r requirements.txt`
3. Run the tool: `python password_generator.py`

## Usage

```
usage: generator.py [-h] [--length LENGTH] [--char_set CHAR_SET] [--help_char_sets]

Generate a random password.

optional arguments:
  -h, --help            show this help message and exit
  --length LENGTH, -l LENGTH
                        the length of the generated password
  --char_set CHAR_SET, -c CHAR_SET
                        a comma-separated list of character set codes to use when generating the password (e.g. "lowercase, digits")
  --help_char_sets, -hcs
                        display the available character sets
```

If you do not specify a length using the `--length` argument, the tool will generate a password with the default length specified in `config.ini.`

You can specify a custom character set using the `--char_set` argument. Separate multiple character sets by commas (e.g. `--char_set lowercase, digits`). If you need help with the available character sets, use the `--help_char_sets` argument.
## Configuration

The `config.ini` file allows you to customize the default password length and character set.

```
[password]
length = 16
allowed_chars = ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-={}[]|\:;"'<>,.?/~`
```

## Example Output

```
$ python generator.py --length 12 --char_set lowercase, digits
# output
u5gyzrm0htoj
Strength score: 2
Password length is good.
It would take approximately 1.95 million years or more to crack this password using a brute force attack.
```


## Contributing

Contributions are welcome! If you find a bug or have a feature request, please submit an issue or pull request.
