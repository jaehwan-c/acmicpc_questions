n, m, w, h = map(int, input().split())
print(min(n, m, abs(n-w), abs(m-h), abs(w-n), abs(h-m)))