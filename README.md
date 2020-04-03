# baekjoon

>백준 문제풀이 코드와 설명을 남기기 위한 레포지터리입니다.

* Deque (double-ended queue)
    <p>
    스택과 큐가 결합한 형태이다. 기본 큐에 pop을 하는 경우 O(n)의 비용이 드는데,<br>
    popleft()를 하면 O(1)로 해결가능.
    </p>     
```python
from collection import deque

q = deque.Deque()
q.popleft()
```