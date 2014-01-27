rand_lyrics
===========

Gets random lyrics off the internet, because why not

To run, simply type

    python rand_lyrics.py

and it will randomly output a (real) song. Or empty text, sometimes. Who knows?

To create a Markov Chain-generated "song", you need to actually call it from Python:

    import rand_lyrics
    song = rand_lyrics.generateMarkov(n=10)
    
The `n` parameter denotes how many songs will be used to train the Markov Chain. 10 seemed like a good compromise between not just spitting out an existing song and not running forever. `song` will be a list of lists, because you're an adult, and you can just deal with it.

I'm not 100% sure any of this actually complies with Fair Use, because all the APIs I could find only output partial lyrics and that's just bad. If I wanted a "generate the first part of the first line of a song" program, I could make it, but I won't.
