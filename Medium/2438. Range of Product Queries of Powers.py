class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7
        powers = []
        bit = 0
        while (1 << bit) <= n:
            if (n >> bit) & 1:
                powers.append(1 << bit)
            bit += 1
        prefix = [powers[0] % MOD]
        for i in range(1, len(powers)):
            prefix.append((prefix[-1] * powers[i]) % MOD)
        def mod_inv(x):
            return pow(x, MOD - 2, MOD)
        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix[r])
            else:
                res.append((prefix[r] * mod_inv(prefix[l - 1])) % MOD)
        return res
