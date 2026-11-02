class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 1_000_000_007
        a, b = 0, 1          # a=dp[i-2], b=dp[i-1]
        
        for i, ch in enumerate(s):
            c = 0
            
            # Single character decoding
            if ch == '*':
                c = 9 * b % MOD
            elif ch != '0':
                c = b
            
            # Two characters decoding
            if i > 0:
                prev = s[i - 1]
                if prev == '*' and ch == '*':
                    c = (c + 15 * a) % MOD
                elif prev == '*':
                    c = (c + (2 if ch <= '6' else 1) * a) % MOD
                elif ch == '*':
                    if prev == '1':
                        c = (c + 9 * a) % MOD
                    elif prev == '2':
                        c = (c + 6 * a) % MOD
                else:
                    if prev == '1' or (prev == '2' and ch <= '6'):
                        c = (c + a) % MOD
            
            a, b = b, c
        
        return b
