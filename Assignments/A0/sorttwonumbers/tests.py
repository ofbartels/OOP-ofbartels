import subprocess
import os


def run_test(input_file, expected_output_file):

    with open(input_file, 'r') as infile, open(expected_output_file,
                                               'r')as outfile:
        expected_output = outfile.read().strip()
        input_data = infile.read()
        process = subprocess.run(['python', 'sorttwonumbers.py'],
                                 input=input_data,
                                 capture_output=True, text=True)
        actual_output = process.stdout.strip()
        print(f"Expected: {expected_output}, Actual: {actual_output}")
        return actual_output == expected_output


# Directory where the test files are stored
test_directory = os.path.join(os.getcwd(), 'data')

# Assuming test files are named like 1.in, 1.ans, 2.in, 2.ans, etc.
test_count = 1  # Start with test file 1

while True:
    input_file = os.path.join(test_directory, f'{test_count}.in')
    output_file = os.path.join(test_directory, f'{test_count}.ans')

    # Check if both input and output test files exist
    if not os.path.exists(input_file) or not os.path.exists(output_file):
        break  # Exit the loop if a test file is missing

    if run_test(input_file, output_file):
        print(f"Test {test_count} Passed")
    else:
        print(f"Test {test_count} Failed")

    test_count += 1
