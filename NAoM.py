from typing import Tuple

# EXCEPTIONS
class InvalidAlgorithmOperator(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else: self.message = None
    def __str__(self):
        return f"Invalid algorithm of Markov's operator. It must be '->' or '->.' ."

class InvalidSubstringArgument(Exception):
    def __init__(self, *args):
        if args:
            self.character = args[0]
        else: self.character = None
    def __str__(self):
        if self.args:
            return f"Invalid substring for rule. '{self.character}' has character that is not in alphabet."
        else:
            return f"Invalid substring for rule. Characters must be in alphabet"
        
class EmptyRulesList(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else: self.message = None
    def __str__(self):
        return f"Rule's list is empty. Can't start processing."

# NEED POSITION TO REPLACE OR INSERT?

# CUSTOM TYPE 
class Rule:
    def __init__(self, input: str, operator: str, output: str):
        self.input = input
        self.operator = operator
        self.output = output
        self.check_rule_operator()

    def check_rule_operator(self):
        valid_operators = ['->', '->.']
        # Checking the validity of the rule's operator
        if self.operator not in valid_operators:
            raise InvalidAlgorithmOperator
        
# ALGORITHM CLASS
class NAoM:
    def __init__(self, alph: list):
        self.alph = alph + ['->', '->.']
        self.rules = []
    
    def processing(self, string: str, show_process: bool = True) -> str:
        if len(self.rules) == 0: raise EmptyRulesList
        print(f'''Processing string "{string}":''')
        log = ""
        main_process_state = True
        while main_process_state:
            old_string = string
            # Checking all the rules
            for rule in self.rules:
                breaked = False
                # If found occurrence
                if rule.input in string:
                    if rule.operator == '->':
                        string = string.replace(rule.input, rule.output, 1)
                        breaked = True
                        break # need to start reviewing the rules again
                    elif rule.operator == '->.':
                        string = string.replace(rule.input, rule.output, 1)
                        main_process_state = False
                        break
            if show_process: 
                print(old_string+rule.operator+string)
                log += old_string+rule.operator+string+'\n'
            if not breaked:
                main_process_state = False # Stop if we haven't found an occurrence
        if show_process:
            return log
        return string

    # RULES MANIPULATING
    def add_rule(self, input: str, operator: str, output: str):
        rule = Rule(input,operator,output)
        self.check_rule_substrings(rule)
        self.rules.append(rule)
    
    def delete_rule(self, position: int):
        self.rules.remove(self.rules[position])

    def clear_rules(self):
        self.rules.clear()

    def replace_rule(self, input: str, operator: str, output: str, position: int):
        rule = Rule(input,operator,output)
        self.check_rule_substrings(rule)
        self.rules[position] = rule

    def insert_rule(self, input: str, operator: str, output: str, position: int):
        rule = Rule(input,operator,output)
        self.check_rule_substrings(rule)
        self.rules.insert(position, rule)

    def show_rules(self):
        print('Rules:')
        print('--------------')
        for rule in self.rules:
            print(rule.input + rule.operator + rule.output)
        print('--------------')

    def check_rule_substrings(self, rule: Rule):
        # Checking the validity of the rule's substring
        if list(set(rule.input) & set(self.alph)) != list(set(rule.input)):
            raise InvalidSubstringArgument(rule.input)
        elif list(set(rule.output) & set(self.alph)) != list(set(rule.output)):
            raise InvalidSubstringArgument(rule.output)

    # Alphabet manipulating
    def show_alph(self):
        print(f"Alphabet: "+', '.join(self.alph))