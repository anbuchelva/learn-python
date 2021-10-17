import requests

END_POINT = "https://pixe.la/v1/users"
USER_NAME = "anbuchelva"
API_KEY = "<hidden>"

users_param = {
    "token": API_KEY,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create user using manually generated API Key
# create_user = requests.post(url=END_POINT, json=users_param)
# print(create_user.text)

# Update user profile
Profile_URL = "https://pixe.la/@anbuchelva"

user_profile_param = {
    "displayName": "Anbuselvan Palaniyandi",
    "gravatarIconEmail": "anbuchelva@gmail.com",
    # "timezone": "IST",
}
user_header = {
    "X-USER-TOKEN": API_KEY
}
# update_user = requests.put(url=Profile_URL, json=user_profile_param, headers=user_header)
# print(update_user.text)

# Create new graph for a habit
create_graph_params = {
    # "id": "graph-l2c",
    "name": "Learn to code",
    "unit": "lines of code",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Kolkata",
}
# create_graph = requests.post(url=f"{END_POINT}/{USER_NAME}/graphs", json=create_graph_params, headers=user_header)
# print(create_graph.text)

# update_graph_params = requests.put(url=f"{END_POINT}/{USER_NAME}/graphs/graph-l2c",
#                                     json=create_graph_params,
#                                     headers=user_header)
# print(update_graph_params.text)

post_pixel_params = {
    "date": "20211017",
    "quantity": "59",
}

post_pixel = requests.post(url=f"{END_POINT}/{USER_NAME}/graphs/graph-l2c", json=post_pixel_params, headers=user_header)
print(post_pixel.text)

# Delete posted pixel entry
# delete_pixel = requests.delete(url=f"{END_POINT}/{USER_NAME}/graphs/graph-l2c/20211015", headers=user_header)
# print(delete_pixel.text)