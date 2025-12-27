---
layout: clrs-solution
title: "Exercise B.1-3"
---

> Prove the generalization of equation (B.3), which is called the **principle of inclusion and exclusion**:
>
> $$
> \begin{align*}
> \lvert A_1 \cup A_2 \cup \cdots A_n \rvert = &\lvert A_1 \rvert + \lvert A_2 \rvert + \cdots + \lvert A_n \rvert \\
> & - \lvert A_1 \cap A_2 \rvert - \lvert A_1 \cap A_3 \rvert - \cdots & \text{(all pairs)} \\
> & + \lvert A_1 \cap A_2 \cap A_3 \rvert + \cdots & \text{(all triples)} \\
> & \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \vdots \\
> & + (-1)^{n-1} \lvert A_1 \cap A_2 \cap \cdots \cap A_n \rvert \\
> \end{align*}
> $$

Equation B.3 tells us that $$ \lvert A_1 \cup A_2 \rvert = \lvert A_1 \rvert + \lvert A_2 \rvert - \lvert A_1 \cap A_2 \rvert$$. Intuitively, we know that $$ \lvert A_1 \cup A_2 \rvert = \lvert A_1 \rvert + \lvert A_2 \rvert$$ iff $$A_1$$ and $$A_2$$ contain values entirely distinct from one another. When this is not the case, we need to account for any values that appear in both $$A_1$$ and $$A_2$$ since they will have been double-counted by $$\lvert A_1 \rvert + \lvert A_2 \rvert$$, hence the final term where we subtract the count of values contained within the intersection of the two sets ($$... - \lvert A_1 \cap A_2 \rvert$$ ).

Suppose we have a value $$x$$ that appears in $$r$$ of the sets $$A_1, A_2, ..., A_n$$. During the first portion of the formula we aim to prove, the amount of terms in each set is counted and so we would expect $$x$$ to appear $$r$$ times during this count. For reasons that will become clear in a moment, note that this value can also be represented as $$\binom{r}{1}$$.

Next, consider the portion of the equation where we handle pairs of sets. We are subtracting the intersection result of every possible pair of sets, so we want to know how many distinct pairs of sets that both contain $$x$$ can we form? This is the exact definition of a binomial coefficient, and so we know that there are $$\binom{r}{2}$$ possible pairs that both contain x. Finally, we subtract this term: $$- \binom{r}{2}$$.

Next, we have $$\binom{r}{3}$$ triplets where all three sets contain $$x$$. This term is added.

To generalize, when we consider $$k$$-wise intersections there are $$\binom{r}{k}$$ such interesections and the contribution to the overall count must consider the alternating positive and negative contribution as k changes: $$(-1)^{k+1}\binom{r}{k}$$. So, the total number of times that $$x$$ is counted by the above formula is

$$\sum^{r}_{k=1} (-1)^{k+1} \binom{r}{k}$$

This expression evaluates to $$1$$ when $$r \ge 1$$ and $$0$$ otherwise. Therefore a universe of possible $$x$$s which may or may not appear in one ore more $$A$$s, we know that each of them will be counted only once across the various pairs, triplets, etc. that are being added and subtracted from the final result. Any $$x$$ value that is not present in any $$A$$ will receive a count of $$0$$ and so we see that the **principle of inclusion and exclusion** follows directly from equation B.3.
