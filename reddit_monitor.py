"""
Reddit Senior Care Monitor
A monitoring tool for A Senior Journey senior care placement agency in Tucson, Arizona.

This script monitors specified Reddit subreddits for discussions related to senior care
and sends email alerts to the team for manual review and response.

NO automated posting occurs - all responses are manual and human-driven.
"""

import praw
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import config

# Keywords to monitor for senior care discussions
KEYWORDS = [
    'senior care', 'assisted living', 'memory care', 'senior housing',
    'elderly care', 'nursing home', 'senior living', 'senior placement',
    'alzheimer', 'dementia care', 'independent living', 'senior community'
]

# Subreddits to monitor
SUBREDDITS = [
    'Tucson',
    'arizona',
    'AgingParents',
    'caregivers',
    'dementia',
    'AlzheimersGroup'
]


def initialize_reddit():
    """Initialize Reddit API connection using PRAW."""
    try:
        reddit = praw.Reddit(
            client_id=config.REDDIT_CLIENT_ID,
            client_secret=config.REDDIT_CLIENT_SECRET,
            user_agent=config.REDDIT_USER_AGENT
        )
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Successfully connected to Reddit API")
        return reddit
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error connecting to Reddit: {e}")
        return None


def send_email_alert(post_data):
    """Send email alert when relevant post is found."""
    try:
        msg = MIMEMultipart()
        msg['From'] = config.EMAIL_FROM
        msg['To'] = ', '.join(config.EMAIL_TO)
        msg['Subject'] = f"Reddit Alert: {post_data['subreddit']} - {post_data['title'][:50]}..."

        body = f"""
New relevant post found on Reddit:

Subreddit: r/{post_data['subreddit']}
Title: {post_data['title']}
Author: u/{post_data['author']}
URL: {post_data['url']}
Posted: {post_data['created']}

Post Content:
{post_data['content'][:500]}{'...' if len(post_data['content']) > 500 else ''}

---
This is an automated alert from the Reddit Senior Care Monitor.
Please review and respond manually as appropriate.
"""

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
        server.starttls()
        server.login(config.EMAIL_FROM, config.EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Email alert sent for post: {post_data['title'][:50]}")
        return True
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error sending email: {e}")
        return False


def check_post_relevance(post):
    """Check if a post contains relevant keywords."""
    text_to_check = f"{post.title} {post.selftext}".lower()

    for keyword in KEYWORDS:
        if keyword.lower() in text_to_check:
            return True
    return False


def monitor_subreddits(reddit, processed_posts):
    """Monitor specified subreddits for new posts."""
    for subreddit_name in SUBREDDITS:
        try:
            subreddit = reddit.subreddit(subreddit_name)

            # Check new posts
            for post in subreddit.new(limit=10):
                post_id = post.id

                # Skip if already processed
                if post_id in processed_posts:
                    continue

                # Check if post is relevant
                if check_post_relevance(post):
                    post_data = {
                        'subreddit': subreddit_name,
                        'title': post.title,
                        'author': str(post.author),
                        'url': f"https://reddit.com{post.permalink}",
                        'created': datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                        'content': post.selftext
                    }

                    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Relevant post found in r/{subreddit_name}: {post.title[:50]}")
                    send_email_alert(post_data)

                # Mark as processed
                processed_posts.add(post_id)

        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error monitoring r/{subreddit_name}: {e}")

    return processed_posts


def main():
    """Main monitoring loop."""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting Reddit Senior Care Monitor")
    print(f"Monitoring subreddits: {', '.join(SUBREDDITS)}")
    print(f"Alert emails will be sent to: {', '.join(config.EMAIL_TO)}")
    print("-" * 80)

    reddit = initialize_reddit()
    if not reddit:
        print("Failed to initialize Reddit connection. Exiting.")
        return

    processed_posts = set()

    while True:
        try:
            processed_posts = monitor_subreddits(reddit, processed_posts)

            # Keep processed posts set from growing too large
            if len(processed_posts) > 1000:
                processed_posts = set(list(processed_posts)[-500:])

            # Wait before next check (15 minutes)
            wait_time = 900
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Waiting {wait_time//60} minutes before next check...")
            time.sleep(wait_time)

        except KeyboardInterrupt:
            print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Monitoring stopped by user")
            break
        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Unexpected error: {e}")
            print("Waiting 5 minutes before retrying...")
            time.sleep(300)


if __name__ == "__main__":
    main()
