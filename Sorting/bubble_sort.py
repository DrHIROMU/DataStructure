# Time Complexity: O(n^2)

def bubble_sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(0, i, 1):        
            if numbers[j] > numbers[j+1]:
                swap(numbers, j, j+1)
    return numbers

def swap(num_array, index_a, index_b):
    temp = num_array[index_a]
    num_array[index_a] = num_array[index_b]
    num_array[index_b] = temp

def main():
    nums = [3,4,8,2,1]
    sorted_numbers = bubble_sort(nums)
    print(sorted_numbers)

if __name__ == '__main__':
    main()