rand_lyrics
===========

Gets random lyrics off the internet, because why not

To run, simply type

    python rand_lyrics.py

and it will randomly output a (real) song. Or empty text, sometimes. Who knows? It runs off a wiki of user-generated content, so sometimes it'll be crap and you'll just have to deal with it.

To create a Markov Chain-generated "song", add a second integer argument

    python rand_lyrics.py 10

The `n` parameter denotes how many songs will be used to train the Markov Chain. 10 seemed like a good compromise between not just spitting out an existing song and not running forever. If you want something really cool, run it with `100`. No it doesn't parallelize. I'll wait.

I'm not 100% sure any of this actually complies with Fair Use, because all the APIs I could find only output partial lyrics and that's just bad. If I wanted a "generate the first part of the first line of a song" program, I could make it, but I won't.
