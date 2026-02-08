def solution(record):
    answer = []
    change_dict = {}
    
    for r in record:
        single_record = r.split()

        if single_record[0] in ("Change", "Enter") :
            change_dict[single_record[1]] = single_record[2]
    
    for r in record:
        single_record = r.split()
        
        if single_record[0] == "Enter":
            if single_record[1] in change_dict:
                single_record[2] = change_dict[single_record[1]]
            answer.append(single_record[2] + "님이 들어왔습니다.")
        elif single_record[0] == "Leave":
            answer.append(change_dict[single_record[1]] + "님이 나갔습니다.")
        else:
            continue # Change 제외
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))