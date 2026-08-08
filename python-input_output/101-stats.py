#!/usr/bin/python3
"""Script that reads stdin log lines and prints running statistics."""
import sys

total_size = 0
status_counts = {}
line_count = 0


def print_stats():
    """Print the accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue

        status_code = parts[-2]
        file_size = parts[-1]

        try:
            file_size = int(file_size)
        except ValueError:
            continue

        if status_code not in ["200", "301", "400", "401",
                                "403", "404", "405", "500"]:
            continue

        total_size += file_size
        status_counts[status_code] = status_counts.get(status_code, 0) + 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
