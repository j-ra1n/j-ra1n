import feedparser

def fetch_latest_blog_post():
    feed = feedparser.parse("https://j-ra1n.tistory.com/rss")
    latest_post = feed.entries[0]
    title = latest_post.title
    link = latest_post.link
    return title, link

def update_readme(latest_post_title, latest_post_link):
    with open("README.md", "r", encoding="utf-8") as file:
        readme_content = file.readlines()

    with open("README.md", "w", encoding="utf-8") as file:
        for line in readme_content:
            if "<!-- LATEST_BLOG_POST -->" in line:
                line = f"[{latest_post_title}]({latest_post_link})\n"
            file.write(line)

if __name__ == "__main__":
    latest_post_title, latest_post_link = fetch_latest_blog_post()
    update_readme(latest_post_title, latest_post_link)
