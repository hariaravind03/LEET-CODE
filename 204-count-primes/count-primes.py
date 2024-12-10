class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if prime[p]:
                prime[p*p:n:p] = [False]*((n-1-p*p)//p + 1)
        return sum(prime)