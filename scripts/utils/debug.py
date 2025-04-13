def devlog(line: str):
	"""
	Output information in console in a uniform way.

	Example:
		devlog("no files are locked")
		devlog(f"There are {len(flashcards)} flashcards.")
	"""
	print(f"DEBUG ### {line} ################################")