def is_anagram(message1, message2):
    for character in message2:
        if character not in message1:
            return False
    return True