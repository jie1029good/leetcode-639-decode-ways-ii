# LeetCode 639. Decode Ways II

## Problem

A message containing letters from A-Z can be encoded into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).

In addition to the digits, the encoded message may contain the character `*`, which can represent any digit from `1` to `9` (not `0`).

Given a string `s` containing digits and the `*` character, return the number of ways to decode it.

Since the answer may be very large, return it modulo `10^9 + 7`.

## Solution

Dynamic Programming with rolling variables (O(n) time, O(1) space).

All cases for single and two-digit decoding with `*` are fully covered.

### Python

See `solution.py`.

### Examples

- `"*"` → 9
- `"1*"` → 18
- `"2*"` → 15
