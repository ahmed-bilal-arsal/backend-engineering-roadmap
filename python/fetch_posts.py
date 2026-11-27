import json
import urllib.request

URL = "https://jsonplaceholder.typicode.com/posts"

#Fetch
with urllib.request.urlopen(URL) as response:
    posts = json.load(response)

#Filter: Keep user 1's posts
filtered = [post for post in posts if post["userId"] == 1]

#Save
with open("filtered_posts.json", "w") as file:
    json.dump(filtered, file, indent=2)

print(f"Saved {len(filtered)} of {len(posts)} posts")