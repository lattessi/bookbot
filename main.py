import sys

from stats import get_num_words, get_num_times_character, get_dictionary_of_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")

        sys.exit(1)

    else:
        book_path = sys.argv[1]

        text = get_book_text(book_path)
        number_of_words = get_num_words(text)
        character_in_words = get_num_times_character(text)
        dictionary_of_characters = get_dictionary_of_characters(character_in_words)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")

        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")

        print("--------- Character Count -------")

        for char_dict in dictionary_of_characters:
            char = next(iter(char_dict.keys()))
            count = next(iter(char_dict.values()))

            if char.isalpha():
                print(f"{char}: {count}")

        print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
