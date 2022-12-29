---
layout: clrs-solution
title:  "Exercise A.1-5"
---
>Evaluate the sum $$\sum\limits^{\infty}_{k=1}(2k+1)x^2k$$ for $$\lvert x \rvert < 1$$.

$$(2k+1)x^2k$$ looks familiar in that it is the derivative of $$x^{2k+1}$$. Let's work backwards to derive a solution.

$$\begin{split}
\sum\limits^{\infty}_{k=1}x^k &= \frac{x}{1-x} \\
\sum\limits^{\infty}_{k=1}(x^2)^k &= \frac{x^2}{1-x^2} \\
\sum\limits^{\infty}_{k=1}xx^{2k} &= \frac{x^3}{1-x^2} \\
\sum\limits^{\infty}_{k=1}x^{2k+1} &= \frac{x^3}{1-x^2} \\
\sum\limits^{\infty}_{k=1}(2k+1)x^{2k} &= \frac{3x^2(1-x^2)+2x^4}{(1-x^2)^2} \\
\sum\limits^{\infty}_{k=1}(2k+1)x^{2k} &= \frac{3x^2-x^4}{(1-x^2)^2} \\
\end{split}$$ 

for $$\lvert x \rvert < 1$$.