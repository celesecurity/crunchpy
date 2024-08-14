#!/usr/bin/env python3

import itertools
import sys


def generate_wordlist(min_length, max_length, charset, output_file):
    with open(output_file, 'w') as f:
        for length in range(min_length, max_length + 1):
            for word in itertools.product(charset, repeat=length):
                f.write(''.join(word) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python crunch_clone.py <min_length> <max_length> <charset> <output_file>")
        sys.exit(1)
    
    min_length = int(sys.argv[1])
    max_length = int(sys.argv[2])
    charset = sys.argv[3]
    output_file = sys.argv[4]

    generate_wordlist(min_length, max_length, charset, output_file)
    print(f"Wordlist generated and saved to {output_file}")
