def solution(bridge_length,weight,truck_weights):
    ans=0
    # 트럭 댓수
    a=len(truck_weights)
    timer=[]
    crossed_truck=[]
    crossing_truck=[]
    while(len(crossed_truck)!=a):
        ans+=1
        timer=list(map(lambda x: x+1, timer))
        if len(timer)>0:
            if timer[0]==bridge_length:
                timer.pop(0)
                b=crossing_truck.pop(0)
                crossed_truck.append(b)
        if len(truck_weights)>0:
            if sum(crossing_truck) + truck_weights[0] <= weight:
                b=truck_weights.pop(0)
                crossing_truck.append(b)
                timer.append(0)
        print(timer)

    return ans