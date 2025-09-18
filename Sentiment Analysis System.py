# Step 1: Import libraries
import praw
from textblob import TextBlob

# Step 2: Connect to Reddit API
reddit = praw.Reddit(
    client_id = "w2pGyjV0uFMKnz1HQ7U3zw",
    client_secret = "FS1n9oDilkKnFWBoRU3gVO-rvRDmsg",
    user_agent = "sentiment_script by taha_musa"
)

# Step 3: Collect user input (keyword + number of posts)
keyword = input("Enter a keyword to search: ")    
count = int(input("How many posts to analyze? "))

# Step 4: Search posts in Reddit and display basic info
for submmission in reddit.subreddit ('all').search (keyword, limit = count):
    print ('=' * 60)
    print ('Title:', submmission.title)
    print ('URL:', submmission.url)

    # Step 5: Collect comments for each post
    submmission.comments.replace_more (limit = 0)
    comments = submmission.comments.list ()
    
    if not comments:
        print ('No comment found. ')
        
        # Step 6: Sentiment analysis using TextBlob
    else:
        for comment in comments [:3]:
            text = comment.body
            blob = TextBlob (text)
            polarity = blob.sentiment.polarity
    
            if polarity > 0:
                sentiment = "😊 Positive"
            elif polarity < 0:
                sentiment = "😠 Negative"
            else:
                sentiment = "😐 Neutral"
                
            print(f"\nComment: {text}")
            print("Sentiment:",sentiment)