def solution(id_list, report, k):
    answer = []
    
    store = {} // 각 유저가 어떤 사람을 신고했는지 저장
    count = {} // 각 유저들이 몇 번의 신고를 받는지 저장
    memory = set() // 신고했던 내역을 저장(중복된 사항은 거를수 있도록 Set을 사용)
    
		// 초기화
    for i in id_list: 
        store[i] = []
        count[i] = 0
    
		// count와 store에 저장하는 구현부분
    for val in report:
        user, target = val.split(' ')

				// 이전에 동일한 중복 내역이 없다면 진행
        if (user, target) not in memory:
            memory.add((user, target)) // 신고 내역 저장
            count[target] += 1 // 신고 횟수 저장
            store[user].append(target) // 유저가 누구에게 신고했는지 저장
    
		// k번 이상 신고받은 사람의 리스트를 추출
    suspended_user = []
    for id in id_list:
        if count[id] >= k:
            suspended_user.append(id)
    
		// 저장된 신고 내역을 보면서 k번 이상 신고받은 사람의 횟수를 카운트해서 리스트에 저장
    result = []
    for key in store:
        value = store[key]
        cnt = 0
        for j in value:
            if j in suspended_user:
                cnt += 1
        result.append(cnt)
    
    return result

def bestSolution(id_list, report, k):
		// id의 개수만큼 ans 리스트를 초기화
    ans = [0] * len(id_list)
		// id_list에서 id를 꺼내서 각각 0으로 초기화
    reports = {i : 0 for i in id_list}
    
		// 애초에 중복을 set으로 없앤 상태에서 카운팅
    for i in set(report):
        reports[i.split()[1]] += 1
    
		// 마찬가지로 중복을 없앤 상태에서 k보다 큰 것을 카운팅
    for i in set(report):
        if reports[i.split()[1]] >= k:
            ans[id_list.index(i.split()[0])] += 1
    
    return ans