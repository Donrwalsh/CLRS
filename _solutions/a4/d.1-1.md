---
layout: clrs-solution
title:  "Exercise D.1-1"
---
>Show that if $$A$$ and $$B$$ are symmetric $$n \times n$$ matrices, then so are $$A + B$$ and $$A - B$$.

Let $$C = A + B$$ and $$D = A - B$$. $$A$$ and $$B$$ being symmetric implies that $$a_{ij} = a_{ji}$$ and $$b_{ij} = b_{ji}$$. So for matrix $$C$$ we have:

$$\begin{split}
c_{ij} &= a_{ij} + b_{ij} \\
&= a_{ji} + b_{ji} \\
&= c_{ji} \\
\end{split}$$

and for matrix $$D$$ we have:

$$\begin{split}
d_{ij} &= a_{ij} - b_{ij} \\
&= a_{ji} - b_{ji} \\
&= d_{ji} \\
\end{split}$$

Therefore $$A+B$$ and $$A-B$$ are symmetric matrices.