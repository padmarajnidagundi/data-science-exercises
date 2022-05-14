valores = input().split()
start, end = valores

start = int(start)
end = int(end)

if start == end:
    print("O JOGO DUROU 24 HORA (S)")
elif start > end:
    time = 24 - start + end
    print("O JOGO DUROU %d HORA (S)" %time)
elif end > start:
    time = end - start
    print("O JOGO DUROU %d HORA (S)" %time)