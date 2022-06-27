# import user --> user.User()
from user import User
from post import Post

app_user_one = User("kk@gmail.com", "Kishor K", "mypass", "Cloud Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("Data Architect")
app_user_one.get_user_info()

# create new user
app_user_two = User("ts@marvel.com", "Tony Stark", "keypass", "Life Saver")
app_user_two.get_user_info()


new_post = Post("On a life saving mission", app_user_two.name)
new_post.get_post_info()