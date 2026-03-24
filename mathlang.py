"""
MathLang Interpreter
A tiny language for math calculations using plain English words.
Examples:
    add three and five          -> 8
    subtract ten from twenty    -> 10
    multiply four by six        -> 24
    divide fifteen by three     -> 5
"""

# --- Number word mapping ---
NUMBER_WORDS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
    "hundred": 100
}

# --- Result word mapping ---
RESULT_WORDS = {v: k for k, v in NUMBER_WORDS.items()}


def words_to_number(tokens):
    """Convert a list of word tokens into an integer."""
    total = 0
    current = 0
    for token in tokens:
        if token not in NUMBER_WORDS:
            raise ValueError(f"Unknown number word: '{token}'")
        val = NUMBER_WORDS[token]
        if val == 100:
            if current == 0:
                current = 1
            current *= val
        elif val >= 20:
            current += val
        else:
            current += val
    total += current
    return total


def number_to_words(n):
    """Convert an integer result to an English word (for small numbers)."""
    if n in RESULT_WORDS:
        return RESULT_WORDS[n]
    # Handle compound numbers like 23 -> "twenty three"
    if 20 < n < 100:
        tens = (n // 10) * 10
        ones = n % 10
        if ones == 0:
            return RESULT_WORDS.get(tens, str(n))
        return f"{RESULT_WORDS.get(tens, str(tens))} {RESULT_WORDS.get(ones, str(ones))}"
    return str(n)


def parse_and_eval(expression):
    """
    Parse a MathLang expression and return (result_int, result_word).

    Grammar (BNF):
        <expr>   ::= <add_expr> | <sub_expr> | <mul_expr> | <div_expr>
        <add_expr> ::= "add" <number> "and" <number>
        <sub_expr> ::= "subtract" <number> "from" <number>
        <mul_expr> ::= "multiply" <number> "by" <number>
        <div_expr> ::= "divide" <number> "by" <number>
        <number>   ::= <word> { <word> }
    """
    tokens = expression.strip().lower().split()

    if not tokens:
        raise ValueError("Empty expression.")

    op = tokens[0]

    if op == "add":
        # add <A> and <B>
        if "and" not in tokens:
            raise ValueError("Expected 'and' in add expression. Example: add three and five")
        idx = tokens.index("and")
        a_tokens = tokens[1:idx]
        b_tokens = tokens[idx + 1:]
        a = words_to_number(a_tokens)
        b = words_to_number(b_tokens)
        result = a + b

    elif op == "subtract":
        # subtract <A> from <B>
        if "from" not in tokens:
            raise ValueError("Expected 'from' in subtract expression. Example: subtract three from ten")
        idx = tokens.index("from")
        a_tokens = tokens[1:idx]
        b_tokens = tokens[idx + 1:]
        a = words_to_number(a_tokens)
        b = words_to_number(b_tokens)
        result = b - a

    elif op == "multiply":
        # multiply <A> by <B>
        if "by" not in tokens:
            raise ValueError("Expected 'by' in multiply expression. Example: multiply four by five")
        idx = tokens.index("by")
        a_tokens = tokens[1:idx]
        b_tokens = tokens[idx + 1:]
        a = words_to_number(a_tokens)
        b = words_to_number(b_tokens)
        result = a * b

    elif op == "divide":
        # divide <A> by <B>
        if "by" not in tokens:
            raise ValueError("Expected 'by' in divide expression. Example: divide ten by two")
        idx = tokens.index("by")
        a_tokens = tokens[1:idx]
        b_tokens = tokens[idx + 1:]
        a = words_to_number(a_tokens)
        b = words_to_number(b_tokens)
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a // b  # Integer division for clean word results

    else:
        raise ValueError(
            f"Unknown operation: '{op}'. Supported: add, subtract, multiply, divide"
        )

    return result, number_to_words(result)


def run_repl():
    """Interactive Read-Eval-Print Loop for MathLang."""
    print("=== MathLang Interpreter ===")
    print("Type a math expression in plain English, or 'quit' to exit.")
    print("Examples:")
    print("  add three and five")
    print("  subtract four from twenty")
    print("  multiply six by seven")
    print("  divide fifteen by three")
    print()

    while True:
        try:
            user_input = input("MathLang> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            result_int, result_word = parse_and_eval(user_input)
            print(f"=> {result_word} ({result_int})")
        except ValueError as e:
            print(f"Error: {e}")

        print()


# --- Demo / test cases ---
def run_tests():
    test_cases = [
        ("add three and five", 8),
        ("add twenty and fifteen", 35),
        ("subtract four from ten", 6),
        ("subtract three from twenty", 17),
        ("multiply four by six", 24),
        ("multiply two by fifty", 100),
        ("divide fifteen by three", 5),
        ("divide twenty by four", 5),
    ]

    print("Running MathLang tests...\n")
    passed = 0
    for expr, expected in test_cases:
        result_int, result_word = parse_and_eval(expr)
        status = "PASS" if result_int == expected else "FAIL"
        print(f"[{status}] '{expr}' => {result_word} ({result_int})")
        if result_int == expected:
            passed += 1

    print(f"\n{passed}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        run_repl()