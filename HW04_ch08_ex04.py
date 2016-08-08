#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
       It returns True or False based on the first character (missing checking for the others).
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
       It doesn't check for any lowercase letters at all since string 'c' is always lower, so 
       always True.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
       For each iteration, the previous checking result is overwritten by the latter one, essentially
       we are just checking the last character in the string.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
       This function is right, once it encounters a lowercase character, the flag variable will always
       contains boolean value of True.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
       As long as there is one uppercase character in the string, it will always return False.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1('Abcdelowercaseeversince'))
    print(any_lowercase2('ALL UPPERCASE BUT STILL RETURN TRUE ALWAYS'))
    print(any_lowercase3('AaBbCcDd'))
    print(any_lowercase4('ABcD'))
    print(any_lowercase5('aaBcde'))


if __name__ == '__main__':
    main()
