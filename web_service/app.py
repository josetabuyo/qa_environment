from flask import Flask, jsonify, request, render_template
import unittest

import io, os, inspect, sys

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.google.test_google_page import test_google_page
from tests.other.test_dummy import test_dummy

from rpa.RpaJobs import RpaJobs


app = Flask(__name__)

@app.route('/')
def index():
    
    
    test_google_page_cases = []
    for name in dir(test_google_page):
        if name.startswith('test_'):
            method = getattr(test_google_page, name)
            test_google_page_cases.append({
                'class':'test_google_page',
                'name': name,
                'doc': method.__doc__
            })
            #inspect.signature(method)


    test_dummy_cases = []
    for name in dir(test_dummy):
        if name.startswith('test_'):
            method = getattr(test_dummy, name)
            test_dummy_cases.append({
                'class':'test_dummy',
                'name': name,
                'doc': method.__doc__
            })
    
    
    test_cases = {
        "test_google_page_cases": test_google_page_cases,
        "test_dummy_cases": test_dummy_cases
    }

    rpa_jobs = []
    for name in dir(RpaJobs):
        if name.startswith('rpa_'):
            method = getattr(RpaJobs, name)
            rpa_jobs.append({
                'name': name,
                'doc': method.__doc__
            })

    
    return render_template('index.html', test_cases=test_cases, rpa_jobs=rpa_jobs)
    
@app.route('/run_test_case', methods=['GET'])
def run_test_case():
    # Get the test case name from the query parameters
    test_class = request.args.get('class')
    test_case_name = request.args.get('name')
    
    # Dynamically create a test suite with the specified test case
    test_suite = unittest.TestSuite()

    if test_class == 'test_dummy':
        test_suite.addTest(test_dummy(test_case_name))
    elif test_class == 'test_google_page':
        test_suite.addTest(test_google_page(test_case_name))
    
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
    results = {
        'name': test_case_name,
        'result': test_result.wasSuccessful(),
        'output': stdout_output
    }
    
    
    return render_template('automation_results.html', results=results)

    # return jsonify(response)


@app.route('/run_rpa', methods=['GET'])
def run_rpa():
    rpa_name = request.args.get('name')
    

    method = getattr(RpaJobs(), rpa_name)
    
    # Redirect stdout to an in-memory buffer
    stdout_buffer = io.StringIO()
    sys.stdout = stdout_buffer
    
    method()

    # Capture the stdout output and reset it to its original value
    stdout_output = stdout_buffer.getvalue()
    sys.stdout = sys.__stdout__
    

    # Return a JSON response with the test results and output
    response = {
        'name': rpa_name,
        'output': stdout_output
    }
    
    return render_template('automation_results.html', results=response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8089)))
