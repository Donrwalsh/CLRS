---
layout: clrs-solution
title:  "Exercise B.1-2"
---
>Prove the generalization of DeMorgan's laws to any finite collection of sets:
>
> $$\overline{A_1 \cap A_2 \cap \cdots \cap A_n} = \overline{A_1} \cup \overline{A_2} \cup \cdots \cup \overline{A_n}$$
>
> $$\overline{A_1 \cup A_2 \cup \cdots \cup A_n} = \overline{A_1} \cap \overline{A_2} \cap \cdots \cap \overline{A_n}$$

B.2 tells us that $$\overline{B \cap C} = \overline{B} \cup \overline{C}$$. Suppose that set $$\overline{B}$$ is composed of two smaller sets, call them $$\overline{A_1}$$ and $$\overline{A_2}$$. Then the following is true: $$\overline{A_1} \cup \overline{A_2} \cup \overline{C} = \overline{A_1 \cap A_2 \cap C} = \overline{B \cap C}$$. Now suppose $$C$$ is composed of an arbitrary number of sets, call these $$\overline{A_3}, \dots, \overline{A_n}$$. Then, by similar logic we see that $$\overline{A_1} \cap \overline{A_2} \cup \overline{A_3} \cup \cdots \cup \overline{A_n} = \overline{A_1 \cap A_2 \cap A_3 \cap \cdots \cap A_n}$$.

B.2 also tells us that $$\overline{B \cup C} = \overline{B} \cap \overline{C}$$ which we can use to craft an equivalent argument showing $$\overline{A_1 \cup A_2 \cup \cdots \cup A_n} = \overline{A_1} \cap \overline{A_2} \cap \cdots \cap \overline{A_n}$$