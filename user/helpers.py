def password_num(password):
    numbers = '1234567890'
    count = 0
    for character in password:
        if character in numbers:
            count += 1
    return count


def password_special_char(password):
    special_characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    count = 0
    for character in password:
        if character in special_characters:
            count += 1
    return count
