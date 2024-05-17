def main():
    book_path = "/home/zoloni/workspace/github.com/ZoloniChase/boobot/books/frankenstein.txt"
    text = get_book_text(book_path)
    sentence = text.lower()
    letter_counts = {}
    for letter in sentence:
        if letter != " ":  # Exclude spaces
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    print("--- Begin report of books/frankenstein.txt ---")
    new = text.split()
    total = len(new)
    print(f"{total} words was found in the document")

    # Print the results
    for letter, count in letter_counts.items():
        
        print(f"The letter'{letter}': was found {count} times.")
    print("--- End report  please---")
 

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
