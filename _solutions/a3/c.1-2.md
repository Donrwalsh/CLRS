---
layout: clrs-solution
title:  "Exercise C.1-2"
---
>An $$n$$-input, $$m$$-output ***boolean function*** is a function from $$\{TRUE, FALSE\}^n$$ to $$\{TRUE, FALSE\}^m$$. How many $$n$$-input, $$1$$-output boolean functions are there? How many $$n$$-input, $$m$$-output boolean functions are there?

First of all, these inputs are simply $$n$$ length binary strings of which there are $$2^n$$ possible forms.  For single-output boolean functions ($$m=1$$) each possible input corresponds to 2 possible outputs, and so the total number of possible $$n$$-input, $$1$$-output boolean functions is $$2^{2^n}$$.

Generalizing this approach for arbitrary values of $$m$$ gives us $$2^m$$ possible outputs and so the total number of $$n$$-input, $$m$$-output boolean functions is $$2^{m2^n}$$.