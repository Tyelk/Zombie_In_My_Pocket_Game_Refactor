from zimp.domain.common.direction import Direction
from zimp.domain.common.tile_effect import TileEffect
from zimp.domain.map.tile import Tile


class OutsideTile(Tile):
    """A tile for the outside area of the map."""

    def __init__(self, tile_id: int, doors: tuple[Direction, ...],
                 effect: TileEffect = TileEffect.NONE,
                 is_entry_tile: bool = False) -> None:
        super().__init__(tile_id, doors, effect)
        self.__is_entry_tile = is_entry_tile

    def is_outside(self) -> bool:
        return True

    def is_entry(self) -> bool:
        return self.__is_entry_tile
