rand_lyrics
===========

Gets random lyrics off the internet and makes a new song out of them, because why not

To run, simply type

    python rand_lyrics.py
    
This will read 10 songs off of the internet and use them to create a new song, using a line-oriented simple Markov Chain. The songs are pretty hit-or-miss because it's all user-generated content and users can't spell. Also sometimes a song just doesn't have lyrics. Or it's not in English, which is why this is all unicode-aware. (It handles Spanish and French really interestingly, because of the overlap with Engllish. It's great.)

The program takes an optional integer argument:

    python rand_lyrics.py 100

The `n` parameter denotes how many songs will be used to train the Markov Chain. 10 seemed like a good compromise between not just spitting out an existing song and not running forever. If you want something really cool, run it with `100`. No it doesn't parallelize. I'll wait.

I'm not 100% sure any of this actually complies with Fair Use, because all the APIs I could find only output partial lyrics and that's just bad. If I wanted a "generate the first part of the first line of a song" program, I could make it, but I won't.
