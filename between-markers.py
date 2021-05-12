
def between_markers(text: str, begin: str, end: str) -> str:
    resut = text[:text.index(end)] if end in text else text
    return resut[resut.index(begin)+len(begin):] if begin in resut else ('' if begin in text else resut)


if __name__ == '__main__':
    print('Example:')
    # between_markers('What is >apple<', '>', '<')

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

