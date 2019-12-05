# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 02:56:51 2018

@author: diego
"""

#!/usr/bin/python
import praw
import pdb
import re
import os
import time
import string
import random

while 1==1:
    time.sleep(1)
    # Create the Reddit instance
    reddit = praw.Reddit('bot3')
    
    # and login
    #reddit.login(REDDIT_USERNAME, REDDIT_PASS)
    
    # Have we run this code before? If not, create an empty list
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    
    # If we have run the code before, load the list of posts we have replied to
    else:
        # Read the file into a list and remove any empty values
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))
    
    # Get the top 5 values from our subreddit
    subreddit = reddit.subreddit('askouija')
    for submission in subreddit.new(limit=1):
        #print(submission.title)
    
        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:
    
            # Do a case insensitive search
            if re.search("I", submission.title, re.IGNORECASE):
                letter = random.choice(string.ascii_uppercase)
                submission.reply(letter)
                print("Bot replying " , letter," to :" , submission.title)
    
                # Store the current id into our list
                posts_replied_to.append(submission.id)
    
    # Write our updated list back to the file
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")