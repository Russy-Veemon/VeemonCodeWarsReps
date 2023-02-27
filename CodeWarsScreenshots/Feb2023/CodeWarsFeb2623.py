# Write a simple regex to validate a username. Allowed characters are:
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

import re

def validate_usr(username):
    regex = r"^[a-z0-9_]{4,16}$"
    # Define the expression pattern as a raw string
    return bool(re.match(regex, username))
    # use re.match to check if the username matches the pattern above
