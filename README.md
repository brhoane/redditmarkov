redditmarkov
============

Markov Chains on reddit post titles.

Downloading Post Titles: rlist.py
---------------------------------

The [python requests package](http://docs.python-requests.org/en/latest/) is required for this script.

Usage:
./rlist.py [subreddit list]


Generating Markov Models: markov.py
-----------------------------------

Usage:
./markov.py [file containing title data]

Downloading with scripts:
----------------------------------


Usage:
./download.sh [file]

where the file is a newline separate list of subreddits. 
