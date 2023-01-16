# The Task
# Think of a way to store the languages as a database (eg an object). The languages are listed below so you can copy and paste!
# Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input.
# The Database

languages = {
    'english': 'Welcome',
    'czech': 'Vitejte',
    'danish': 'Velkomst',
    'dutch': 'Welkom',
    'estonian': 'Tere tulemast',
    'finnish': 'Tervetuloa',
    'flemish': 'Welgekomen',
    'french': 'Bienvenue',
    'german': 'Willkommen',
    'irish': 'Failte',
    'italian': 'Benvenuto',
    'latvian': 'Gaidits',
    'lithuanian': 'Laukiamas',
    'polish': 'Witamy',
    'spanish': 'Bienvenido',
    'swedish': 'Valkommen',
    'welsh': 'Croeso'
    }
def greet(language):
    if language in languages:
        return languages[language]
    else:
        return languages["english"]

# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!
# input
# customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.

def queue_time(customers, n):
    # Initialize time and till counters
    time = 0
    tills = [0] * n
    while customers:
        # Find the next available till
        next_till = tills.index(min(tills))
        # Assign the next customer to the till
        tills[next_till] += customers.pop(0)
        # Update the time to the maximum time of all tills
        time = max(tills)
    return time