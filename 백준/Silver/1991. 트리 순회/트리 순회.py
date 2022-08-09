N = int(input())
node_list = {}

for _ in range(N):
    d, l, r = input().split()
    node_list[d] = [l, r]

answer = ''
def pre(node):
    global answer
    answer += node
    if node_list.get(node)[0] != '.':
        pre(node_list.get(node)[0])
    if node_list.get(node)[1] != '.':
        pre(node_list.get(node)[1])

pre('A')
print(answer)

answer = ''
def In(node):
    global answer
    if node_list.get(node)[0] != '.':
        In(node_list.get(node)[0])
    answer += node
    if node_list.get(node)[1] != '.':
        In(node_list.get(node)[1])

In('A')
print(answer)

answer = ''
def post(node):
    global answer
    if node_list.get(node)[0] != '.':
        post(node_list.get(node)[0])
    if node_list.get(node)[1] != '.':
        post(node_list.get(node)[1])
    answer += node

post('A')
print(answer)