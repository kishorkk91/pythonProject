import requests

response = requests.get("https://gitlab.com/api/v4/users/kishorkk91/projects")

# print(response.text)
# print(type(response.text)) --> str

# print(response.json())
# print(type(response.json())) --> list

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} \n Project Url: {project['web_url']} \n")

