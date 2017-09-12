def percent_to_gpv(mark):
    '''(int) -> float
    Return the Grade Point Value of given percentage mark.
    REQ: mark >= 0
    REQ: mark <= 100
    >>> percent_to_gpv(0)
    0.0
    >>> percent_to_gpv(59)
    1.3
    >>> percent_to_gpv(70)
    2.7
    >>> percent_to_gpv(100)
    4.0
    >>> percent_to_gpv(95)
    4.0
    '''
    # Check conditions and store appropriate GPV
    if (mark >= 86):
        gpv = 4.0
    elif (mark >= 80 and mark < 85):
        gpv = 3.7
    elif (mark >= 77 and mark < 80):
        gpv = 3.3
    elif (mark >= 73 and mark < 77):
        gpv = 3.0
    elif (mark >= 70 and mark < 73):
        gpv = 2.7
    elif (mark >= 67 and mark < 70):
        gpv = 2.3
    elif (mark >= 63 and mark < 67):
        gpv = 2.0
    elif (mark >= 60 and mark < 63):
        gpv = 1.7
    elif (mark >= 57 and mark < 60):
        gpv = 1.3
    elif (mark >= 53 and mark < 57):
        gpv = 1.0
    elif (mark >= 50 and mark < 53):
        gpv = 0.7
    else:
        gpv = 0.0

    # Return grade point value
    return gpv
