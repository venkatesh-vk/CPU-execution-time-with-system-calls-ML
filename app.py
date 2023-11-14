from flask import Flask, request, render_template
import subprocess
import re
import pandas as pd
import pickle 
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/submit', methods=['POST'])
def submit():
    s = request.form.get('code')
    # Save the Python code to a file
    with open("s.py", "w") as code_file:
        code_file.write(s)

    # Define the command to run strace on the Python script
    strace_command = "strace -o s.txt python3 s.py"

    # Run strace and capture system calls
    subprocess.run(strace_command, shell=True)

    # Clean up: remove the temporary Python script
    subprocess.run("rm s.py", shell=True)


    # Define the list of system calls you want to extract
    system_calls = [
        'getgid', 'getrandom', 'access', 'getdents64', 'fcntl', 'write',
        'getcwd', 'geteuid', 'execve', 'dup', 'mmap', 'prctl', 'gettid',
        'print', 'ioctl', 'openat', 'getuid', 'getegid', 'brk', 'pread64',
        'isSorted', 'futex', 'close', 'exit_group'
    ]

    # Initialize a dictionary to store the count of each system call
    call_counts = {call: [0] for call in system_calls}

    # Define the path to your strace output file
    strace_file = 's.txt'

    # Open and read the strace file
    with open(strace_file, 'r') as file:
        strace_content = file.read()

    # Use regular expressions to find and count system calls
    for call in system_calls:
        pattern = f'\\b{call}\\b'
        count = len(re.findall(pattern, strace_content))
        call_counts[call] = [count]

    df = pd.DataFrame(call_counts) 

    print(df)
    with open('CPU_exe_model.pkl', 'rb') as file:
        stacked_model = pickle.load(file)

    stacked_predictions = stacked_model.predict(df)
    print(stacked_predictions)
    return render_template('preview.html',msg = 'The CPU Execution time is {} seconds'.format(stacked_predictions[0]))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
    # app.run(debug=True)
