from urllib2 import urlopen


def getRandomPage():
  page = urlopen('http://lyrics.wikia.com/Special:Random')
  content = page.read()
  page.close()
  return content

def getLyrics(content):

  #abuse the hell out of the page structure
  index = content.find("class='lyricbox'")
  i1 = content.find('</div>', index) + len('</div>')
  i2 = content.find('<!--', index)

  #now for the PITA processing
  #lyrics-wiki obfuscates lyrics by putting them in untranslated UTF8
  #so unobfuscate them

  lines = content[i1:i2].split('<br />')

  lines_translated = [''.join(chr(int(c[:-1])) for c in line.split('&#') if c[:-1].isdigit()) for line in lines if line]

  return lines_translated


if __name__ == '__main__':
  page_content = getRandomPage()
  print '\n'.join(getLyrics(page_content))
