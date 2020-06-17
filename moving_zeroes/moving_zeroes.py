'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # counts 0's in the array
	count = arr.count(0)
    # for every index in range of 0 to the amount of 0's we have
	for i in range(0, count):
        # remove the 0 and then append it aka putting it on the end
		arr.remove(0)
		arr.append(0)
    # return the array
	return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")