# Makefile to download Frankenstein text

# Target: load
# This will download the Frankenstein text file into the "books" directory

load:
	mkdir -p books
	wget -O books/frankenstein.txt https://www.gutenberg.org/cache/epub/41445/pg41445.txt
	wget -O books/mobydick.txt https://www.gutenberg.org/cache/epub/2701/pg2701.txt
	wget -O books/prideandprejudice.txt https://www.gutenberg.org/cache/epub/1342/pg1342.txt
# You can also add more targets here if needed, e.g., cleanup
clean:
	rm -rf books/frankenstein.txt
	rm -rf books/mobydick.txt 
	rm -rf books/prideandprejudice.txt



