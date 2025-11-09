#!/usr/bin/env python3
import sys

def main():
    word_sentences = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            word, sentence_id = line.split('\t')
            if word not in word_sentences:
                word_sentences[word] = []
            if sentence_id not in word_sentences[word]:
                word_sentences[word].append(sentence_id)
        except (ValueError, IndexError):
            continue
    
    sorted_words = sorted(word_sentences.items(), key=lambda x: x[0])
    
    for word, sentence_ids in sorted_words:
        sentence_ids_str = ', '.join(sentence_ids)
        print(f"{word}\t[{sentence_ids_str}]")

if __name__ == "__main__":
    main()




