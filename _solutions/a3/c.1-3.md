---
layout: clrs-solution
title:  "Exercise C.1-3"
---
>In how many ways can $$n$$ professors sit around a circular conference table? Consider two seatings to be the same if one can be rotated to form the other.

Note that this is not the same as counting permutations based on the rotation detail in the exercise description.

Start by placing the first professor. In the next position there are $$n-1$$ possible professors to be placed. After placing the second professor, there are $$n-2$$ possible placements for the next position. This pattern continues until there is only one professor to be placed. We need not concern ourselves with adjusting the first (or any other) placement due to the circular nature of the table.

By multiplying all these choices together, we see that there are $$(n-1) \cdot (n-2) \cdots 1 = (n-1)!$$ ways to seat $$n$$ professors around a circular table.