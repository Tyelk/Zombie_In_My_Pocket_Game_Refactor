from zimp.domain.common.direction import Direction
from zimp.domain.common.tile_effect import TileEffect
from zimp.domain.map.outside_tile import OutsideTile
from zimp.domain.map.tile import Tile
from zimp.domain.map.tile_factory import TileFactory


class OutsideTileFactory(TileFactory):
    """Concrete factory that creates outside tiles."""

    def create_tile(self, tile_id: int) -> Tile:
        match tile_id:
            case 1:
                return OutsideTile(9, (Direction.EAST, Direction.SOUTH,
                                       Direction.WEST))
            case 2:
                return OutsideTile(10, (Direction.EAST, Direction.SOUTH,
                                        Direction.WEST))
            case 3:
                return OutsideTile(11, (Direction.NORTH, Direction.EAST,
                                        Direction.SOUTH), is_entry_tile=True)
            case 4:
                return OutsideTile(12, (Direction.SOUTH, Direction.WEST))
            case 5:
                return OutsideTile(13, (Direction.EAST, Direction.SOUTH,
                                        Direction.WEST), TileEffect.HEALTH)
            case 6:
                return OutsideTile(14, (Direction.EAST, Direction.SOUTH,
                                        Direction.WEST))
            case 7:
                return OutsideTile(15, (Direction.EAST, Direction.SOUTH,
                                        Direction.WEST))
            case 8:
                return OutsideTile(16, (Direction.EAST, Direction.SOUTH),
                                   TileEffect.BURY_TOTEM)
            case _:
                raise ValueError(f"Unknown outside tile ID: {tile_id}")
