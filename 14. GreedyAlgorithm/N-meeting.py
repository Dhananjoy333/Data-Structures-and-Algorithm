#Q. Find how many max meeting we can attend given start and end time
class Meeting:
    def __init__(self,start,end,position):
        self.start = start
        self.end = end
        self.position = position              
start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]  
meet = [Meeting(start[i],end[i],i+1) for i in range(len(start))]
meet.sort(key=lambda x:(x.end,x.start))   
result = [1]
count = 1
lastTime = meet[0].end
for i in range(1,len(end)):
    if meet[i].start >lastTime:
        count += 1
        result.append(meet[i].position)
        lastTime = meet[i].end
print(result)
print(count)