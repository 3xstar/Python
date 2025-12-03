def upper_case(func):
    def innerFunc(text):
        result = func(text.upper())
        return result

    return innerFunc


@upper_case
def message(text):
    print(text)


message("андрей")
