#!/usr/bin/env python3
f1 = lambda x: (not(x%3) or not(x%5))
print(sum(filter(f1, range(1000))))





