def solution(n, results):
    ans = 0
     win = {i: set() for i in range(1, n+1)}
      lose = {i: set() for i in range(1, n+1)}

       for winner, loser in results:
            win[winner].add(loser)
            lose[loser].add(winner)

        for i in range(1, n+1):
            # i가 진 사람들(승자들)은 i가 이긴 사람들도 이긴다.
            for winner in lose[i]:
                win[winner].update(win[i])
            # i에게 진 사람들(패자들)은 i가 진사람들에게도 진다
            for loser in win[i]:
                lose[loser].update(lose[i])

        for i in range(1, n+1):
            if len(win[i]) + len(lose[i]) == n-1:
                ans += 1

        return ans
