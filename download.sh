#!/bin/bash

# download.sh


if [ -z "$1" ]; then
    echo "$0 subreddit_list_file"
    exit -1
fi

for i in `cat ${1}`; do
  python rlist.py $i
	python markov.py $i
done
