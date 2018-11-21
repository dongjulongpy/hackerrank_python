n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    func = input().split()

    if func[0] == 'pop':
        s.pop()
    elif func[0] == 'remove':
        s.remove(int(func[1]))
    elif func[0] == 'discard':
        s.discard(int(func[1]))       

print(sum(s))
