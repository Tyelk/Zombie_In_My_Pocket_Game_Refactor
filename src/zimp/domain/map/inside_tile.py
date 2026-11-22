from zimp.domain.common.direction import Direction
from zimp.domain.common.tile_effect import TileEffect
from zimp.domain.map.tile import Tile


class InsideTile(Tile):
    """A tile for the inside area of the map."""

    def __init__(self, tile_id: int, doors: tuple[Direction, ...],
                 effect: TileEffect = TileEffect.NONE,
                 is_exit_tile: bool = False) -> None:
        super().__init__(tile_id, doors, effect)
        self.__is_exit_tile = is_exit_tile

    def is_outside(self) -> bool:
        return False

    def is_exit(self) -> bool:
        return self.__is_exit_tile
