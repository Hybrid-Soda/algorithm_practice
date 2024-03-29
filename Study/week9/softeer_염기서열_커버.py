import sys 
sys.stdin = open('input.txt') 


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

    # 분리한 두 이진수를 비교하여 새로운 초염기서열 생성
    superDNA[idx] = merge(DNA[pos], superDNA[idx-2**pos])


def gen_answer(idx):
    


if __name__ == "__main__":
    N,M = map(int, input().split())
    DNA = [input() for _ in range(N)]
    # 염기서열 N개 -> 초염기서열은 염기서열의 부분집합으로 간주 2^N개
    superDNA = [None for _ in range(2**N)]
    superDNA[0] = ['.'] * M  # 모든 염기서열을 만족하지 않는 초염기서열 -> 항등원 역할
    # 답안 배열 : DP
    ans = [N+1] * (2**N)
    ans[0] = 0

    # 초염기서열 생성
    for i in range(1, 2**N):
        gen_super_DNA(i)

    # 초염기서열의 개수 체크
    for i in range(1, 2**N):
        # superDNA[i] 값이 있으면 초염기서열 1개로 만들 수 있다는 뜻
        if superDNA[i]:
            ans[i] = 1
        else:
            gen_answer(i)