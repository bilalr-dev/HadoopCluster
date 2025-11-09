#!/usr/bin/env python3
import sys

def main():
    current_question_id = None
    question_text = None
    answers = []
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            parts = line.split('\t')
            if len(parts) < 3:
                continue
            
            question_id = parts[0]
            record_type = parts[1]
            
            if question_id != current_question_id:
                if current_question_id is not None and question_text:
                    for answer_id, answer_text in answers:
                        print(f"{current_question_id},{question_text},{answer_id},{answer_text}")
                
                current_question_id = question_id
                question_text = None
                answers = []
            
            if record_type == "Q":
                question_text = parts[2]
            elif record_type == "A":
                answer_id = parts[2]
                answer_text = parts[3]
                answers.append((answer_id, answer_text))
        except (ValueError, IndexError):
            continue
    
    if current_question_id is not None and question_text:
        for answer_id, answer_text in answers:
            print(f"{current_question_id},{question_text},{answer_id},{answer_text}")

if __name__ == "__main__":
    main()


