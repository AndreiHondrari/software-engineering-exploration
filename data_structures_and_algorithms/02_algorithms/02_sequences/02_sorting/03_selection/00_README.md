# Selection sort

## Algorithm description

Selection sorting works by using two loops. First overarching loop will iterate
over all elements from start to end.

Second, nested loop will iterate through the same elements but starting with
the next element to the right of the current master loop iteration element.

The point of the master loop is to take a potential candidate for comparison,
which is compared in the secondary loop that has the sole purpose of finding
the smallest value. As a result, the elements to the left of the current element
used by the master loop will always be sorted already, that is the algorithm
invariant.

There are two strategies by which the minimum replaces the current master
element. First method is that you immediately replace the value that is smaller,
basically having a swap operation for each successful comparison. Second
method is by keeping a reference of the smallest found element and just doing
the swap at the end of the secondary loop.
