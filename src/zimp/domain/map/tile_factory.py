from abc import ABC, abstractmethod

from zimp.domain.map.tile import Tile


class TileFactory(ABC):
    """Abstract Tile factory that defines the interface for creating tiles."""

    @abstractmethod
    def create_tile(self, tile_id: int) -> Tile:
        """Factory method used by subclasses to decide how to create a tile."""
        raise NotImplementedError(
            "subclasses of TileFactory must implement the create_tile method")

    def get_all_tiles(self, tile_ids: list[int]) -> dict[int, Tile]:
        """Uses the factory method to build all the tiles."""
        return {tile_id: self.create_tile(tile_id) for tile_id in tile_ids}
