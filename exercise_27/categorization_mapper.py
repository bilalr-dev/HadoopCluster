#!/usr/bin/env python3
import sys
import os
import re

def parse_rule(rule_line):
    rule_line = rule_line.strip()
    if not rule_line:
        return None
    
    parts = rule_line.split('->')
    if len(parts) != 2:
        return None
    
    conditions = parts[0].strip()
    category = parts[1].strip()
    
    gender_match = re.search(r'Gender=([MF])', conditions)
    year_match = re.search(r'YearOfBirth=(\d+)', conditions)
    
    if not gender_match or not year_match:
        return None
    
    gender = gender_match.group(1)
    year = year_match.group(1)
    
    return {
        'gender': gender,
        'year': year,
        'category': category
    }

def load_rules(rules_file):
    rules = []
    if os.path.exists(rules_file):
        with open(rules_file, 'r') as f:
            for line in f:
                rule = parse_rule(line)
                if rule:
                    rules.append(rule)
    return rules

def match_user_to_category(user_record, rules):
    parts = user_record.split(',')
    if len(parts) != 7:
        return "Unknown"
    
    user_id = parts[0].strip()
    name = parts[1].strip()
    surname = parts[2].strip()
    gender = parts[3].strip()
    year_of_birth = parts[4].strip()
    city = parts[5].strip()
    education = parts[6].strip()
    
    for rule in rules:
        if rule['gender'] == gender and rule['year'] == year_of_birth:
            return rule['category']
    
    return "Unknown"

def main():
    rules_file = None
    
    if len(sys.argv) > 1:
        rules_file = sys.argv[1]
    elif 'RULES_FILE' in os.environ:
        rules_file = os.environ['RULES_FILE']
    else:
        sys.stderr.write("Error: Rules file not provided. Use: python3 categorization_mapper.py <rules_file>\n")
        sys.exit(1)
    
    rules = load_rules(rules_file)
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        category = match_user_to_category(line, rules)
        print(f"{line},{category}")

if __name__ == "__main__":
    main()


