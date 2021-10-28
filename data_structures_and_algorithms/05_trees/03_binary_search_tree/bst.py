import dataclasses as dc
from typing import Optional

from tree_structure import Node


@dc.dataclass
class BinarySearchTree:
    root: Optional[Node] = None
