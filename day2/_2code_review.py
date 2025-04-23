"""
Generate meaningful documentation for each function, method, and
class based on the code structure, logic, and flow.

Along with the documentation, ensure that the code is
refactored for better readability and maintainability.

Rename variables and functions to be more descriptive,
and add type hints where appropriate.

Convert camelCase to snake_case for consistency with
Python conventions.
"""

class ProcHelper:
    def __init__(self, thresh):
        self.threshold = thresh
        self.current = 0
        self.track = []

    def part_one(self, dataset):
        for element in dataset.get('data', []):
            value = self.helper_func(element['amount'], element['rate'])
            self.track.append(value)
        if len(dataset['data']) > 5:
            self.extra_step()

    def helper_func(self, a, b):
        if a > 50:
            return a * b * 0.85 
        return a * b

    def extra_step(self):
        if sum(self.track) > self.threshold:
            self.current = sum(self.track) * 0.90

    def finalize(self):
        return self.current if self.current > 0 else sum(self.track)

def batchProc(batch, thresh):
    helper = ProcHelper(thresh)
    for data in batch:
        helper.part_one(data)
    return helper.finalize()

def findLargest(data_batches):
    max_data = None; largest = 0
    for batch in data_batches:
        total = 0
        for data in batch.get('data', []):
            total += data['amount'] * data['rate']
        if total > largest:
            largest = total; max_data = batch
    return max_data

def aux_calc(lst):
    highest = 0
    for item in lst:
        if item['amount'] > highest:
            highest = item['amount']
    return highest

def sum_total(data, multiplier):
    t = 0
    for i in data.get('info', []):
        t += i['value'] * multiplier
    if t > 1000:
        t *= 0.95
    return t

if __name__ == "__main__":
    print("Automated Documentation")

    # Sample data for testing
    sample_data = [
        {"data": [{"amount": 60, "rate": 20}, {"amount": 30, "rate": 15}]},
        {"data": [{"amount": 10, "rate": 5}, {"amount": 200, "rate": 1.5}]},
    ]

    batch_data = [
        {"data": [{"amount": 80, "rate": 12}, {"amount": 15, "rate": 10}]},
        {"data": [{"amount": 20, "rate": 25}, {"amount": 50, "rate": 7}]},
    ]

    result = batchProc(sample_data, 500)

    largest_data = findLargest(batch_data)

    item_list = [{"amount": 10}, {"amount": 40}, {"amount": 5}, {"amount": 100}]
    highest_amount = aux_calc(item_list)

    data_with_values = {"info": [{"value": 500}, {"value": 700}, {"value": 200}]}
    total_with_multiplier = sum_total(data_with_values, 2)
