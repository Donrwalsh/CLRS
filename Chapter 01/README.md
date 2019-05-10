### Exercise 1.1-1
**Give a real-world example that requires sorting or a real-world example that requires computing a convex hull.**

Sorting: Alphabitizing the names of employees in order to count how many Johns are employed.

[Convex Hull](https://en.wikipedia.org/wiki/Convex_hull): Crafting dice of various sides (d12, d20, etc.)

### Exercise 1.1-2
**Other than speed, what other measures of efﬁciency might one use in a real-world setting**

Memory; wear-and-tear on physical hardware.

### Exercise 1.1-3
**Select a data structure that you have seen previously, and discuss its strengths and limitations.**

Human memory. Incredible ability to recall specific information on demand, but practically incapable of accurately describing it in its entirety (Have you seen this movie versus tell me every movie you've seen). Subject to unreliable precision as well as deterioration over time.

### Exercise 1.1-4
**How are the shortest-path and traveling-salesman problems given above similar? How are they different?**

They are similar in that they both deal with a map and care about the distance between points (cities and roads for example). Additionally, each problem seeks to produce a route that minimizes distance. They differ in that the shortest-path problem has a defined beginning point and end point with no stipulations on which or how many points must be traversed from beginning to end. The travelling salesman problem instead cares about hitting every destination along the way while ending at the original beginning point - this difference complicates the problem greatly.

### Exercise 1.1-5
**Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is “approximately” the best is good enough.**

Only-the-best: The methods and procedures used by surgeons during life-saving operations must use only the best available approach given the current understanding of medical science. Lives are literally on the line.

"apporximately"-the-best: The algorithm used by a cashier to determine proper change for a purchase need not be efficient, so long as it produces the correct figure.

### Exercise 1.2-1
**Give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved.**

On my phone, I have a list of contacts. I am able to sort this list by names (first or last), date added, date used, birthday and more. This application must include some sort of sorting algorithm as another user may have an entirely different list of contacts, but would need them to be sorted quickly just the same as me.

### Exercise 1.2-2
**Suppose weare comparing implementations of insertion sort and merge sort on the same machine. For inputs of size *n*, insertion sort runs in 8*n*<sup>2</sup> steps, while merge sort runs in 64*n*lg*n* steps. For which values of *n* does insertion sort beat merge sort**

First of all, 8*n*<sup>2</sup> < 64*n*lg*n* reduces to *n* < 8lg*n*. Next I used `sort_compare.py` to determine when insertion sort overtakes merge sort, which is at *n* = 43. (hilariously, this script wasn't doing what I wanted it to until I set n to start at 2 instead of 1)

### Exercise 1.2-3
**What is the smallest value of n such that an algorithm whose running time is 100*n*<sup>2</sup> runs faster than an algorithm whose running time is 2<sup>n</sup> on the same machine?**

I wrote `algorithm_compare.py` to calculate that the lowest value of *n* that satisfies this condition is 15.

### Problem 1-1 Comparison of running times 
**For each function *f(n)* and time *t* in the following table, determine the largest size *n* of a problem that can be solved in time *t*, assuming that the algorithm to solve the problem takes *f(n)* microseconds.**

I wrote `running_time_compare.py` to solve this table. The numbers got pretty big, so I used some techniques to simplify the figures. 

| | 1 second | 1 minute | 1 hour | 1 day | 1 month | 1 year | 1 century
| - | - | - | - | - | - | - | - |
| lg *n* | 2<sup>10<sup>6</sup></sup> | 2<sup>6*10<sup>7</sup></sup> | 2<sup>3.6*10<sup>9</sup></sup> | 2<sup>8.64*10<sup>10</sup></sup> | 2<sup>2.59*10<sup>12</sup></sup> | 2<sup>3.15*10<sup>13</sup></sup> | 2<sup>3.15*10<sup>15</sup></sup>
| sqrt(*n*) | 10<sup>12</sup> | 3.6*10<sup>15</sup> | 1.3*10<sup>19</sup> | 7.47*10<sup>21</sup> | 6.72*10<sup>24</sup> | 9.95*10<sup>26</sup> | 9.96*10<sup>30</sup>
| *n* | 10<sup>6</sup> | 6*10<sup>7</sup> | 3.6*10<sup>9</sup> | 8.64*10<sup>10</sup> | 2.6*10<sup>12</sup> | 3.15*10<sup>13</sup> | 3.15*10<sup>15</sup>
| *n* lg *n* | 62,746 | 2,801,417 | 133,378,058 | 2,755,147,513 | 71,870,856,404 | 797,633,893,349 | 68,610,956,750,570
| n<sup>2</sup> | 1,000 | 7,745 | 60,000 | 293,398 | 1,609,968 | 5,615,692 | 56,156,922
| n<sup>3</sup> | 100| 391 | 1,532 | 4,420 | 13,736 | 31,593 | 146,645
| 2<sup>*n*</sup> |19 | 25 | 31 | 36 | 41 | 44 | 51
| *n*! | 9 | 11 | 12 | 13 | 15 | 16 | 17



