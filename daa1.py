def knapsack(c,weight,values):
    value_per_weight=[]
    for i in range(len(weight)):
        value_per_weight.append((values[i]/weight[i],weight[i],values[i]))
    value_per_weight.sort(reverse=True)
    total_value=0.0
    rem_cap=c
    for value_per_unit,weight,value in value_per_weight:
        if rem_cap<=0:
            break
        fraction=min(1,rem_cap/weight)
        total_value+=fraction*value
        rem_cap-=fraction* weight
    return total_value
weights=list(map(int,input("Enter weights").split()))
values=list(map(int,input("Enter values").split()))
capacity=int(input("Enter the capacity"))
max_val=knapsack(capacity,weights,values)
print("Maximum value of knapsack is:",max_val)
            
        
    
