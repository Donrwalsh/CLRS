---
layout: clrs-solution
title:  "Exercise A.1-3"
---
>Show that $$\sum\limits^{\infty}_{k = 0} k^2 x^k = x(1+x)/(1-x)^3$$ for $$\lvert x \rvert < 1$$.

Based on equation A.8 we know that 

$$\sum\limits^{\infty}_{k=0} kx^k = \frac{x}{(1-x)^2}$$

for $$\lvert x \rvert$$. This isn't quite the equation we want, so let's differentiate each side of it:

$$\begin{split}
\sum\limits^{\infty}_{k=0} k \cdot kx^{k-1} &= \frac{(1-x)^2 + 2x(1-x)}{(1-x)^4} \\
&= \frac{(1-x) + 2x}{(1-x)^3} \\
&= \frac{1+x}{(1-x)^3} \\
\end{split}$$

Finally, we multiply both sides by $$x$$ to reach the desired result:

$$\sum\limits^{\infty}_{k = 0} k^2 x^k = \frac{x(1+x)}{(1-x)^3}$$