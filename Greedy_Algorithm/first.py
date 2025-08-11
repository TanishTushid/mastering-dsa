def activity_selection(activites):
    #sort by the end time
    activites.sort(key = lambda x:x[1])
    
    selected = []
    last_end = 0

    for start, end in activites:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected

activities = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7), (8, 9)]
print(activity_selection(activities))