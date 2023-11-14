import os
import re
from collections import Counter
import csv

# Directory containing STRACE output files
strace_directory = "STRACE"

# Directory containing TIME output files
time_directory = "TIME"

# Output CSV file for system calls
system_calls_csv = "system_calls2.csv"

# Output CSV file for CPU times
cpu_times_csv = "cpu_times2.csv"

# Function to extract system call names and their counts from a line
def extract_system_calls(line):
    # Use regular expression to match system calls
    system_calls = re.findall(r'(\w+)\(', line)
    return system_calls

# Process STRACE files and extract system call counts
system_call_counts = {}
for filename in os.listdir(strace_directory):
    if filename.endswith(".txt"):
        # Extract the program name without the extension
        program_name = os.path.splitext(filename)[0]
        file_path = os.path.join(strace_directory, filename)
        with open(file_path, "r") as file:
            lines = file.readlines()
            # Extract and count system calls from each line
            calls = [call for line in lines for call in extract_system_calls(line)]
            system_call_counts[program_name] = dict(Counter(calls))

# Write system call counts to a CSV file
with open(system_calls_csv, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header row
    header = ["File"] + list(set(call for calls in system_call_counts.values() for call in calls))
    csvwriter.writerow(header)

    # Write data rows
    for filename, call_counts in system_call_counts.items():
        row = [filename]
        for header_item in header[1:]:
            row.append(call_counts.get(header_item, 0))
        csvwriter.writerow(row)

print(f"System call counts saved to {system_calls_csv}")

# Process TIME files and extract CPU times
cpu_times = {}
for filename in os.listdir(time_directory):
    if filename.endswith(".txt"):
        # Extract the program name without the extension
        program_name = os.path.splitext(filename)[0]
        file_path = os.path.join(time_directory, filename)
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("CPU exe :"):
                    time_value = float(line.split(":")[1].strip().split()[0])
                    cpu_times[program_name] = time_value

# Write CPU times to a CSV file
with open(cpu_times_csv, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["File", "CPU Time (seconds)"])
    for filename, time_value in cpu_times.items():
        csvwriter.writerow([filename, time_value])

print(f"CPU times saved to {cpu_times_csv}")
