import operator

ops = ['+', '-', '*', '/']
op_mask = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calc(op, item1=0, item2=0):
    return op_mask[op](int(item1), int(item2))

def is_operator(ch):
    return ch in ops

def next_operator(string):
    for c in string:
        if is_operator(c):
            return c
    return False

def previous_operator(string):
    reversed_string = string[::-1]
    return next_operator(reversed_string)

def is_minus_sign(string):
    return string.count('-') == 1 and string.index('-') == 0

def still_operators(string):
    for operation in ops:
        if string.count(operation) > 0 and not (operation == '-' and is_minus_sign(string)):
            return True
    return False

def get_terms(string, position):
    # -- Split the string in two parts by the operator --
    string_item1 = string[:position]
    string_item2 = string[position + 1:]

    # -- Looking for size of the first term --
    previous_operation = previous_operator(string_item1)
    if previous_operation:
        item1 = string_item1.split(previous_operation)[-1]

        # -- If previous operator is "-" we assume is the sign of the number and we add it --
        if previous_operation == '-' and is_minus_sign(string_item1):
            item1 = '-' + item1
    else:
        item1 = string_item1

    # -- Looking for size of the second term --
    next_operation = next_operator(string_item2)
    if next_operation:
        item2 = string_item2[0:string_item2.index(next_operation)]
    else:
        item2 = string_item2

    return (item1, item2, next_operation)


def normalize(line):
    result = ''
    line = ''.join(line.split())

    # -- If line starts with (-) or (+) we keep this for the result --
    if line[0] in ['+', '-']:
        result = line[0]
        line = line[1:]

    subline = line
    list_operations = []
    while next_operator(subline):
        operation = next_operator(subline)
        position = subline.index(operation)
        subline = subline[position + 1:]
        list_operations.append(operation)

    subline = line
    for operation in ops:
        subline = subline.replace(operation, '#')
    list_words = subline.split('#')

    for position in range(len(list_words)):
        word = list_words[position].strip()
        try:
            int(word)
        except ValueError:
            print('Unable to parse word: ' + word)

        result += word
        if position < len(list_operations):
            result += list_operations[position]

    return result

def run(string):
    string = normalize(string)
    assert string[0] not in ['*', '/'], 'Error: Operator(* or /) can\'t be at the beginning of the instruction'

    # -- Until we don't find more operators in the string we keep looping --
    result = 0
    while still_operators(string):

        operation = next_operator(string)
        position = string.index(operation)

        # -- Avoiding (-) symbol at the beginning --
        if operation == '-' and position == 0:
            substring = string[1:]
            operation = next_operator(substring)

            if not operation:
                break

            subposition = substring.index(operation)
            position += subposition + 1

        # -- Getting terms involve in the operation --
        (item1, item2, next_operation) = get_terms(string, position)
        string = string[position + len(item2) + 1:]

        # -- If current operation is + or - and next operation is / or *
        # -- the second one has preference over the first one. Otherwise we just calculate --
        if next_operation and operation in ['+', '-'] and next_operation in ['/', '*']:
            (_, item3, _) = get_terms(string, 0)
            item2 = calc(next_operation, item2, item3)
            string = str(item1) + operation + str(item2) + string[len(item3) + 1:]
        else:
            result = calc(operation, item1, item2)
            string = str(result) + string

    return int(result)



if __name__ == '__main__':
    inp = input('Enter your calculation request:\n')
    print(run(inp))
