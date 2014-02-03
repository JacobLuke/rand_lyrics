from __future__ import print_function


from urllib2 import urlopen, HTTPError

from collections import defaultdict

import random
import re

from time import sleep

#handling unicode in both PY2 and PY3
import sys

if sys.version_info >= (3,):
  chr_func = chr
else:
  chr_func = unichr


def getRandomPage():
  while True:
    try:
      page = urlopen('http://lyrics.wikia.com/Special:Random')
      content = page.read()
      page.close()
      return content
    except HTTPError as e:
      print("Encountered exception:", e, file=sys.stderr)
      sleep(100)


def parseLyrics(content):
  
  #abuse the hell out of the page structure
  index = content.find("class='lyricbox'")
  i1 = content.find('</div>', index) + len('</div>')
  i2 = content.find('<!--', index)
  
  #now for the PITA processing
  #lyrics-wiki obfuscates lyrics by putting them in untranslated UTF8
  #so unobfuscate them

  lines = content[i1:i2].split('<br />')
  
  lines_translated = [''.join(chr_func(int(c[:-1])) for c in line.split('&#') if c[:-1].isdigit()).strip() for line in lines if line]

  return lines_translated

#get rid of the broken lyrics using a simple heuristic
def validLyrics(lyrics):
  for line in lyrics:
    if re.search('[a-z][A-Z]', line):
      return False
  return True

def getRandomLyrics():
  page = getRandomPage()
  return parseLyrics(page)

def generateMarkov(n=10):
  path = defaultdict(list)
  total_len = 0
  starts = []
  for i in range(n):
    print("\rRetrieving lyrics {0} of {1} ({2}%)".format(i+1, n, i*100/n), end='', file=sys.stderr)
    while True:
      lyrics = getRandomLyrics()
      if lyrics and validLyrics(lyrics):
        break
    total_len += len(lyrics)
    for line in lyrics:
      words = line.strip().split()
      if not words: continue
      starts.append(words[0])
      for index in range(len(words) - 1):
        path[words[index]].append(words[index+1])
      path[words[-1]].append(None)

  print("Processing lyrics...", file=sys.stderr) 
  lines = []

  for i in range(total_len / n):
    word = random.choice(starts)
    line = []
    while word is not None:
      line.append(word)
      word = random.choice(path[word])
    lines.append(line)
  return lines

if __name__ == '__main__':
  if len(sys.argv) == 2 and sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
    n = int(sys.argv[1]) 
  elif len(sys.argv) == 1:
	n = 10
  else:
    print("usage: python rand_lyrics.py [ n=10 ]")
    sys.exit(1)
  lyrics = generateMarkov(n)
  print('\n'.join(' '.join(line) for line in lyrics))
  
