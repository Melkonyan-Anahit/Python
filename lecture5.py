def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        return sum(num for num in numbers if num >= 0)
    return sum(numbers)

def main():
    
    user_input = input("Enter a list of numbers separated by spaces (e.g., '1 2 3 -4 5'): ")
    
    numbers = list(map(int, user_input.split()))
    
    exclude_negatives = input("Do you want to exclude negative numbers? (yes/no): ").strip().lower()
    
    exclude_negative = exclude_negatives == 'yes'
    total_sum = sum_of_elements(numbers, exclude_negative=exclude_negative)
    
 
    print(f"The sum of the elements is: {total_sum}")

main()