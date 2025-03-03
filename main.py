from stats import get_num_words, get_chars_dict, sort_dictionary


def get_book_text(path) -> str:
    with open(path) as f:
        file_contents = f.read()
    return str(file_contents)


def main():
    text_content = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text_content)
    num_chars = get_chars_dict(text_content)
    report_stats = sort_dictionary(num_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for data in report_stats:
        character = data["character"]
        count = data["count"]
        if character.isalpha():
            print(f"{character}: {count}")
        continue

    print("============= END ===============")


if __name__ == "__main__":
    main()
