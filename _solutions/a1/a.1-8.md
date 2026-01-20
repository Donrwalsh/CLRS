---
layout: clrs-solution
title: "Exercise A.1-8"
---

> Evaluate the product $$ \prod^n_{k=2} (1 - \frac{1}{k^2})$$.

Expanding this product creates a pattern in which we can cancel out all but the first and last numerator and the first and last denominator:

$$\begin{split}
\require{cancel}
\prod\limits^n_{k=2} (1 - \frac{1}{k^2}) &= \prod\limits^n_{k=2} \frac{(k-1)(k+1)}{k^2} \\
&= \frac{1 \cdot 3}{2 \cdot 2} \cdot \frac{2 \cdot 4}{3 \cdot 3} \cdot \frac{3 \cdot 5}{4 \cdot 4} \cdots \frac{(n-1)(n+1)}{n \cdot n} \\
&= \frac{1 \cdot \cancel{3}}{2 \cdot \cancel{2}} \cdot \frac{\cancel{2} \cdot \cancel{4}}{\cancel{3} \cdot \cancel{3}} \cdot \frac{\cancel{3} \cdot \cancel{5}}{\cancel{4} \cdot \cancel{4}} \cdots \frac{\cancel{(n-1)}(n+1)}{\cancel{n} \cdot n} \\
&= \frac{n+1}{2n}
\end{split}$$

