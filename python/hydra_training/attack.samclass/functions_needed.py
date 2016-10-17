
def list2string(a_list):
    """Given a list, it concatenates all the elements into a string."""

    the_string = ''
    for elem in a_list:
        the_string += str(elem)
    return the_string
