def raiz_b(a, b):
    return pow(a, 1 / b)

def main():
    a, b = map(int, input().split())
    result = raiz_b(a, b)
    print(int(result))

if __name__ == "__main__":
    main()
