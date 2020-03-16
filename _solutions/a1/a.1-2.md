---
layout: clrs-solution
title:  "Exercise A.1-2"
---
>Show that $$\sum_{k=1}^{n} 1/(2k - 1)  = \ln(\sqrt{n}) + O(1)$$ by manipulating the harmonic series.

Observe that the summation $$\sum_{k=1}^{n} 1/(2k - 1)$$ is a harmonic series from $$1$$ to $$2n$$ with all terms that have even denominators removed. With this in mind, we can express this summation as a function of modified harmonic series' in order to solve using the harmonic series identity: $$\sum\limits_{k=1}^{n}\frac{1}{k} = \ln n + O(1)$$.

$$\begin{split}
\sum\limits_{k=1}^{n} \frac{1}{2k - 1} & = 1 + \frac{1}{3} + \frac{1}{5} + \cdots + \frac{1}{2n -1 }\\
& = \sum\limits_{k=1}^{2n}\frac{1}{k} - \sum\limits_{k=1}^{n}\frac{1}{2k} \\
& = \sum\limits_{k=1}^{2n}\frac{1}{k} - \frac{1}{2} \sum\limits_{k=1}^{n}\frac{1}{k} \\
& = \ln (2n) + O(1) - \frac{1}{2}(\ln n + O(1)) \\
& = \ln n + \ln 2 + O(1) - \frac{1}{2} \ln n - \frac{1}{2} O(1) \\
& = \frac{1}{2} \ln n + O(1) \\
& = \ln (\sqrt{n}) + O(1) \\
\end{split}$$