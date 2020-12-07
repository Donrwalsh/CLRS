---
layout: clrs-solution
title:  "Exercise D.1-2"
---
>Prove that $$(AB)^T = B^TA^T$$ and that $$A^TA$$ is always a symmetric matrix.

Recall that the transpose of a matrix is the switching of rows and columns. This gives us

$$\begin{split}
(AB)^{T}_{ij} &= (AB)_{ji} \\
&= \sum\limits^{n}_{k=1} a_{jk}b_{ij}\\
&= \sum\limits^{n}_{k=1} b_{ij}a_{jk}\\
&= (B^TA^T)_{ij}
\end{split}$$ 

which shows us that $$(AB)^T = B^T A^T$$. This logic can be directly applied to the second part of the question:

$$(A^TA)^T = A^T(A^T)^T = A^T A$$

So $$A^T A$$ is by definition symmetric.