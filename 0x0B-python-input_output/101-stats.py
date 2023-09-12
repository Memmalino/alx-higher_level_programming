#!/usr/bin/python3
import sys
from collections import defaultdict

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 10:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_file_size += file_size
            status_code_counts[status_code] += 1

        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                if status_code_counts[code] > 0:
                    print(f"{code}: {status_code_counts[code]}")
            print()
except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

