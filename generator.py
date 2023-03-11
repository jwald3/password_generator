import argparse
from password_generator import generate_password, password_length, check_strength, allowed_char_sets


# creates the command-line parser. When you call --help, this is what is printed in the header
parser = argparse.ArgumentParser(description='Generate a random password.')

# add an optional argument for password length (that will be used instead of the default)
parser.add_argument('--length', '-l', type=int, help='the length of the generated password')

# add an optional argument for the allowed characters
parser.add_argument('--char_set', '-c', type=str, help='a comma-separated list of character set codes to use when generating the password (e.g. "lowercase, digits")')

# add an argument to display available character sets
parser.add_argument('--help_char_sets', '-hcs', action='store_true', help='display the available character sets')

# parse the arguments given by the user
args = parser.parse_args()

if args.help_char_sets:
    print('Available character sets:')
    for char_set in allowed_char_sets:
        print(f'{char_set}: {allowed_char_sets[char_set]}')
else:
    password, complexity = generate_password(args.length or password_length, args.char_set or None)
    score, feedback = check_strength(password, complexity)
    print(password)
    print(f'Strength score: {score}')
    print(feedback)
