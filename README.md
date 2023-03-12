# Secure Password Generator CLI

This command-line interface (CLI) tool generates a random password that meets your desired specifications. You can choose the length of the password and the character set from which the password will be generated. The tool also calculates the strength of the password and provides feedback on how long it would take to crack the password using a brute force attack.

## Installation

1. Clone the repository to your local machine.
```
git clone https://github.com/<username>/<repository-name>.git
```
2. Install the required packages using `pip`:
```
cd <repository-name>
pip install -r requirements.txt
```
3. Run the tool using the `generator.py` script:
```
python generator.py
```

## Usage

### Generating a password
You can generate a password with default settings or customize it using the following arguments:

```
usage: generator.py [-h] [--length LENGTH] [--char_set CHAR_SET] [--word_list]

Generate a random password.

optional arguments:
  -h, --help            show this help message and exit
  --length LENGTH, -l LENGTH
                        the length of the generated password (default: 16)
  --char_set CHAR_SET, -c CHAR_SET
                        a comma-separated list of character set codes to use when generating the password (e.g. "lowercase, digits")
  --word_list, -w       generate password using words from the NLTK corpus

```

By default, the tool generates a password with a length of 16 characters, including lowercase and uppercase letters, digits, and special characters. If you do not specify a length using the --length argument, the tool will use the default length.
You can specify a custom character set using the --char_set argument. Separate multiple character sets by commas (e.g., --char_set lowercase, digits, special). Available character sets include:
- `lowercase`: lowercase letters (abcdefghijklmnopqrstuvwxyz)
- `uppercase`: uppercase letters (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
- `digits`: digits (0123456789)
- `special`: special characters (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
- `alphanumeric`: alphanumeric characters (letters and digits)

If you want to generate a password using random words from the NLTK corpus, use the `--word_list` argument.

## Checking password strength
The tool also calculates the strength of the password and provides feedback on how long it would take to crack the password using a brute force attack. The strength score is based on the length and complexity of the password.

```
Strength score: <score>
<feedback>
```

The feedback includes the estimated time to crack the password, assuming a brute force attack with 10 million guesses per second.

## Testing

The `test_password_generator.py` file contains unit tests for the password generator functions. To run the tests, use the following command:

```
python -m unittest test_password_generator.py
```


## Configuration

You can customize the default settings for the password length and character set in the `config.ini` file.

```
[password]
length = 16
allowed_chars = ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-={}[]|\:;"'<>,.?/~`
```

## Example Output
### Generating a password with default settings

```
$ python generator.py
GvI#45an@YrT!rW2
Strength score: 2
Password length is good.
It would take approximately 8.81 quadrillion years or more to crack this password using a brute force attack.
```

## Running the test suite
To run the test suite, navigate to the root directory of the project and run the following command:

```python -m unittest discover -s . -p "*_test.py"```

This will run all the test cases in the root directory of the project that match the pattern `*_test.py`.

The test suite includes tests for the password generator functions and the `format_time_to_crack` and `check_strength` functions. The tests ensure that the functions behave as expected and provide accurate results.

## Conclusion

The Secure Password Generator CLI is a useful tool for generating secure passwords quickly and easily. With the ability to customize password length and character sets, the tool can meet the specific needs of individual users. The tool also provides feedback on the strength of the password and estimates the time required to crack it, making it a valuable addition to any security-conscious individual's toolkit.
