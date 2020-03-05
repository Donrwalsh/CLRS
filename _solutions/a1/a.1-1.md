---
layout: clrs-solution
title:  "Exercise A.1-1"
---
>Find a simple formula for $$\sum_{k=1}^{n}(2k-1)$$.

Solved by using the arithmetic series identity: $$\sum\limits_{k=1}^{n}k = \frac{1}{2}n(n + 1)$$.

$$\begin{split}
\sum\limits_{k=1}^{n}(2k-1) & = 2\sum\limits_{k=1}^{n}k - \sum\limits_{k=1}^{n} 1 \\
& = 2 \cdot \frac{1}{2}n(n+1) - n \\
& = n^2 + n - n \\
& = n^2 \\
\end{split}$$