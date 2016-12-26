def square(x):
    '''
    input number and return result

    >>> square(2)
    4
    >>> square(7)
    49
    >>> square(10)
    100
    '''
    return x*x

if __name__ == '__main__':
    import doctest,doctest_test
    doctest.testmod(doctest_test)