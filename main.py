book_path = 'books/frankenstein.txt'
with open(book_path) as f:
    book = f.read()

words = book.split()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

chars = get_chars_dict(book)

letters = [(k,v) for k, v in sorted(chars.items(), key=lambda pair: pair[0]) if k.isalpha()]

book_rpt_str = f" --- Begin report of {book_path} --- \n"
book_rpt_str += f"The document had {len(words)} words in it. \n\n"

for i in range(len(letters)):
    each = letters[i]
    book_rpt_str += f"The '{each[0]}' character was found {each[1]} times \n"

book_rpt_str += "--- End of report ---"

print(book_rpt_str)