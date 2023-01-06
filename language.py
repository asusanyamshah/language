digits = "0123456789"

tt_int = 'tt_int'
tt_float = 'float'
tt_plus = 'plus'
tt_minus = 'minus'
tt_mul = 'mul'
tt_div = 'div'
tt_lparen = 'lparen'
tt_rparen = 'rparen'
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    def __repr__(self):
        if self.value: return f"{self.type}:{self.value}"
        return f"{self.type}"

class Error:
    def __init__(self, error, details):
        self.error = error
        self.details = details
    def as_string(self):
        result = f"{self.error}: {self.details}"
        return result

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_character = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_character = self.text[self.pos] if self.pos < len(self.text) else None 

    def generate_tokens(self):
        tokens = []
        while self.current_character!= None:
            if self.current_character in " \t":
                self.advance()
            elif self.current_character in digits:
                tokens.append(self.make_number())
            elif self.current_character == "+":
                tokens.append(Token(tt_plus))
                self.advance()
            elif self.current_character == "-":
                tokens.append(Token(tt_minus))
                self.advance()
            elif self.current_character == "*":
                tokens.append(Token(tt_mul))
                self.advance()
            elif self.current_character == "/":
                tokens.append(Token(tt_div))
                self.advance()
            elif self.current_character == "(":
                tokens.append(Token(tt_plus))
                self.advance()
            elif self.current_character == ")":
                tokens.append(Token(tt_rparen))
                self.advance()
            else:
                pass

        return tokens

    def make_number(self):
        num_instr = ''
        dots = 0

        while self.current_character != None and self.current_character in digits + '.':
            if self.current_character == '.':
                if self.dots == 1:
                    break
                dots += 1
                num_instr += '.'
            else:
                num_instr = self.current_character

        if dots == 0:
            return Token(tt_int, int(num_instr))
        else:
            return Token(tt_float, float(num_instr))
