import configparser
import random
import string

config = configparser.ConfigParser()
config.read('config.ini')

# get the settings from the config file
password_length = int(config['password']['length'])
allowed_char_sets = {
    'lowercase': string.ascii_lowercase,
    'uppercase': string.ascii_uppercase,
    'digits': string.digits,
    'special': string.punctuation,
    'alphanumeric': string.ascii_letters + string.digits
}

def generate_password(length = password_length, allowed_chars = None):
    """Generates a password of a fixed length using the specified character set"""
    if allowed_chars is None:
        allowed_chars = allowed_char_sets['alphanumeric'] + allowed_char_sets['special']
    else:
        parsed_chars = []
        for char_code in allowed_chars.split(','):
            if char_code in allowed_char_sets:
                parsed_chars.extend(allowed_char_sets[char_code])
            else:
                raise ValueError(f'Invalid character set code: {char_code}')
        allowed_chars = ''.join(parsed_chars)

    password = ''.join(random.choice(allowed_chars) for _ in range(length))
    complexity = len(allowed_chars)
    return password, complexity

def format_time_to_crack(time_to_crack):
    units = ['years', 'million years', 'billion years', 'trillion years', 'quadrillion years', 
             'quintillion years', 'sextillion years', 'septillion years', 'octillion years']
    for i, unit in enumerate(units):
        if time_to_crack < 1000:
            return f'{time_to_crack:.2f} {unit}'
        time_to_crack /= 1000
        return f'{time_to_crack:.2f} {units[-1]} or more'

def check_strength(password, complexity):
    """Calculates password strength based on length and complexity. 
    Returns a tuple of score (based on length) and 
    feedback (The length of time needed to guess the password)"""
    
    score = 0
    feedback = ''
    password_length = len(password)

    if password_length < 8:
        feedback += 'Password is too short.\n'
    elif password_length < 12:
        score += 1
        feedback += 'Password length is OK, but could be longer.\n'
    else:
        score += 2
        feedback += 'Password length is good.\n'

    # calculate the estimated time to crack the password assuming:
    # 10 million guesses per second

    guesses_per_second = 10000000
    time_to_crack = (complexity ** password_length) / guesses_per_second / 3600 / 24 / 365 # in terms of years
    feedback += f'It would take approximately {format_time_to_crack(time_to_crack)} to crack this password using a brute force attack.\n'

    return score, feedback