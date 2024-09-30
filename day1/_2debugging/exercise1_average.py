"""
Identify and fix the error in a function that
computes the average for a list of items
"""

def calculate_average(items):
    return sum(items) / len(items)

# Example usage
if __name__ == "__main__":
    print("Code Debugging[1] Average Calculator")

    average = calculate_average([])
    print(f"Empty list average: {average}")

    average = calculate_average([1, 2, 3, 4, 5])
    print(f"Average of [1, 2, 3, 4, 5]: {average}")

    average = calculate_average([10, '20', 'NaN'])
    print(f"Average of [10, '20', 'NaN']: {average}")
