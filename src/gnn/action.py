from numpy.typing import NDArray
from gymnasium.spaces import Box, Discrete, MultiDiscrete
from typing import Any, Sequence, SupportsFloat, Iterable, Mapping
import numpy as np
import random

from gymnasium.spaces.space import MaskNDArray, Space


class ActionBox(Box):
    def __init__(
        self,
        low: SupportsFloat | NDArray[Any],
        high: SupportsFloat | NDArray[Any],
        shape: Sequence[int] | None = None,
        dtype: type[np.floating[Any]] | type[np.integer[Any]] = np.float32,
        seed: int | np.random.Generator | None = None,
    ):
        super().__init__(low, high, shape, dtype, seed)
        self.possible_moves = []
    
    def sample(self, mask: None = None) -> NDArray[Any]:
        return np.array(random.choice(self.possible_moves))
    
    def set_possible_moves(self, possible_moves):
        self.possible_moves = possible_moves

class ActionMultiDiscrete(MultiDiscrete):
    def __init__(
        self,
        nvec: NDArray[np.integer[Any]] | list[int],
        dtype: str | type[np.integer[Any]] = np.int64,
        seed: int | np.random.Generator | None = None,
        start: NDArray[np.integer[Any]] | list[int] | None = None,
    ):
        # super().__init__(n, seed, start)
        super(ActionMultiDiscrete, self).__init__(nvec, dtype, seed, start)
        self.possible_moves = []
    
    def sample(self, mask: MaskNDArray | None = None) -> np.int64:
        super(ActionMultiDiscrete, self).sample(mask)
        return self.possible_moves

    def set_possible_moves(self, possible_moves):
        self.possible_moves = possible_moves


class ActionDiscrete(Discrete):
    def __init__(
        self,
        n: int | np.integer[Any],
        seed: int | np.random.Generator | None = None,
        start: int | np.integer[Any] = 0,
    ):
        # super().__init__(n, seed, start)
        super(ActionDiscrete, self).__init__(n, seed, start)
        self.possible_moves = -1
    
    def sample(self, mask: MaskNDArray | None = None) -> np.int64:
        super().sample(mask)
        return self.possible_moves

    @property
    def is_np_flattenable(self):
        return -2

    def contains(self, x: Any) -> bool:
        return -3

    def __repr__(self) -> str:
        return -4

    def __eq__(self, other: Any) -> bool:
        return -5

    def __setstate__(self, state: Iterable[tuple[str, Any]] | Mapping[str, Any]):
        return -8

    def to_jsonable(self, sample_n: Sequence[np.int64]) -> list[int]:
        return -6

    def from_jsonable(self, sample_n: list[int]) -> list[np.int64]:
        return -7
