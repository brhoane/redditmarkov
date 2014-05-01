#!/usr/bin/python

import requests
import time
import sys

# Our application id
cid = 'Sz4H8ppMzrZUFA'

# Unique user agent
headers = {
    'User-Agent': 'Linguistic Analysis/1.0 by bluejuce',
}

def get_subreddit_url(sr):
    """Makes a url from a subreddit name."""
    return 'http://reddit.com/r/' + sr + '/hot.json'

# 
def get_subreddit_titles(sr, n=10000):
    """Gets titles from a subreddit using the reddit API.
    
    Sends requests to the reddit api for titles from the specified
    subreddit. Titles are recieved in batches of 100. Waits 2 seconds
    between requests in order to avoid rate-limiting.

    sr: Subreddit name
    n: Number of titles to request
    
    Returns a list of tuples containing a post title and the score for
    that title.
    """
    print ("Getting " + str(n) + " post titles for subreddit " + sr)
    url = get_subreddit_url(sr)
    count = 0
    after = ''
    titles = []

    while (count < n and after != None):
        params = {
            'client_id': cid,
            't': 'all',
            'limit': '100',
            'after': after,
            'count': str(count),
            'show': 'all'
        }
        response = requests.get(url, headers=headers, params=params)        

        if (response.status_code == requests.codes.ok):
            js = response.json()
            after = js['data']['after']
            posts = js['data']['children']
            count += len(posts)
            for i in range(len(posts)):
                curr_title = posts[i]['data']['title']
                curr_score = posts[i]['data']['score']
                titles.append((curr_title, curr_score))
            print "Recieved " + str(count) + " titles"
        else:
            print "Bad response " + str(response.status_code)
            break
        time.sleep(2)
    return titles


def main():
    for i in range(1,len(sys.argv)):
        print sys.argv[i]
        titles = get_subreddit_titles(sys.argv[i], 10000)
        with open("download/" + sys.argv[i] + ".txt", "w+") as f:
            for x in titles:
                f.write(x[0].encode('utf8') + "\n")
                f.write(str(x[1]))
                f.write("\n")
    
if len(sys.argv) <= 1:
    print "Usage: python rlist.py subreddit"
else:
    main()