import argparse
from password_generator import generate_password, password_length, allowed_chars, check_strength


# creates the command-line parser. When you call --help, this is what is printed in the header
parser = argparse.ArgumentParser(description='Generate a random password.')

# add an optional argument for password length (that will be used instead of the default)
parser.add_argument('--length', '-l', type=int, help='the length of the generated password')

# parse the arguments given by the user
args = parser.parse_args()


password = generate_password(args.length or password_length, allowed_chars)
score, feedback = check_strength(password)
print(password)
print(f'Strength score: {score}')
print(feedback)
