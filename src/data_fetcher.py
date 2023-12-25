import random

# Sample data for each field
_first_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth']
_last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']


def generate_random_data(n):
    """
    Generate n random choices for each field.

    :param n: Number of random choices to generate for each field
    :return: A list of dictionaries containing the random data
    """
    count = 1
    for _ in range(n):
        yield count, {
            'firstname': random.choice(_first_names),
            'lastname': random.choice(_last_names)
        }
        count += 1
