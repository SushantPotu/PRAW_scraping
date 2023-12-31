import praw
import pdb
import re
import os
import time

# CHANGE THE ...'S WITH OWN DETAILS
scraping = praw.Reddit(
    client_id = "...",
    client_secret = "...",
    user_agent = "... by u/...",
    username = "...",
    password = "..."
)

def file_update():
    for post_id in replied_posts: 
        replyW.write(post_id + "\n")
        print("done")

if not os.path.isfile("reply.txt"):
    replied_posts = []
else:
    replyR = open("reply.txt", "r")
    replied_posts = replyR.read()
    replied_posts = replied_posts.split("\n")
    replied_posts = list(filter(None, replied_posts))
    replyR.close()

# CURRENTLY SET TO SEARCH FOR TIMES SQUARE IN TOP ALL TIME OF R/ALL WITH 500 POST LIMIT
scrape_subreddit = scraping.subreddit('all')
replied_posts = []
replyW = open("reply.txt", "a")
for post in scrape_subreddit.top(limit=500):
    if post.id not in replied_posts:
        if re.search("times square", post.title, re.IGNORECASE):
            if post.archived == True:
                print(f"Skipped old post: {post.title}") 
            try:
                post.reply(".")
                print(f"Replied to post: {post.title}")  
                replied_posts.append(post.id)
                print(f"Added post {post.id} to replied posts")
                print(f"Writing post IDs to file: {replied_posts}")
                file_update()
            except:
                print("Error replying to post:", post.title)
            
            
replyW.close()
replied_posts = []
            