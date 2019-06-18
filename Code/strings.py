#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    text_index = 0 
    pattern_index = 0 

    # base cases
    if pattern == '' or text == pattern:
        return True

    while text_index <= len(text)-1:
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == len(pattern) - 1:
                return True
            pattern_index += 1
        else:
            text_index -= pattern_index
            pattern_index = 0
        text_index += 1
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    starting_index = None
    text_index = 0 
    pattern_index = 0 

    # base cases
    if pattern == '' :
        return 0
    
    for text_index, char in enumerate(text):
        while pattern[pattern_index]== text[text_index]:
            if starting_index is None:
                starting_index = text_index
            if len(pattern) - 1 == pattern_index:
                return starting_index
            pattern_index += 1
            text_index += 1
        pattern_index = 0
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    all_indexes = []

    if len(pattern) == 0:
        return list(range(len(text)))
    if len(pattern) > len(text):
        return all_indexes

    text_index = 0
    pattern_index = 0

    while text_index < len(text):

        if text[text_index] == pattern[pattern_index]:

            # equal until last character in pattern
            if pattern_index == len(pattern) - 1:

                # calculate the start index and append to the result array
                start_index = text_index - pattern_index
                all_indexes.append(start_index)

                # point the text index to be one ahead the start index
                text_index = start_index + 1
                pattern_index = 0

            # equal in the pattern
            else:

                pattern_index += 1
                text_index += 1

        else:

            # set back to the next index since it didnt pass all the pattern
            if pattern_index != 0:
                text_index = (text_index - pattern_index) + 1
            else:
                # set to next index
                text_index += 1

            pattern_index = 0

    return all_indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))

    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))

    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
