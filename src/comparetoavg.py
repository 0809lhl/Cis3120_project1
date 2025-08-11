# src comparetoavg.py

def comparetoavg(a, b, c, avg):
    """
    Prints whether each number is below, equal to, or above the average.
    """
    for num in [a, b, c]:
        if num < avg:
            print(f'{num} is less than the average {avg}')
        elif num > avg:
            print(f'{num} is greater than the average {avg}')
        else:
            print(f'{num} is equal to the average {avg}')


