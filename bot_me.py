import groupy
import time
import random


def get_member_by_name(member_list, name):
    for m in member_list:
        if m.nickname == name:
            return m
    return None


def get_group_by_name(group_list, name):
    for g in group_list:
        if g.name == name:
            return g
    return None


if __name__ == "__main__":

    data = {}
    data['group'] = None

    # get and show user's groups
    groups = groupy.Group.list()
    print("Your groups:")
    for g in groups:
        print(g.name)
    print()

    while True:
        print("Enter a group to act as a bot inside: ")
        group_name = input(">>> ")

        if not group_name:
            print("[ERROR] You must specify a valid group.")
            continue

        # check if input matches a group
        data['group'] = get_group_by_name(groups, group_name)

        if data['group'] is not None:
            break
        else:
            print("[ERROR] You are not a member of group '" + group_name + "'.")

    print("Successfully selected group '" + group_name + "'.")

    callback_url = "https://example.com/oath_callback" + str(random.randrange(0, 1000000000000000000000000))
    data['bot_picture'] = None

    print("Enter bot's display name: ")
    bot_name = input(">>> ")

    while True:
        try:
            data['bot'] = groupy.Bot.create(bot_name, data['group'], avatar_url=data['bot_picture'], callback_url=callback_url)

            print("Successfully created bot '" + bot_name + "'.")

            print("Now posting as bot.")
            while True:
                # post as this bot in the group
                text = input(">>> ")
                data['bot'].post(text)

        except groupy.api.errors.ApiError as e:
            if 'Name already taken by group member' in e.args[0]['errors']:

                data['bot_picture'] = get_member_by_name(data['group'].members(), bot_name).image_url

                bot_name += ' '

            if 'Callback url callback url  already registered for group' in e.args[0]['errors']:
                callback_url += '2'
