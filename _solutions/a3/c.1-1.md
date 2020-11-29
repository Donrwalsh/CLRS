---
layout: clrs-solution
title:  "Exercise C.1-1"
---
>how many $$k$$-substrings does an $$n$$-string have? (Consider identical $$k$$-substrings at different positions to be different.) How many substrings does an $$n$$-string have in total?

Note that these substrings retain the character order found in the original string and so we are not counting all permutations. For every possible start position $$i$$ of the $$n$$-string where $$i = 1, \dots, n - k + 1$$ there exists a single $$k$$-substring beginning at $$i$$ and terminating at $$i + k - 1$$. So the number of $$k$$-substrings in an $$n$$-string is 

$$\sum\limits^{n-k+1}_{i=1} 1 = n - k + 1$$

The total number of substrings in an $$n$$-string is the sum of all possible $$k$$-substrings:

$$\begin{split}
\sum\limits^{n}_{k=1} n - k + 1 &= n^2 + n - \sum\limits^{n}_{k=1} k \\
&= n^2 + n - \frac{n(n+1)}{2} \\
&= n(n+1) - \frac{n(n+1)}{2} \\
&= \frac{n(n-1)}{2} \\
\end{split}$$   