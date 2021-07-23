def solve(N: int, A: int, X: int, Y: int) -> int:
    if N <= A:
        return N * X

    return A * X + (N - A) * Y

if __name__ == "__main__":
    n, a, x, y = map(int, input().split())
    ans = solve(n, a, x, y)
    print(ans)
