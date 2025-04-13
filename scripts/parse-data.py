import utils.debug as debug
import utils.files as files
 
debug.devlog("get lines from file")
lines = files.get_lines_from_file("../data/flashcards.txt")

for i, line in enumerate(lines, 1):
    print(f"{i:03d}: {line}")