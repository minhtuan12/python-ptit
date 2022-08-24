def solve(s):
    for i in range(0, len(s), 2):
        print(s[i] * int(s[i + 1]), end = "")

def main():
    t = int(input())
    for i in range(t):
        s = input()
        solve(s)
        print(end = "\n")

if __name__ == "__main__":
    main()
    