class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name  = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password()

    def change_job_title(self, new_job_titile):
        self.current_job_title = new_job_titile

    def get_user_info(self):
        print(f"User {self.name} currently work as a {self.current_job_title}. You can contact them at {self.email}")
