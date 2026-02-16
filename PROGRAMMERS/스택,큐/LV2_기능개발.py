from collections import deque

def solution(progresses, speeds):
    answer = []
    q_progresses = deque(progresses)
    q_speeds = deque(speeds)
    day_cnt = 0
    how_many_job_today = 0
    while q_progresses:
    
        now_job = q_progresses.popleft()
        now_speeds = q_speeds.popleft()
        
        if (now_speeds * day_cnt) >= 100 - now_job:
            how_many_job_today += 1        
        
        else:
            answer.append(how_many_job_today)
            day_cnt = (100 - (now_job)) // now_speeds
            if (100 - (now_job)) % now_speeds != 0:
                day_cnt += 1
            how_many_job_today = 1        
        
        
    if how_many_job_today != 0:
        answer.append(how_many_job_today)
    
    return answer[1:]