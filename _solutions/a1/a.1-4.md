---
layout: clrs-solution
title:  "Exercise A.1-4"
---
>Show that $$\sum\limits^{\infty}_{k=0} \frac{(k-1)}{2^k} = 0$$.

We can use formulas A.6 and A.8 to deconstruct this summation:

$$\begin{split}
\sum\limits^{\infty}_{k=0} \frac{(k-1)}{2^k} &= \sum\limits^{\infty}_{k=0} \frac{k}{2^k} - \sum\limits^{\infty}_{k=0} \frac{1}{2^k} \\
&= \sum\limits^{\infty}_{k=0} \frac{k}{2^k} - \frac{1}{1 - \frac{1}{2}} \\
&= \sum\limits^{\infty}_{k=0} k \left( \frac{1}{2} \right)^k - 2 \\
&= \sum\limits^{\infty}_{k=0} \frac{\frac{1}{2}}{\left(1 - \frac{1}{2} \right)^2} - 2 \\
&= \frac{1/2}{1/4} - 2 \\
&= 2 - 2 \\
&= 0 \\
\end{split}$$