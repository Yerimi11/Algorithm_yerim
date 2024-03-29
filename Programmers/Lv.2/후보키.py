# 테스트케이스 추가
# [["a", "1", "aaa", "c", "ng"], ["a", "1", "bbb", "e", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]  >>>> 5
# [["a", "aa"], ["aa", "a"], ["a", "a"]]  >>>> 1
# [["100", "100", "ryan", "music", "2"], ["200", "200", "apeach", "math", "2"], ["300", "300", "tube", "computer", "3"], ["400", "400", "con", "computer", "4"], ["500", "500", "muzi", "music", "3"], ["600", "600", "apeach", "music", "2"]] >>>> 3
# [["a", "1", "aaa", "c", "ng"], ["b", "1", "bbb", "c", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]  >>>>> 3

# https://school.programmers.co.kr/learn/courses/30/lessons/42890#

# [["a", "1", "aaa", "c", "ng"], 
#  ["a", "1", "bbb", "e", "g"], 
#  ["c", "1", "aaa", "d", "ng"], 
#  ["d", "2", "bbb", "d", "ng"]]  >>>> 5
# (1,3), (1,4), (1,5), (2,4), (3,4)
# (1,2,3), (1,3,4).. 이런 것 다 되지만 최소 갯수여야하니 pass

# 최소성 검사를 먼저 한다. for in 으로, 후보키 후보들 중에서 최소성 검사로 먼저 제외함
#   (ex:(1)이 후보키를 만족했을 때, (1,3), (1,2,4) 이런 것들은 볼 필요가 없어짐. 이미 (1)이 최소 후보키니까
# 다음으로 유일성 검사. combination으로 열(인덱스) 조합(튜플)을 찾아낸다. 조합 갯수는 1개부터(학번 하나로도 되니까)
# for문으로 행을 돌면서 열 조합에 나온 행의 인덱스를 해쉬 키-밸류로 넣어서 len을 비교

# 최소성 검사를 먼저 한다. for in 으로, 후보키 후보들 중에서 최소성 검사로 먼저 제외함
#   (ex:(1)이 후보키를 만족했을 때, (1,3), (1,2,4) 이런 것들은 볼 필요가 없어짐. 이미 (1)이 최소 후보키니까
# 다음으로 유일성 검사. combination으로 열(인덱스) 조합(튜플)을 찾아낸다. 조합 갯수는 1개부터(학번 하나로도 되니까)
# for문으로 행을 돌면서 열 조합에 나온 행의 인덱스를 해쉬 키-밸류로 넣어서 len을 비교

# from itertools import combinations
# from collections import Counter

# 시도 중

# # 최소성 검사 먼저
# def is_minimal(candidate_keys, x):
#     for i in range(len(candidate_keys)):
#         for ck in candidate_keys[i]:
#             if ck not in x:
#                 break
#         else:
#             return False
#     return True

# # 유일성 검사
# def is_unique(relation, combi):
#     no_duple = set()
#     yes_duple = []
#     for row in range(len(relation)):
#         for c in combi: # combi: (0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), ...
#             no_duple.add(relation[row][c])
#             yes_duple.append(relation[row][c])
#     combi_cnt_total = len(combi) * len(relation) # 이게 끝이 아님!
#     # 1: 3개, d: 2개 c,e,2: 1개인데(Counter로 세자), 총 8개에서 3개+2개가 1개로 바뀌어야 함 (차 구하기)
#     # 그러면, 3-1=2, 2-1=1 더하면 3이고
#     # total 8-3=5랑 len(hash_list)랑 같으면 True
#     yes_duple = Counter(yes_duple)
#     for x in yes_duple:
#         if yes_duple[x] > 1:
#             combi_cnt_total -= (yes_duple[x]-1)
#             yes_duple[x] = 1
#     if combi_cnt_total == len(no_duple):
#         return True
#     else:
#         return False
        
    
# def solution(relation):
#     n_row = len(relation)
#     n_col = len(relation[0])
    
#     combi_list = []
#     for i in range(1, n_col+1):
#         combi_list.extend(combinations(range(n_col), i))
#         # combi_list = [(0,), (1,), (2,), (3,), 
#                     #   (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), 
#                     #   (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]
    
#     candidate_keys = []
#     for combi in combi_list: # 후보키: (1,3), (1,4), (1,5), (2,4), (3,4)
#         # if len(combi) <= 1 and is_unique(relation, combi):
#         #     candidate_keys.append(combi)
#         if len(combi) > 1 and is_minimal(candidate_keys, combi) and is_unique(relation, combi):
#             candidate_keys.append(combi)
            
    
#     return len(candidate_keys)

# solution([["a", "1", "aaa", "c", "ng"],  ["a", "1", "bbb", "e", "g"],  ["c", "1", "aaa", "d", "ng"],  ["d", "2", "bbb", "d", "ng"]]) # 5


# --------------------------------------

from itertools import combinations

def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    combi_list = list()
    for i in range(1, n_col+1):
        combi_list.extend(combinations(range(n_col), i))  #종목별로 만들 수 있는 모든 조합갯수 찾기

    final = []
    for combi in combi_list:
        tmp = [tuple([row[c] for c in combi]) for row in relation] # 주어진 키로 리스트의 index별 아이템 뽑아내기
        if len(set(tmp)) == n_row: #set로 변경후 사라진게 없다면 key로 사용해도 무방
            final.append(combi)

    print(final)
    answer = set(final[:])
    print("answer", answer)
    for i in range(len(final)):
        for j in range(i+1, len(final)):       # intersection: 교집합
            # 후보키[i]의 인덱스(원소)갯수 == 후보키[i]와 후보키[j]의 교집합 갯수 => 어쨋든 교집합이 있다면,
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))): # c 중에 겹치는 부분이 있는 것을 삭제
                answer.discard(final[j]) # 후보키[i]보다 갯수 많은 후보키[j]는 최소성에 해당 안되므로 리스트에서 삭제
    return(len(answer))

solution([["a", "1", "aaa", "c", "ng"],  ["a", "1", "bbb", "e", "g"],  ["c", "1", "aaa", "d", "ng"],  ["d", "2", "bbb", "d", "ng"]]) # 5

# # ---------------------------

# from itertools import combinations

# def solution(relation):
#     columnSize = len(relation[0])
#     CandidateKeys = []
#     answer = 0
#     columnIdx = [i for i in range(columnSize)]

#     for size in range(1, columnSize + 1):
#         columnCombis = combinations(columnIdx, size)
#         nowSet = set()
#         isCandidateKey = True

#         for columnCombi in columnCombis:
#             # 최소성 확인
#             minimal = True
#             for CandidateCol in CandidateKeys:
#                 including = True
#                 for col in CandidateCol:
#                     if col not in columnCombi:
#                         including = False
#                         break

#                 if including:
#                     minimal = False
#                     break

#             #최소성을 만족하지 못하면 건너 뛴다
#             if not minimal:
#                 continue

#             #유일성 확인
#             nowSet = set()
#             isCandidateKey = True
#             for row in relation:
#                 #해당하는 컬럼의 값을 하나의 값으로 만든다
#                 nowVal = ""
#                 for idx in columnCombi:
#                     nowVal += ',' + row[idx]

#                 #동일한 값이 있다면 유일성을 만족하지 못한다
#                 if nowVal in nowSet:
#                     isCandidateKey = False
#                     break
#                 else:
#                     nowSet.add(nowVal)

#             #최소성과 유일성을 만족하면 후보키이다
#             if isCandidateKey:
#                 answer += 1
#                 CandidateKeys.append(columnCombi)

#     return answer
