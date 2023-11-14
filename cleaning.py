import pandas as pd

df = pd.read_csv('system_calls2.csv')

# List of columns to remove
columns_to_remove = [
    'rfind', 'str', 'lit', 'rob', 'sum', 'DivisibleByThree', 'svRead', 'insertionSort',
    'rt_sigaction', 'log', 'mremap', 'mprotect', 'factorial', 'map', 'fib', '_occr_element',
    'int', 'pop', 'tprint', 'lay', '346z', 'it', 'rseq', 'rint', 'nreverse_a_string',
    'csvRead', 'main', 'st', 'lseek', 'arch_prctl', 'read', 'sysinfo', 'findEquilibrium',
    'auth', 'firstRepeatedChar', 'sendmmsg', 'if_nametoindex', '217', 'len', 'join',
    'nprint', 'nscan_network', '334', 'list', 'eckGreater', 'munmap', 'getsockname',
    'lper', 'login', 'argumentParser', '323', 'makedev', 'divide', 'myFunction', 'peek',
    'd', 'newfstatat', 't', 'inet_pton', 'recvfrom', 'swapPositions', 'RemoveDuplicate',
    'arySearch', 'add', 'inet_addr', 'shellSort', 'set_tid_address', 'set_robust_list',
    'readlink', 'mirror', 'input', 'htonl', 'ndmail', 'rd', 'prlimit64', 'count_alphabets',
    'tMissingPositive', 'epoll_create1', '202', 'getpeername', 'checkPrime'
]

# Remove the specified columns
df = df.drop(columns=columns_to_remove, errors='ignore')

# Save the modified DataFrame back to a new CSV file
df.to_csv('SCE2.csv', index=False)