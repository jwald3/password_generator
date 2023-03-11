# Secure Password Generator CLI

This command-line interface (CLI) tool generates a random password that meets your desired specifications. You can choose the length of the password and the character set from which the password will be generated. The tool also calculates the strength of the password and provides feedback on how long it would take to crack the password using a brute force attack.

## Installation

1. Clone the repository to your local machine.
2. Install the required packages: `pip install -r requirements.txt`
3. Run the tool: `python password_generator.py`

## Usage

```
usage: password_generator.py [-h] [--length LENGTH]

Generate a random password.

optional arguments:
  -h, --help       show this help message and exit
  --length LENGTH  the length of the generated password
```

If you do not specify a length using the --length argument, the tool will generate a password with the default length specified in config.ini.

## Configuration

The `config.ini` file allows you to customize the default password length and character set.

```
[password]
length = 16
allowed_chars = ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-={}[]|\:;"'<>,.?/~`
```

## Example Output

```
$ python password_generator.py --length 12
# output
q3=0S&}@frJH
Strength score: 2
Password length is good.
It would take approximately 1.51 million years or more to crack this password using a brute force attack.
```


## Contributing

Contributions are welcome! If you find a bug or have a feature request, please submit an issue or pull request.
