import re

# Define patterns for different token types using regex
keywords = {'if', 'else', 'while', 'for', 'return', 'int', 'float'}
punctuators = {',', ';', '(', ')', '{', '}'}
assignment_operator = '='
operators = {'+', '-', '*', '/', '%'}
constants = r'\d+(\.\d+)?'  # Matches integers or floating-point numbers
identifiers = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Identifiers start with a letter or underscore
literals = r'\"[^\"]*\"'  # Matches strings enclosed in double quotes

# Regular expressions for each token
token_patterns = {
    'keyword': r'\b(?:' + '|'.join(keywords) + r')\b',
    'identifier': identifiers,
    'literal': literals,
    'constant': constants,
    'operator': r'|'.join(map(re.escape, operators)),
    'assignment_operator': re.escape(assignment_operator),
    'punctuator': r'|'.join(map(re.escape, punctuators))
}

# Tokenizing function
def tokenize(input_string):
    tokens = []
    position = 0

    while position < len(input_string):
        match = None

        # Skip whitespace characters
        if input_string[position].isspace():
            position += 1
            continue

        # Check for each token type in the input string
        for token_type, pattern in token_patterns.items():
            regex = re.compile(pattern)
            match = regex.match(input_string, position)

            if match:
                token_value = match.group(0)
                if token_type == 'constant':  # Handling constants specifically
                    tokens.append(('CONSTANT', token_value))
                elif token_type == 'identifier':  # Identifiers
                    if token_value in keywords:
                        tokens.append(('KEYWORD', token_value))
                    else:
                        tokens.append(('IDENTIFIER', token_value))
                else:
                    tokens.append((token_type.upper(), token_value))
                position = match.end()
                break

        # If no match is found, print the unhandled character and raise an error
        if not match:
            print(f"Unmatched character at position {position}: {input_string[position]}")
            raise SyntaxError(f"Invalid character at position {position}")

    return tokens

# Input string for testing
input_string = input("Enter the string: ")

# Tokenize the input
try:
    tokens = tokenize(input_string)

    # Output the tokens
    for token in tokens:
        print(f"Token: {token[0]} | Value: {token[1]}")
except SyntaxError as e:
    print(e)