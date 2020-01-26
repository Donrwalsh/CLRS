### Exercise 2.1-1
**Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the array A = {31, 41, 59, 26, 41, 58}.**

| Step | 1 | 2| 3 | 4 | 5 | 6
| - | - | - | - | - | - | - |
|   | 31 | 41 | 59 | 26 | 41 | 58 |
| 1 | | | | | | | 
|   | **31** | ***41*** | 59 | 26 | 41 | 58 |
| 2 | | | | | | |
|   | **31** | **41** | ***59*** | 26 | 41 | 58 |
| 3 | ← | ← | ← | ← | | | 
|   | ***26*** | **31** | **41** | **59**  | 41 | 58 |
| 4 |  |  | ← | ← | ← | | 
|   | **26** | **31** | ***41*** | **41** | **59** | 58|
| 5 | | | | | ← | ← |
|   | **26** | **31** | **41** | **41** | ***58*** | **59**|

The idea here is that the step rows are indicating what action occurs in the row beneath them. Left-pointing arrows demonstrate that a ***number*** has been moved to a new position, and by following these arrows you can map an array element from its original position to its new destination.

### Exercise 2.1-2
**Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.**

The only necessary change is to change the `>` on line 5 to a `<`.

INSERTION-SORT(A)

1 `for  j = 2 to A.length`:

2 &nbsp;&nbsp;&nbsp;&nbsp;`key = A[j]`

3 &nbsp;&nbsp;&nbsp;&nbsp;`//Insert A[j] into the sorted sequence A[1..j-1].`

4 &nbsp;&nbsp;&nbsp;&nbsp;`i = j - 1`

5 &nbsp;&nbsp;&nbsp;&nbsp;`while i > 0 and A[i] < key`:

6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`A[i+1] = A[i]`

7 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`i = i - 1`

8 &nbsp;&nbsp;&nbsp;&nbsp;`A[i+1] = key`

### Exercise 2.1-3
**Consider the searching problem:**

***Input*: A sequence of n numbers *A = {a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>}* and a value *v*.**

***Output*: An index *i* such that *v* = *A[i]* or the special value NIL if *v* does not appear in *A*.**

**Write pseudocode for *linear search*, which scans through the sequence, looking for *v*. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.**

LINEAR-SEARCH(A, v)

1 `i = NIL`

2 `for j = 1 to A.length`:

3 &nbsp;&nbsp;&nbsp;&nbsp; `if A[j] == v`:

4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `i = j`

5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `break`

6 `return i`

*Loop Invariant*: At the start of each iteration of the for loop of lines 2-5, the subarray *A[1, ... j-1]* consists of elements that are not *v*.

**Initialization**: At initialization, the subarray contains no elements, therefore it does not contain *v*.

**Maintenance**: We already know that *A[1, ... j-1]* does not contain *v*. We then check to see if the element *A[j]* is *v* and assign it to the variable *i* if it does. We also break the for loop in this case, and will then return *i* which is the index of where *v* appears in *A*. Otherwise, we continue to the next iteration of the loop and because we did not find *v* at position *j*, the resulting array still does not contain *v* which means the invariant holds.

**Termination**: The loop will terminate when *j* is greater than the length of *A*. Since we are incrementing *j* by 1, we have thus examined each element of *A* and determined that none of them contain *v*, in which case we return NIL.

### Exercise 2.1-4
**Consider the problem of adding two *n*-bit binary integers, stored in two *n*-element arrays *A* and *B*. The sum of the two integers should be stored in binary form in an *(n + 1)*-element array *C*. State the problem formally and write pseudocode for adding the two integers.**

**Input**: An array of booleans *A = {a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>}* and an array of booleans *B = {b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>n</sub>}*, each representing an integer stored in binary format.

**Output**: An array of booleans *C = {c<sub>1</sub>, c<sub>2</sub>, ..., c<sub>n</sub>}* such that *C* = *A* + *B*.

BINARY-SUM (A, B)

1 `C = new integer[A.length + 1]`

2 `carry - 0`

3 `for i = A.length to 1`:

4 &nbsp;&nbsp;&nbsp;&nbsp; `sum = A[i] + B[i] + carry`

5 &nbsp;&nbsp;&nbsp;&nbsp; `if sum <= 1`:

6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `C[i] = sum`

7 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `carry = 0`

8 &nbsp;&nbsp;&nbsp;&nbsp; `else`:

9 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `C[i] = sum - 2`

10 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `carry = 0`

11 `C[0] = carry`

12 `return C`

### Exercise 2.2-1
**Express the function *n<sup>3</sup>/1000 - 100n<sup>2</sup> - 100n + 3* in terms of  Θ-notation.**

Θ(n<sup>3</sup>)

### Exercise 2.2-2 
**Consider sorting *n* numbers stored in array *A* by ﬁrst ﬁnding the smallest element of *A* and exchanging it with the element in *A*[1]. Then ﬁnd the second smallest element of *A*, and exchange it with *A*[2]. Continue in this manner for the ﬁrst *n-1* elements of *A*. Write pseudocode for this algorithm, which is known as *selection sort*. What loop invariant does this algorithm maintain? Why does it need to run for only the ﬁrst *n-1* elements, rather than for all *n* elements? Give the best-case and worst-case running times of selection sort in Θ-notation.**

SELECTION-SORT (A)

1 `for i = 1 to A.length - 1`:

2 &nbsp;&nbsp;&nbsp;&nbsp; `smallest_val = A[i]`

3 &nbsp;&nbsp;&nbsp;&nbsp; `smallest_pos = i`

4 &nbsp;&nbsp;&nbsp;&nbsp; `for j = i+1 to A.length`:

5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `if A[j] < smallest_val:`

6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `smallest_val = A[j]`

7 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `smallest_pos = j`

8 &nbsp;&nbsp;&nbsp;&nbsp; `A[smallest_pos] = A[i]`

9 &nbsp;&nbsp;&nbsp;&nbsp; `A[i] = smallest_val`

10 `return A`

*Loop Invariant* At the start of each iteration of the loop in lines 1-9, the subarray *A*[1, ... i-1] contains the smallest elements of A in increasing order. At the start of each iteration of the loop in lines 5-7, the smallest_val variable contains the smallest element of the subarray *A*[i, ... j-1] and the smallest_pos variable contains that value's position in the array.

We only need to run this algorithm for the first *n-1* elements of the array because it is 'forward-looking'. The *n*th element has nothing to be compared against and is therefore trivially the smallest element remaining (which is to say, the largest element).

Both the best and worst case running times are Θ(n<sup>2</sup>).

### Exercise 2.2-3
**Consider linear search again (see Exercise 2.1-3). How many elements of the input sequence need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? What are the average-case and worst-case running times of linear search in Θ-notation? Justify your answers.**

On average, we would be examining *n/2* elements before finding our desired value. In the worst-case, we would need to look at all *n* elements. In both of these cases, *n* is the only significant figure therefore both running times are Θ(n<sup>2</sup>).

### Exercise 2.2-4
**How can we modify almost any algorithm to have a good best-case running time?**

An approach that would work for any algorithm would be to include a 'truth-check' that rapidly verifies whether or not the input already satisfies the requirements of the desired output. For a sorting algorithm, we would look at the input array and determine if it is already sorted. This would result in a very fast best-case scenario, but sort of defeats the purpose of the underlying algorithm at the same time.

### Exercise 2.3-1
**Using Figure 2.4 as a model, illustrate the operation of merge sort on the array A = {3, 41, 52, 26, 38, 57, 9, 49}**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[03, 09, 26, 38, 41, 49, 52, 57]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⬈ merge ⬉

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[03, 26, 41, 52]`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[09, 38, 49, 57]`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⬈ merge ⬉&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⬈ merge ⬉

&nbsp;&nbsp;&nbsp;`[03, 41]`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[26, 52]`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[38, 57]`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[09, 49]`

&nbsp;&nbsp;&nbsp;⬈ merge ⬉&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⬈ merge ⬉&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⬈ merge ⬉&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⬈ merge ⬉

&nbsp;`[03]`&nbsp;&nbsp;&nbsp;`[41]`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[52]`&nbsp;&nbsp;&nbsp;`[26]`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[38]`&nbsp;&nbsp;&nbsp;`[57]`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[09]`&nbsp;&nbsp;&nbsp;`[49]`

### Exercise 2.3-2
**Rewrite the MERGE procedure so that it does not use sentinels, instead stopping once either array *L* or *R* has had all its elements copied back to *A* and then copying the remainder of the other array back into *A*.**

MERGE-SORT (A, p, q, r)

01 `n₁ = q - p + 1`

02 `n₂ = r - q`

03 `Let L[1 . . n₁] and R[1 . . n₂] be new arrays`

04 `for i = 1 to n₁`

05 &nbsp;&nbsp;&nbsp;&nbsp; `L[i] = A[p + i - 1]`

06 `for j = 1 to n₂`

07 &nbsp;&nbsp;&nbsp;&nbsp; `R[j] = A[q + j]`

08 `i = 1`

09 `j = 1`

10 `for k = p to r`

11 &nbsp;&nbsp;&nbsp;&nbsp; `j > n₂`

12 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `A[k] = L[i]`

13 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `i = i + 1`

14 &nbsp;&nbsp;&nbsp;&nbsp; `else if if i > n₁`

15 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `A[k] = R[j]`

16 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `j = j + 1`

17 &nbsp;&nbsp;&nbsp;&nbsp; `else if L[i] ≤ R[j]`

18 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `A[k] = L[i]`

19 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `i = i + 1`

20 &nbsp;&nbsp;&nbsp;&nbsp; `else`

21 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `A[k] = R[j]`

22 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `j = j + 1`

### Exercise 2.3-3
**Use mathematical induction to show that when *n* is an exact power of 2, the solution of the recurrence**

**T(n) = { 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if n = 2**

** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ 2T(n/2) + n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if n = 2<sup>k</sup>, for k > 1**

**is T(n) = *n*lg*n***

In the base case, *k* = 1, and so *n* = 2<sup>1</sup>. *T*(*n*) = *n*lg*n* = 2·lg(2<sup>1</sup>) = 2·1 = 2. 

Next we suppose this holds for any *k* > 1, and will show that it also holds for any *k* + 1:

*T*(*n*/2) + *n* = *n*lg*n*

2[(2<sup>*k* + 1</sup>/2)·lg(2<sup>*k* + 1</sup>/2)] + 2<sup>*k* + 1</sup> = 2<sup>*k* + 1</sup>lg2<sup>*k* + 1</sup>

2{[2<sup>*k* + 1</sup>/2]·[lg(2<sup>*k* + 1</sup>/2) - lg2] + 2<sup>*k* + 1</sup> = 2<sup>*k* + 1</sup>(*k* + 1)

2{[2<sup>*k* + 1</sup>/2]·[*k* + 1 - 1] + 2<sup>*k* + 1</sup> = 2<sup>*k* + 1</sup>(*k* + 1)

2<sup>*k* + 1</sup>·*k* + 2<sup>*k* + 1</sup> = 2<sup>*k* + 1</sup>(*k* + 1)

2<sup>*k* + 1</sup>(*k* + 1) = 2<sup>*k* + 1</sup>(*k* + 1)

