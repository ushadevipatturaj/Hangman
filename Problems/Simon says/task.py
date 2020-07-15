def what_to_do(instructions):
    index_simon = instructions.find('Simon says')
    if instructions.startswith('Simon says'):
         return "I " + instructions[index_simon + 11:len(instructions)]
    elif instructions.endswith('Simon says'):
        print_str = "I " + instructions[:index_simon - 1]
        return print_str.strip('')
    else:
        return "I won't do it!"