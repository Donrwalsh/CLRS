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
