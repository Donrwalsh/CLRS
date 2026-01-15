---
layout: clrs-solution
title: "Exercise A.1-7"
---

> Evaluate the product $$ \prod_{k=1}^n 2 \cdot 4^k$$

This expression can be rearranged a few times by taking advantage of identities found in this appendix. We start by taking the log of the product to turn it into a summation:

$$\begin{split}
&  \lg \left( \prod\limits_{k=1}^n 2 \cdot 4^k \right) \\
&= \sum\limits^{n}_{k=1} \lg (2 \cdot 4^k)\\
&= \sum\limits^{n}_{k=1} \lg(2) + k \lg (4)\\
&= \left( \lg(2) \sum\limits^{n}_{k=1} 1 \right) + \left( \lg(4) \sum\limits^{n}_{k=1} \right) \\
&= n + 2\frac{n(n+1)}{2} \\
&= n(n+2)
\end{split}$$

In order to unwind the applied log in the first step, we raise $$2$$ to the power of our result:

$$2^{n(n+2)} = 2^{n^2} \cdot 4^n$$