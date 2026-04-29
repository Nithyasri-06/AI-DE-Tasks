import requests
from collections import defaultdict
class DataAnalyzer:
    def __init__(self):
        self.BASE_URL="https://jsonplaceholder.typicode.com"
        self.users= []
        self.posts= []
        self.comments= []
        self.user_post=defaultdict(list)
        self.post_comment=defaultdict(list)
        
    def fetch_data(self):
        self.users=requests.get(f"{self.BASE_URL}/users").json()
        self.posts=requests.get(f"{self.BASE_URL}/posts").json()
        self.comments=requests.get(f"{self.BASE_URL}/comments").json()
        
    def map_user_posts(self):
        for post in self.posts:
            self.user_post[post["userId"]].append(post)
            
    def map_post_comments(self):
        for comment in self.comments:
            self.post_comment[comment["postId"]].append(comment)
        
    def show_user_post(self):
        print("\n----User->Posts----")
        for user_id,user_post_list in self.user_post.items():
            post_id=[post["id"]for post in user_post_list]
            print(f"User {user_id} -> Posts : {post_id} (Total : {len(user_post_list)} posts)")
    
    def show_post_comments(self):
        print("\n----Post->Comments----")    
        for post_id,post_comment_list in self.post_comment.items():
            comment_id=[comment["id"] for comment in post_comment_list]
            print(f"post {post_id} -> Comments : {comment_id} (Total : {len(post_comment_list)} comments)")
    
    def most_active_user(self):
        max_post=0
        most_Active_user=None
        for user in self.users:
            user_id=user["id"]
            post_count=len(self.user_post[user_id])
            if post_count>max_post:
                max_post=post_count
                most_Active_user=user
        print("Most Active user : ",most_Active_user["name"])
        print("Number of posts: ",max_post)
        
    def post_max_comment(self):
        max_comment=-1
        top_post=None
        for post in self.posts:
            post_id=post["id"]
            comment_count=len(self.post_comment[post_id])
            if comment_count>max_comment:
                max_comment=comment_count
                top_post=post
        print("Post with Highest comments")
        print("post id : ",top_post["id"])
        print("Title : ",top_post["title"])
        print("Total comments : ",max_comment)
        
    def average_comment_per_user(self):
        for user in self.users:
            user_id=user["id"]
            post_of_user=self.user_post[user_id]
            total_comments=0
            
            for post in post_of_user:
                post_id=post["id"]
                total_comments+=len(self.post_comment[post_id])
            total_posts=len(post_of_user)
            average_comments=total_comments/total_posts if total_posts!=0 else 0
            print(user["name"],"->",round(average_comments,2))
            
    def menu(self):
        while(True):
            print("\n--------Menu--------")
            print("1. Show User → Post count")
            print("2. Show Post → Comment count")
            print("3. Most Active User")
            print("4. Post with Highest Comments")
            print("5. Average Comments per User")
            print("6. Exit")
            
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                self.show_user_post()
            elif choice==2:
                self.show_post_comments()
            elif choice==3:
                self.most_active_user()
            elif choice==4:
                self.post_max_comment()
            elif choice==5:
                self.average_comment_per_user()
            elif choice==6:
                print("Exiting.....")
                break
            else:
                print("Invalid choice,Try again")
                
                
    def run(self):
        print("Fetching data")
        self.fetch_data()
        self.map_user_posts()
        self.map_post_comments()
        print("Data Loaded Successfully")
        self.menu()
    
if __name__=="__main__":
    analyzer=DataAnalyzer()
    analyzer.run()





