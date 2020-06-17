'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    updated_arr = [0] * len(arr)
    # for every index in range 0 - length of array
    for i in range(0, len(arr)):
        # for every index save a copy of the array
        copy = arr.copy()
        # on each pass the index becomes 1 instead so 2 becomes 1 for example as if it's not there.
        copy[i] = 1
        # setting as placeholder of 1 so we can replace it as the product
        total = 1
        # for every value in the copied array
        for val in copy:
            # set the total to equal the product of each value in copied arr.
            total = total * val
        # update the array we made as the total
        updated_arr[i] = total
    # return updated array
    return updated_arr




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
