import requests
import time
import sys

cid = 'Sz4H8ppMzrZUFA'

headers = {
    'User-Agent': 'Linguistic Analysis/1.0 by bluejuce',
}

def get_subreddit_url(sr):
    return 'http://reddit.com/r/' + sr + '/top.json'

def get_subreddit_titles(sr, n):
    print ("Getting " + str(n) + " post titles for subreddit " + sr)
    url = get_subreddit_url(sr)
    count = 0
    after = ''
    titles = []

    while (count < n):
        params = {
            'client_id': cid,
            't': 'all',
            'limit': '100',
            'after': after,
            'count': str(count)
        }
        response = requests.get(url, headers=headers, params=params)        

        if (response.status_code == requests.codes.ok):
            js = response.json()
            after = js['data']['after']
            posts = js['data']['children']
            count += len(posts)
            cur_titles = [(posts[i]['data']['title'], posts[i]['data']['score']) for i in range(len(posts))]
            titles += cur_titles
            print "Recieved " + str(count) + " titles"
        else:
            print "Bad response " + str(response.status_code)
            break
        time.sleep(2)
    return titles


def main():
    for i in range(1,len(sys.argv)):
        titles = get_subreddit_titles(sys.argv[i], 1000)
        with open(sys.argv[i] + ".txt", "w") as f:
            for x in titles:
                f.write(x[0].encode('utf8') + "\n")
                f.write(str(x[1]))
                f.write("\n")
    
if len(sys.argv) <= 1:
    print "Usage: python rlist.py subreddit1 [subreddit2 ... ]"
else:
    main()

