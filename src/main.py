# src/main.py
from src.introduction import introduction
from src.findaverage import findaverage
from src.comparetoavg import comparetoavg

def main():
    introduction()
    """
    Repeats input loop 10 times and prints average and comparsion.
    """
    num_sets = 0

    while num_sets < 10:
        num1 = int(input('Enter the first integer: '))
        num2 = int(input('Enter the second integer: '))
        num3 = int(input('Enter the third integer: '))
        
        print()
        print('The three integers that you entered are',num1,',',num2,',',num3)

        #find the average of the set
        avg = findaverage(num1, num2, num3)
        print(f'The average is {avg:.3f}')
        print()

        #compare each number entered to the set average
        comparetoavg(num1, num2, num3, avg)
        print()
        num_sets += 1
        
    print('Total sets processed', num_sets)

if __name__ == "__main__":
    main()

