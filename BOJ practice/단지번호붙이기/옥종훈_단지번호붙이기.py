from collections import deque


def numbering():
    result = []

    # homes를 순회하며 단지를 만나면 result에 단지 수를 저장
    # 저장한 이후 해당 단지들은 0으로 초기화
    for i in range(n):
        for j in range(n):
            if homes[i][j]:
                result.append(bfs((i, j)))

    # 각 단지내 집의 수가 저장된 result를 오름차순으로 정렬
    result.sort()

    print(len(result))
    # 정렬된 결과 출력
    for element in result:
        print(element)


def bfs(v):
    ans = 0
    q = deque([v])
    visited = [v]

    while q:
        t = q.popleft()
        # 상하좌우를 확인하여 집이 있으면 q에 추가
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]
            # nx, ny가 homes의 범위를 벗어나지 않고
            if 0 <= nx < n and 0 <= ny < n:
                # 해당 위치에 방문하지 않은 집이 있으면 추가
                if homes[nx][ny] and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.append((nx, ny))
    for w in visited:
        homes[w[0]][w[1]] = 0
        ans += 1

    return ans


n = int(input())
homes = [list(map(int, input())) for _ in range(n)]
numbering()
# print(homes)