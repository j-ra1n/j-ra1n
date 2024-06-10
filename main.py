import feedparser
import requests
import time

def fetch_latest_blog_posts(limit=1):
    feed = feedparser.parse("https://j-ra1n.tistory.com/rss")
    posts = []
    for entry in feed.entries[:limit]:
        title = entry.title
        link = entry.link
        published = entry.published
        posts.append((title, link, published))
    return posts

def trigger_jenkins():
    jenkins_url = 'http://<your-jenkins-url>/job/<your-job-name>/build'
    jenkins_user = '<your-jenkins-username>'
    jenkins_token = '<your-jenkins-api-token>'
    
    response = requests.post(jenkins_url, auth=(jenkins_user, jenkins_token))
    if response.status_code == 201:
        print("Jenkins job triggered successfully")
    else:
        print(f"Failed to trigger Jenkins job: {response.status_code}")

def main():
    last_published = None
    
    while True:
        latest_posts = fetch_latest_blog_posts()
        if latest_posts:
            title, link, published = latest_posts[0]
            if last_published != published:
                print(f"New post detected: {title}")
                trigger_jenkins()
                last_published = published
        time.sleep(600)  # 10분마다 검사

if __name__ == "__main__":
    main()
