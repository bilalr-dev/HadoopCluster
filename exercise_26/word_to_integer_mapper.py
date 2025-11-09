#!/usr/bin/env python3
import sys
import os

def load_dictionary(dictionary_file):
    word_to_int = {}
    if os.path.exists(dictionary_file):
        with open(dictionary_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('\t')
                if len(parts) == 2:
                    word = parts[0].strip()
                    integer = parts[1].strip()
                    word_to_int[word] = integer
    return word_to_int

def main():
    dictionary_file = None
    
    if len(sys.argv) > 1:
        dictionary_file = sys.argv[1]
    elif 'DICTIONARY_FILE' in os.environ:
        dictionary_file = os.environ['DICTIONARY_FILE']
    else:
        sys.stderr.write("Error: Dictionary file not provided. Use: python3 word_to_integer_mapper.py <dictionary_file>\n")
        sys.exit(1)
    
    dictionary = load_dictionary(dictionary_file)
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            print()
            continue
        
        words = line.split()
        converted_words = []
        
        for word in words:
            if word in dictionary:
                converted_words.append(dictionary[word])
            else:
                converted_words.append(word)
        
        print(' '.join(converted_words))

if __name__ == "__main__":
    main()

