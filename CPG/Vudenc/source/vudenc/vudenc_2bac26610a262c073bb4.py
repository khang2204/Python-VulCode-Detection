def _is_english_text(text):...
"""docstring"""
avg_word_length = 2.55 + 1
expected_word_number = float(len(text)) / avg_word_length
words = [word for word in re.split('\\W', text) if word.isalpha()]
word_number = len(words)
return word_number > expected_word_number
