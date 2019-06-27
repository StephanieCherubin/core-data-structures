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
    indexes = find_all_indexes(text, pattern, start=0)

    if find_all_indexes(text, pattern, start=0):
        return indexes[0]

def find_all_indexes(text, pattern, start =0):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    indexes = []
    text_index = 0 
    pattern_index = 0 
    starting_index = 0

    if pattern == '' :
        iterator = 0
        while iterator < len(text):
            indexes.append(iterator)
            iterator += 1
        return indexes

    for text_index, char in enumerate(text):
        starting_index = text_index

        while pattern[pattern_index]== text[text_index]:
            
            if len(pattern) - 1 == pattern_index:
                indexes.append(starting_index) 
                break

            pattern_index += 1
            text_index += 1

            if text_index == len(text):
                break

        pattern_index = 0
    return indexes

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
