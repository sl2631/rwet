#!/usr/bin/env python

from __future__ import print_function
import nltk
import nltk.tokenize
import random
import sys
from pprint import pprint


text_path = 'kipling.txt'
sample_size = int(sys.argv[1]) # first argument is sample size

text = open(text_path).read()
# both flat and nested will hold the entire poem
flat = [] # accumulate each line
nested = [] # accumulate nested line structure
for para in text.split('\n\n'):
  lines = [l for l in para.split('\n') if l] # get rid of empty lines
  flat.extend(lines)
  nested.append(lines)

# convert nested list structure into a deeper (binary) tree
# the tree must have elements that are only powers of two
def make_binary_tree(node):
  if isinstance(node, list): # otherwise node is a string (leaf of the tree); do nothing
    l = len(node)
    assert l % 2 == 0 # insist that branch nodes are powers of two
    if l > 2:
      h = l / 2 # half length; int division rounds down
      assert h % 2 == 0 # again, insist that the node is perfectly divisible
      # create two new nodes, low and high half of existing node
      # if either of the new nodes would have a single element only, then just return a leaf/string.
      a = node[:h]
      b = node[h:]
      node[:] = [a, b] # replace the node's contents with the two halves
    assert len(node) == 2
    make_binary_tree(node[0])
    make_binary_tree(node[1])

def print_label(label, obj):
  print('\n', label, ':', sep='')
  pprint(obj)

print_label('flat', flat)
print_label('nested', nested)
make_binary_tree(nested)
print_label('binary nested', nested)

# randomly pick n sentences from the flat array
sample_indices = random.sample(range(len(flat)), sample_size)
sampled = ['{:05b} {}'.format(i, flat[i]) for i in sample_indices]
make_binary_tree(sampled) # give the sampled poem binary structure
print_label('sampled', sampled)

def print_rec(node, depth, indented):
  if not indented:
    print(' ' * depth, end='')
  if isinstance(node, list):
    print('•', end='')
    for i, child in enumerate(node):
      print_rec(child, depth + 1, (i == 0))
  else:
    print(' ', node, sep='')



sys.exit()
