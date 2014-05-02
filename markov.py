#!/usr/bin/python
import sys
import json
from random import random

def make_key(kgram):
    return '|'.join(kgram)


class MarkovModel:

    def add_kgram(self, kgram, nextword):
        """Adds a kgram and the next word to the model's stats."""
        key = make_key(kgram)
        if key in self.stats:
            (words, n) = self.stats[key]
            for i in range(len(words)):
                w, c = words[i]
                if w == nextword:
                    words[i] = (w, c+1)
                    break
            else:
                words.append((nextword,1))
            self.stats[key] = (words, n+1)
        else:
            self.stats[key] = ([(nextword, 1)], 1)

    def add_kgrams(self, data, k):
        """Adds all kgrams of length k to the model's stats."""
        for title in data:
            for i in range(0, len(title)-k):
                kgram = title[i:i+k]
                nextword = title[i+k]
                self.add_kgram(kgram, nextword)

    def add_stats(self, data):
        """Adds all kgrams up to length maxk to the model's stats."""
        for i in range(1, self.maxk+1):
            self.add_kgrams(data, i)

    def normalize(self):
        """Normalizes the histograms so that their frequencies sum to 1."""
        for key in self.stats:
            words, n = self.stats[key]
            nwords = []
            sumc = 0.0
            for w,c in words:
                v = float(c) / n
                sumc += v
                nwords.append((w,sumc))
            self.hist[key] = nwords

    def __init__(self, title_data, maxk=5):
        self.maxk = maxk
        self.stats = dict()
        self.add_stats(title_data)
        self.hist = dict()
        self.normalize()

    def next_word(self, sentence):
        """Generates the next word in a random sentence."""
        slen = min(self.maxk, len(sentence))
        kgram = sentence[-slen:]
        key = make_key(kgram)
        while key not in self.hist:
            slen -= 1
            if slen == 0: # Shouldn't happen
                return "ERROR"
            kgram = sentence[-slen:]
            key = make_key(kgram)
        r = random()
        for (w,c) in self.hist[key]:
            if r < c:
                return w
        else:
            return "ERROR"

    def random_sentence(self):
        """Generates a random sentence based on statistical data."""
        sentence = ["START"]
        nextword = self.next_word(sentence)
        while nextword != "END":
            sentence.append(nextword)
            nextword = self.next_word(sentence)
        return " ".join(sentence[1:])


def read_title_data(path):
    """Reads titles from a file and strips scores."""
    ret = []
    with open(path, "r") as f:
        for line in f:
            if len(line) >= 6:
                # yield title without terminating newline
                ret.append(["START"] + line[:-1].lower().translate(None, ':@#$%^&*,.\'"').split(' ') + ["END"])
    return ret

def main():
    for i in range(1,len(sys.argv)):
        subreddit = sys.argv[i]
        model = MarkovModel(read_title_data("download/" + subreddit + ".txt"), 1)
        list = [model.random_sentence() for i in range(0, 20)]
        data = {"title": subreddit, "url" : subreddit, "titles" : list, }
        with open("data/" + subreddit + ".json", 'w+') as outfile:
            json.dump(data, outfile)
        print list


if len(sys.argv) <= 1:
    print "Usage: python markov.py subreddit"
else:
    main()
