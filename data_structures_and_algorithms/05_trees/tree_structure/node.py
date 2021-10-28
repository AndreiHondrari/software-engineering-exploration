import random
import dataclasses as dc
from typing import Optional, Any, ClassVar


@dc.dataclass
class Node:
    value: Any
    parent: Optional['Node'] = dc.field(default=None, repr=False)
    left: Optional['Node'] = dc.field(default=None, repr=False)
    right: Optional['Node'] = dc.field(default=None, repr=False)

    control_id: int = dc.field(
        init=False,
        repr=False,
        default_factory=lambda: random.randint(0, 10_000_000)
    )
    count: ClassVar[int] = 0
