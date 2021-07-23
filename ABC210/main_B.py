def solve(S: str) -> str:
    for i in range(len(S)):
        if S[i] == "1":
            if i % 2 == 0:
                return "Takahashi"
            else:
                return "Aoki"

if __name__ == "__main__":
    n = int(input())
    s = input()
    ans = solve(s)
    print(ans)
