"""
Refactor the given procedural code into an object-oriented design,
organizing the code into classes and methods.
"""

def read_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            fields = line.strip().split(',')
            data.append(fields)
    return data

def write_data(file_path, data):
    with open(file_path, 'w') as f:
        for item in data:
            line = ','.join(item)
            f.write(line + '\n')

def process_data(data):
    processed_data = []
    for item in data:
        # Some complex processing
        processed_item = [field.upper() for field in item]
        processed_data.append(processed_item)
    return processed_data

# Example usage
if __name__ == '__main__':
    print("Code Debugging[3] Data Processor")

    input_file = 'data/input.csv'
    output_file = 'data/output.csv'

    data = read_data(input_file)
    processed_data = process_data(data)
    write_data(output_file, processed_data)

    print("Data Processing Completed! Text should be converted to uppercase.")
    print(read_data(output_file))
