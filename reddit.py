import praw
import json

import requests

appId = "Qwu48DHwWkxHm4-7R6ktvw"
secret = "fS9rtOLgNKzvh9sdWsCamWQ7HUWWCg"

reddit = praw.Reddit(
    client_id= appId,
    client_secret = secret,
    password="123katimoh456",
    user_agent="apptest by u/mushroom416",
    username="mushroom416",
)

def get_subreddit(subreddit):
    subreddit = reddit.subreddit(subreddit)
    return subreddit


def get_hot_posts(subreddit, limit):
    hot_posts = subreddit.hot(limit=limit)
    return hot_posts


def get_top_posts(subreddit, limit):
    top_posts = subreddit.top(limit=limit)
    return top_posts


def get_new_posts(subreddit, limit):
    new_posts = subreddit.new(limit=limit)
    return new_posts


def get_controversial_posts(subreddit, limit):
    controversial_posts = subreddit.controversial(limit=limit)
    return controversial_posts


posts = get_controversial_posts(get_subreddit("Apple"), 10)

submissions = []
for post in posts:
    #append to list
    submissions.append(post)





#returns dynamic data
def searchNewsApi(searchTerm):
    url = ('https://newsapi.org/v2/everything?'
            'q=Apple&'
            'from=2022-04-11&'
            'sortBy=popularity&'
            'apiKey=cc3b154467694d8daca6f2cd5817f288')

    response = requests.get(url)

    articles  = response.json()["articles"]

    for article in articles:
        print(article["title"], article["content"])
        print("\n")
        print("====================================")



#we will focus on the controversial posts and s

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="administrator",
  password="password",
  database="reddit"
)

cursor = mydb.cursor()

#create database
cursor.execute("CREATE DATABASE IF NOT EXISTS reddit")

#create table subreddit table


cursor.execute("CREATE TABLE IF NOT EXISTS subreddits (subredditId INT NOT NULL PRIMARY KEY, subreddit VARCHAR(255))")



#create table submisson table
cursor.execute("CREATE TABLE IF NOT EXISTS submissions (id INT  AUTO_INCREMENT, title VARCHAR(255), content LONGTEXT, subId INT, PRIMARY KEY (id), CONSTRAINT FK_post FOREIGN KEY (subID) REFERENCES subreddits(subredditId))")

#show tables
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)    


#insert into table
cursor.execute("INSERT INTO subreddits (subredditId, subreddit) VALUES (1, 'Apple')")

#insert multiple rows

#create list of tuples
submissionTuples = []
for submission in submissions:
    submissionTuples.append((submission.title, submission.selftext, 1))


cursor.executemany("INSERT INTO submissions (title, content, subId) VALUES ( %s, %s, %s)", submissionTuples)

mydb.commit()
#get data from table
cursor.execute("SELECT * FROM submissions")


result = cursor.fetchall()

for row in result:
    print(row)