---
layout: clrs-solution
title:  "Exercise A.2-1"
---
>Show that $$\sum\limits_{k=1}^n \frac{1}{k^2}$$ is bounded above by a constant.

Intuitively this summation is bound above by the constant $$2$$. 

Using the techniques from this appendix section, note that we are dealing with a monotonically decreasing function and so we can use a form of (A.12) to show this.

$$\begin{split}
\sum\limits^n_{k=1} \frac{1}{k^2} &= 1 + \sum\limits_{k=2}^n \frac{1}{k^2} \\
&\leq 1+ \int_1^n \frac{dx}{x^2} \\
&= 1 + \left( - \left.\frac{1}{n}\right|^{n}_1 \right)\\
&= 1 + \left(- \frac{1}{n} - \left( - \frac{1}{1}\right) \right) \\
&= 1 - \frac{1}{n} + 1 \\
&= 2 - \frac{1}{n} \\
&\leq 2 \\
\end{split}$$