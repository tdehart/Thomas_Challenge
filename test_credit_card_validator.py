import subprocess

def run_test():
    # Define the input and expected output
    test_input = """6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
"""
    expected_output = """Valid
Valid
Invalid
Valid
Invalid
Invalid
"""
    
    # Run the main script with the test input
    process = subprocess.Popen(
        ['python3', 'credit_card_validator.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate(input=test_input.encode())
    
    # Decode the output and compare with the expected output
    output = stdout.decode()
    assert output == expected_output, f"Expected: {expected_output}\nGot: {output}"
    
    print("All tests passed!")

if __name__ == "__main__":
    run_test()
