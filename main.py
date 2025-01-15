def number_of_words(s):
    return len(s.split())

def character_counts(s):
    counts = {}
    for ch in s:
        ch = ch.lower()
        if not ch in counts:
            counts[ch] = 0
        counts[ch] += 1
    return counts

def main():
    book_file_path = "books/frankenstein.txt"
    with open(book_file_path) as f:
        file_contents = f.read()
        word_count = number_of_words(file_contents)
        character_count = character_counts(file_contents)

        letter_count = []
        for ch in character_count:
            if ch.isalpha():
                letter_count.append((character_count[ch], ch))
        letter_count.sort(reverse=True)

        print(f"--- Begin report of {book_file_path} ---")
        print(f"{word_count} words found in the document")
        print()
        for (count, ch) in letter_count:
            print(f"The '{ch}' character was found {count} times")
        print("--- End report ---")

if __name__ == "__main__":
    main()