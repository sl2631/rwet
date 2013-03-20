# in this version we factored out the replacement functions created multiple synonyms values.

from __future__ import print_function
import sys
import re

f = sys.stdin

# later we can change this to be f = open('somefile.txt')

synonyms = {
	'tool' : 'foot',
	'hampton' : 'foot',
	'hamptons' : 'feet',
	'meat' : 'foot',
	'rig' : 'foot',
	'we' : 'your parents',
}


def replace_word_preserving_caps(word, replacement):
	if word.istitle(): # word is title-cased
		return replacement.capitalize() # original was capitalized, so cap result
	# TODO: implement all caps if necessary
	else:
		return replacement


def replace_synonyms(word):
	low = word.lower() # get the uncapped version
	try:
		replacement = synonyms[low]
		return replace_word_preserving_caps(word, replacement)
	except KeyError:
		return word


#def eat_vowels(s):
 #   return ''.join([c for c in s if c.lower() not in 'aeiou'])


# regex to split words; capture the non-word characters so that split will output both words and non-words interleaved.
word_split_re = re.compile(r'(\W+)')

for index, line in enumerate(f):
	line = line.strip()
	words = word_split_re.split(line)
	words = [replace_synonyms(w) for w in words]
	line = ''.join(words)
	#if True and index  == 2:
		# if False and index % 3 == 0:
		#line = eat_vowels(line)
	print(line)
