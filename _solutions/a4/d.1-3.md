---
layout: clrs-solution
title: "Exercise D.1-3"
---

> Prove that the product of two lower-triangular matrices is lower-triangular.

Let $$A = (a_{ij})$$ and $$B = (b_{ij})$$ be two $$n \times n$$ lower-triangular matrices. By definition, $$A$$ being lower-triangular means $$a_{ij} = 0$$ for all $$i < j$$ and $$B$$ being lower-triangular means $$b_{ij} = 0$$ for all $$i < j$$. 

Let $$C$$ be their product: $$C = AB = (c_{ij})$$, where $$c_{ij} = \sum\limits_{k=1}^n a_{ik}b_{kj}$$. We will show that this product is also lower-triangular: $$c_{ij} = 0$$ for all $$i < j$$:

$$\begin{split}
c_{ij} &= \sum\limits_{k=1}^n a_{ik}b_{kj} \\
&= \sum\limits_{k=1}^{j-1} a_{ik} b_{kj} + \sum\limits_{k=j}^n a_{ik} b_{kj} \\
&= \sum\limits_{k=1}^{j-1} a_{ik} 0 + \sum\limits_{k=j}^n 0 b_{kj} \\
&= \sum\limits_{k=1}^{j-1} 0 + \sum\limits_{k=j}^n 0 \\
&= 0 + 0 \\
&= 0
\end{split}$$ 