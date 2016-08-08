# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate_letter(letter, n):
	# Rotate a letter by n places. Does not chage other characters.
	# letter: single-letter string
	# n: integer
	# return: single-letter string
	if letter.isupper():
		start = ord('A')
	elif letter.islower():
		start = ord('a')
	else:
		return letter

	c = ord(letter) - start
	i = (c + n) % 26 + start
	return chr(i)

def rotate_word(word, n):
	# Rotate a word by n place.
	# word: string
	# n: integer
	# return: rotated string

	replacement = ""
	for letter in word:
		replacement = replacement + rotate_letter(letter, n)
	return replacement

if __name__ == "__main__":
	print(rotate_word('cheer', 7))
	print(rotate_word('melon', -10))

