import tweepy
import re
import os

bearer = open("bearer.txt", "r")
bearer = bearer.readline()
bearer = str(bearer)

client = tweepy.Client(bearer, wait_on_rate_limit=True)

username = input("Username: ")
username = str(username)
times = input("Maximum following per account (1 - 1000): ")
times = int(times)


def program():
    user = client.get_user(username=username)
    user = str(user)

    user = re.sub(r'name.+?meta=\{\}\)', '', user)
    user = re.sub(r'Response.+?id=', '', user)
    user = user.strip()

    # get follwing
    response = client.get_users_following(user, max_results=times, user_fields="username")

    response = str(response)

    # filter output
    response = response.replace("Response(data=[", "")
    response = response.replace(">, ", "]]\n[[@")
    response = re.sub(r'<User id=.+?username=', '', response)
    response = re.sub(r'>], includes=\{\}.+?}\)', '', response)

    # write follwing in file
    dir_exists = os.path.isdir("Accounts/" + username)
    if str(dir_exists) == "False":
        os.makedirs("Accounts/" + username)



    file_exists = os.path.isfile("Accounts/" + username + "/" + username + "_following.md")
    if str(file_exists) == "True":
        os.remove("Accounts/" + username + "/" + username + "_following.md")

    f = open("Accounts/" + username + "/" + username + "_following.md", "w", encoding="utf-8")

    f.truncate(0)
    f.write("[[@" + response + "]]")
    f.close()


# rerun with different usernames
def rerun():
    user2 = client.get_user(username=run)
    user2 = str(user2)

    user2 = re.sub(r'name.+?meta=\{\}\)', '', user2)
    user2 = re.sub(r'Response.+?id=', '', user2)
    user2 = user2.strip()

    # get follwing
    response = client.get_users_following(user2, max_results=times, user_fields="username")

    response = str(response)

    # filter output
    response = response.replace("Response(data=[", "")
    response = response.replace(">, ", "]]\n[[@")
    response = re.sub(r'<User id=.+?username=', '', response)
    response = re.sub(r'>], includes=\{\}.+?}\)', '', response)

    # write follwing in file
    file_exists = os.path.isfile("Accounts/" + username + "/" + run + "_following.md")

    if str(file_exists) == "True":
        os.remove("Accounts/" + username + "/" + run + "_following.md")
    f = open("Accounts/" + username + "/" + run + "_following.md", "w", encoding="utf-8")

    f.truncate(0)
    f.write("[[@" + response + "]]")
    f.close()


program()

runs = open("Accounts/" + username + "/" + username + "_following.md", "r")

# rerun
for run in runs:
    run = run.replace(r'[[', '')
    run = run.replace(r']]', '')
    run = run.replace(r'@', '')
    run = run.strip("\n")
    run = str(run)
    rerun()


