from flask import Flask, jsonify, request, render_template
import unittest
from tests.test_google_page import TestCases
import io, os
import sys

app = Flask(__name__)

@app.route('/')
def index():
    test_cases = []
    for name in dir(TestCases):
        if name.startswith('test_'):
            test_cases.append(name)
    return render_template('index.html', test_cases=test_cases)

@app.route('/run_test_case', methods=['GET'])
def run_test_case():
    # Get the test case name from the query parameters
    test_case_name = request.args.get('name')
    
    # Dynamically create a test suite with the specified test case
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestCases(test_case_name))
    
    # Redirect stdout to an in-memory buffer
    stdout_buffer = io.StringIO()
    sys.stdout = stdout_buffer
    
    # Run the test suite and collect the results
    test_runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    test_result = test_runner.run(test_suite)
    
    # Capture the stdout output and reset it to its original value
    stdout_output = stdout_buffer.getvalue()
    sys.stdout = sys.__stdout__
    
    # Return a JSON response with the test results and output
    response = {
        'name': test_case_name,
        'result': test_result.wasSuccessful(),
        'output': stdout_output
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
