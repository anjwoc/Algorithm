from unicodedata import name


def solution(record):
    ans = []
    namespace = {}
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for r in record:
        items = r.split(' ')
        action, uid = items[0], items[1]
        if action in ['Enter', 'Change']:
            namespace[uid] = items[2]

    for r in record:
        items = r.split(' ')
        action, uid = items[0], items[1]
        if action == 'Change':
            continue
        ans.append(namespace[uid] + printer[action])

    return ans


testcase = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
            "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
answer = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.",
          "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

print("정답" if solution(testcase) == answer else "오답")
