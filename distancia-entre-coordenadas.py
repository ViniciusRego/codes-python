import math

def distancia(Xa, Ya, Xb, Yb):
    return math.sqrt((Xb - Xa)**2 + (Yb - Ya)**2)

def main():
    N = int(input())  # Quantidade de pares de pontos
    for a in range(N):
        Xa, Ya, Xb, Yb = map(int, input().split())
        result = distancia(Xa, Ya, Xb, Yb)
        print(f"{result:.2f}")

if __name__ == "__main__":
    main()
