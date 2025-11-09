#!/usr/bin/env python3
import sys
import os

def load_stopwords(stopwords_file):
    stopwords = set()
    if os.path.exists(stopwords_file):
        with open(stopwords_file, 'r') as f:
            for line in f:
                word = line.strip().lower()
                if word:
                    stopwords.add(word)
    return stopwords

def remove_stopwords(sentence, stopwords):
    words = sentence.split()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return ' '.join(filtered_words)

def main():
    stopwords_file = None
    
    if len(sys.argv) > 1:
        stopwords_file = sys.argv[1]
    elif 'STOPWORDS_FILE' in os.environ:
        stopwords_file = os.environ['STOPWORDS_FILE']
    else:
        sys.stderr.write("Error: Stopwords file not provided. Use: python3 stopword_mapper.py <stopwords_file>\n")
        sys.exit(1)
    
    stopwords = load_stopwords(stopwords_file)
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        cleaned_sentence = remove_stopwords(line, stopwords)
        if cleaned_sentence:
            print(cleaned_sentence)

if __name__ == "__main__":
    main()




