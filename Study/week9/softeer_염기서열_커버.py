import sys 
sys.stdin = open('input.txt') 

N,M = map(int, input().split())
DNA = [list(input()) for _ in range(N)]

# 염기서열 N개 -> 초염기서열은 염기서열의 부분집합으로 간주 2^N개
superDNA = [None for _ in range(2**N)]
superDNA[0] = ['.'] * M  # 모든 염기서열을 만족하지 않는 초염기서열 -> 항등원 역할

def merge(DNA1, DNA2):
    # 두 염기서열 중 하나라도 비어있으면 빈 배열 반환
    if not (DNA1 and DNA2):
        return []

    DNA = []
    # 두 염기서열을 순회하며 교집합의 염기서열을 구한다
    for i in range(M):
        if DNA1[i] == '.':
            DNA.append(DNA2[i])
        elif DNA2[i] == '.':
            DNA.append(DNA1[i])
        elif DNA1[i] == DNA2[i]:
            DNA.append(DNA1[i])
        else:
            return []

    return DNA

# idx를 이진수로 변환했을 때 제일 오른쪽의 1을 찾아 분리
def gen_super_DNA(idx):
    pos = 0
    temp_idx = idx

    # pos: 제일 오른쪽 1의 위치
    while temp_idx % 2 == 0:
        temp_idx //= 2
        pos += 1

    # 분리한 두 이진수를 병합
    superDNA[idx] = merge(DNA[pos], superDNA[idx-2**pos])

# 초염기서열 생성
for i in range(1, 2**N):
    gen_super_DNA(i)

print(superDNA)