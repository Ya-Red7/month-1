



# Write a function that sums numbers in a list.
def sumOfNums(arr):
    return sum(arr)


# Print even numbers between 1 and 20 using a loop.
def evenNumFinder():
    for num in range(1,20+1):
        if num%2 == 0:
            print(num)


# Write a program to find the largest number in a list.
def largestNUm(arr):
    return max(arr)


if __name__ == "__main__":
    nums = [1,2,3,4,5]

    print(sumOfNums(nums))
    evenNumFinder()
    print(largestNUm(nums))