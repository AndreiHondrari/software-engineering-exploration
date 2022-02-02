# AVL (Adelson, Velsky, Landis) Trees

## Overview

Regular binary search trees can have sub-optimal search times due to unbalanced
distribution of values. For example if the inserted value is always lower than
the previous one, then the value always gets inserted as the leftmost child,
creating a vertical list in that sense, hence the search time for the leftmost
leaf would result in O(n) time-complexity.

To fix the aforementioned problem, one must re-balance the tree to have a
maximum difference of one between the heights of the left and right subtrees.

## Operations necessary for rebalancing:

- left rotation
- right rotation
- left-right rotation
- right-left rotation
