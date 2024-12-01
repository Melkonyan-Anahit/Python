import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_filtered_posts():
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()  
        posts = response.json()
        filtered_posts = [
            post for post in posts
            if len(post['title'].split()) <= 6 and post['body'].count('\n') <= 3
        ]
        return filtered_posts
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []

def display_posts(posts):
    if posts:
        print("Filtered Posts:")
        for post in posts:
            print(f"ID: {post['id']}, Title: {post['title']}")
    else:
        print("No posts available or an error occurred.")

def create_new_post():
    post_data = {
        "title": "A Brand New Post",
        "body": "This is the body of the newly created post.",
        "userId": 1
    }
    try:
        response = requests.post(f"{BASE_URL}/posts", json=post_data)
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
        print(f"Error creating post: {e}")
        return None

def update_existing_post(post_id):
    updated_data = {
        "title": "Updated Title for Post",
        "body": "This is the new content for the post.",
        "userId": 1
    }
    try:
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_data)
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        print(f"Error updating post: {e}")
        return None

def delete_existing_post(post_id):
    try:
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status() 
        print(f"Post {post_id} has been deleted.")
        return True
    except requests.RequestException as e:
        print(f"Error deleting post: {e}")
        return False

if name == "main":
    filtered_posts = get_filtered_posts()
    display_posts(filtered_posts)
    
    created_post = create_new_post()
    if created_post:
        print("\nCreated Post:", created_post)

        updated_post = update_existing_post(created_post["id"])
        if updated_post:
            print("\nUpdated Post:", updated_post)
        delete_existing_post(created_post["id"])