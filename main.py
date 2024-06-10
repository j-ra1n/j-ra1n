import feedparser

def fetch_latest_blog_posts(limit=3):
    feed = feedparser.parse("https://j-ra1n.tistory.com/rss")
    posts = []
    for entry in feed.entries[:limit]:
        title = entry.title
        link = entry.link
        posts.append((title, link))
    return posts

def update_readme(posts):
    with open("README.md", "r", encoding="utf-8") as file:
        readme_content = file.readlines()

    with open("README.md", "w", encoding="utf-8") as file:
        for line in readme_content:
            if "<!-- LATEST_BLOG_POSTS -->" in line:
                file.write("<!-- LATEST_BLOG_POSTS -->\n")
                for title, link in posts:
                    file.write(f'<a href="{link}" target="_blank">{title}</a><br>\n')
            else:
                file.write(line)

if __name__ == "__main__":
    latest_posts = fetch_latest_blog_posts()
    update_readme(latest_posts)
