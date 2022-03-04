def format_data_for_display(people):
    formatted_data = []
    for person in people:
        full_name = f"{person['given_name']} {person['family_name']}"
        formatted = f"{full_name}: {person['title']}"
        formatted_data.append(formatted)
    return formatted_data


def format_data_for_excel(people):
    formatted_data = 'given,family,title'
    for person in people:
        formatted_data += f"""
{person['given_name']},{person['family_name']},{person['title']}"""

    return formatted_data


def is_palindrome(string):
    new_string = ''
    string = [string.replace(char, '') for char in string if not char.isalnum()]
    for char in string:
        if char.isalnum():
            new_string += char
    new_string = new_string.lower()

    if new_string == new_string[::-1]:
        return True
    return False
