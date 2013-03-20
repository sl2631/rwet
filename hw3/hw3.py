#!/usr/bin/env python

from __future__ import print_function
import nltk
import nltk.tokenize
import random
import sys
from pprint import pprint


text_path = 'kipling.txt'

text = open(text_path).read()
# both flat and nested will hold the entire poem
lines = [] # accumulate each line
for para in text.split('\n\n'):
  lines.extend([l for l in para.split('\n') if l]) # get rid of empty lines

def print_poem(label, lines):
  print('\n', label, ':', sep='')
  for l in lines:
    print(l)

print_poem('all', lines)

# list comprehension:
# iterate over lines, returning the line up to but not including the last character if the last character is in the punctuation set
lines_strip_end_punct = [l[:-1] if l[-1] in ",.:;!" else l for l in lines]

def gen_poem(n):
  # randomly pick n sentences from the poem
  sample = random.sample(lines_strip_end_punct, n)
  lines_with_punct = []
  for i, l in enumerate(sample):
    j = i + 1
    if j == n: # last line
      p = '!'
    elif j % (n / 4) == 0:
      p = ';'
    else:
      p = ','
    lines_with_punct.append(l + p)
  print_poem(n, lines_with_punct)

n = len(lines)
while n > 0:
  gen_poem(n)
  n /= 2
