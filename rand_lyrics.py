from urllib2 import urlopen

from collections import defaultdict

import random

#handling unicode in both PY2 and PY3
import sys

if sys.version_info >= (3,):
  chr_func = chr
else:
  chr_func = unichr


def getRandomPage():
  page = urlopen('http://lyrics.wikia.com/Special:Random')
  content = page.read()
  page.close()
  return content

def parseLyrics(content):
  
  #abuse the hell out of the page structure
  index = content.find("class='lyricbox'")
  i1 = content.find('</div>', index) + len('</div>')
  i2 = content.find('<!--', index)
  
  #now for the PITA processing
  #lyrics-wiki obfuscates lyrics by putting them in untranslated UTF8
  #so unobfuscate them

  lines = content[i1:i2].split('<br />')
  
  lines_translated = [''.join(chr_func(int(c[:-1])) for c in line.split('&#') if c[:-1].isdigit()) for line in lines if line]

  return lines_translated

def getRandomLyrics():
  page = getRandomPage()
  return parseLyrics(page)

def generateMarkov(n=10):
  path = defaultdict(list)
  lengths = []
  starts = []
  for i in range(n):
    lyrics = getRandomLyrics()
    lengths.append(len(lyrics))
    for line in lyrics:
      words = line.strip().split()
      if not words: continue
      starts.append(words[0])
      for index in range(len(words) - 1):
        path[words[index]].append(words[index+1])
      path[words[-1]].append(None)
  
  lines = []
  for i in range(random.choice(lengths)):
    word = random.choice(starts)
    line = []
    while word is not None:
      line.append(word)
      word = random.choice(path[word])
    lines.append(line)
  return lines

if __name__ == '__main__':
  if len(sys.argv) == 1:
    lyrics = getRandomLyrics()
    print '\n'.join(lyrics)
  elif len(sys.argv) == 2 and sys.argv[1].isdigit():
    n = int(sys.argv[1])
    if n > 0:
     lyrics = generateMarkov(n)
     print '\n'.join(' '.join(line) for line in lyrics)
    else:
      print "Second argument must be a positive integer"
  else:
    print "usage: python rand_lyrics.py [n]"

