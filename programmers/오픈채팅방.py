def insert(dic, idx, action, uid, name="None"):
    if uid not in dic:
        dic[uid] = [[idx, action, name]]
        return

    if name == "None":
        name = dic[uid][0][2]
    dic[uid].append([idx, action, name])

    if (len(dic[uid]) > 1):
        for items in dic[uid]:
            items[2] = name


def leave(dic, idx, action, uid):
    name = dic[uid][0][2]
    dic[uid].append([idx, action, name])


def change(dic, uid, name):
    for items in dic[uid]:
        items[2] = name


def get_action_name(action):
    if action == "Enter":
        return "들어왔습니다."
    else:
        return "나갔습니다."


def flatten(lst):
    res = []
    for item in lst:
        res.extend(item)
    return res


def solution(record):
    ans = []
    dic = {}

    for i in range(len(record)):
        item = record[i]
        items = item.split(' ')
        action, uid = items[0], items[1]

        if action == 'Enter':
            name = items[2]
            insert(dic, i, action, uid, name)
        elif action == 'Leave':
            leave(dic, i, action, uid)
        elif action == 'Change':
            name = items[2]
            change(dic, uid, name)

    arr = sorted(flatten(dic.values()), key=lambda x: x[0])

    for items in arr:
        action, name = items[1], items[2]
        result = name + "님이 " + get_action_name(action)
        ans.append(result)

    return ans
