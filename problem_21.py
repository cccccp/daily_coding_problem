def number_of_classrooms(intervals): #O(nlog(n)) time complexity/ O(n) space complexity
    marked_times=[]
    for interval in intervals:
        marked_times.append((interval[0],'start'))
        marked_times.append((interval[1],'end'))
    
    marked_times.sort(key=lambda x:x[0])
    
    common=0
    classrooms=0
    for marked_time in marked_times:
        if marked_time[1]=='start':
            common+=1
            classrooms=max(common,classrooms)
        else:
            common-=1
    
    return classrooms
