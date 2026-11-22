from zimp.domain.common.direction import Direction
from zimp.domain.common.tile_effect import TileEffect
from zimp.domain.map.inside_tile import InsideTile
from zimp.domain.map.tile import Tile
from zimp.domain.map.tile_factory import TileFactory


class InsideTileFactory(TileFactory):
    """Concrete factory that creates inside tiles."""

    def create_tile(self, tile_id: int) -> Tile:
        match tile_id:
            case 1:
                return InsideTile(1, (Direction.NORTH,))
            case 2:
                return InsideTile(2, (Direction.NORTH, Direction.WEST))
            case 3:
                return InsideTile(3, (Direction.NORTH, Direction.EAST,
                                      Direction.SOUTH, Direction.WEST),
                                  is_exit_tile=True)
            case 4:
                return InsideTile(4, (Direction.NORTH, Direction.EAST,
                                      Direction.WEST))
            case 5:
                return InsideTile(5, (Direction.NORTH,))
            case 6:
                return InsideTile(6, (Direction.NORTH, Direction.EAST,
                                      Direction.WEST), TileEffect.HEALTH)
            case 7:
                return InsideTile(7, (Direction.NORTH,), TileEffect.SEARCH)
            case 8:
                return InsideTile(8, (Direction.EAST, Direction.WEST),
                                  TileEffect.FIND_TOTEM)
            case _:
                raise ValueError(f"Unknown inside tile ID: {tile_id}")
