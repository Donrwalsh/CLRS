---
layout: clrs-solution
title:  "Exercise A.1-6"
---
>Prove that $$\sum\limits^{\infty}_{k=1} O(f_k(i)) = O\left(\sum\limits^{n}_{k=1} f_k(i) \right)$$ by using the linearity property of summations.

Let $$g_1, g_2, \dots, g_n$$ be any functions such that $$g_k(i) = O(f_k(i))$$. By definition, there exist constants $$c_1, c_2, \dots, c_n \ni g_k(i) \leq c_k f_k (i)$$. Take the maximum value of $$c_k$$ where $$1 \leq k \leq n$$. This gives us

$$\begin{split}
\sum\limits^{n}_{k=1} g_k (i) & \leq \sum\limits^{n}_{k=1} c_k f_k (i) \\
& \leq c \sum\limits^{n}_{k=1} f_k(i) \\
&= O \left( \sum\limits^{n}_{k=1} f_k (i) \right)
\end{split}$$