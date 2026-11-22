import random

from zimp.domain.common.error_code import ErrorCode
from zimp.domain.common.result import Result
from zimp.domain.map.inside_tile_factory import InsideTileFactory
from zimp.domain.map.outside_tile_factory import OutsideTileFactory
from zimp.domain.map.tile import Tile
from zimp.domain.map.validators import is_valid_seed


class TileManager:
    """TileManager class used to create and randomise map tiles."""

    # class constants
    __MIN_TILE_ID = 1
    __MAX_TILE_ID = 9
    __NUM_OF_TILES = 8
    __INSIDE_START_TILE_INDEX = 1
    __OUTSIDE_START_TILE_INDEX = 3

    def __init__(self):
        self.__inside_tile_order_index: int = 0
        self.__outside_tile_order_index: int = 0
        self.__inside_tile_order: list[int] = []
        self.__outside_tile_order: list[int] = []
        self.__INSIDE_TILE_DETAILS: dict[int, Tile] = {}
        self.__OUTSIDE_TILE_DETAILS: dict[int, Tile] = {}
        self.__tile_randomizer: random.Random = random.Random()  # class specific randomiser
        self.__randomizer_seed: int | None = None

        # setup factories
        self.__inside_tile_factory = InsideTileFactory()
        self.__outside_tile_factory = OutsideTileFactory()

        # setup tiles
        self.__create_tiles()
        self.reset_tile_order()

    def __create_tiles(self) -> None:
        """Creates inside and outside tiles."""
        tile_ids = list(range(self.__MIN_TILE_ID, self.__MAX_TILE_ID))
        self.__INSIDE_TILE_DETAILS = self.__inside_tile_factory.get_all_tiles(
            tile_ids)
        self.__OUTSIDE_TILE_DETAILS = self.__outside_tile_factory.get_all_tiles(
            tile_ids)

    def __shuffle_tile_order(self) -> None:
        """Shuffles order of inside and outside tiles."""
        self.__tile_randomizer.seed(self.__randomizer_seed)
        inside_random_order = self.__tile_randomizer.sample(
            range(self.__MIN_TILE_ID, self.__MAX_TILE_ID),
            k=self.__NUM_OF_TILES)
        outside_random_order = self.__tile_randomizer.sample(
            range(self.__MIN_TILE_ID, self.__MAX_TILE_ID),
            k=self.__NUM_OF_TILES)

        # add inside/outside starting tiles to the start of each list
        inside_random_order.remove(self.__INSIDE_START_TILE_INDEX)
        outside_random_order.remove(self.__OUTSIDE_START_TILE_INDEX)
        inside_random_order.insert(0, self.__INSIDE_START_TILE_INDEX)
        outside_random_order.insert(0, self.__OUTSIDE_START_TILE_INDEX)

        self.__inside_tile_order = inside_random_order
        self.__outside_tile_order = outside_random_order

    def reset_tile_order(self,
                         randomizer_seed: int | None = None) -> ErrorCode | None:
        """Resets the order of the inside and outside tiles.
        Args:
            randomizer_seed (int | None): New randomiser seed value. Defaults to None (random seed).
        Returns:
            ErrorCode: If seed was invalid. | None: If nothing went wrong.
        """
        if not is_valid_seed(randomizer_seed):
            return ErrorCode.INVALID_TYPE_RANDOMIZER_SEED

        self.__randomizer_seed = randomizer_seed
        self.__inside_tile_order_index = 0
        self.__outside_tile_order_index = 0
        self.__shuffle_tile_order()
        return None  # success

    def is_inside_tiles_depleted(self) -> bool:
        """Checks if player has explored all inside tiles.
        Returns:
            bool: True if player has explored all inside tiles, False otherwise.
        """
        return self.__inside_tile_order_index >= len(self.__inside_tile_order)

    def is_outside_tiles_depleted(self) -> bool:
        """Checks if player has explored all outside tiles.
        Returns:
            bool: True if player has explored all outside tiles, False otherwise.
        """
        return self.__outside_tile_order_index >= len(
            self.__outside_tile_order)

    def get_next_inside_tile(self) -> Result:
        """Gets the next inside tile following the randomised order.
        Returns:
            Result: Success - next inside tile. | Fail - ErrorCode.
        """
        if self.is_inside_tiles_depleted():
            return Result.fail(ErrorCode.DEPLETED_INSIDE_TILES)

        # gets next tile
        index = self.__inside_tile_order[self.__inside_tile_order_index]
        new_tile = self.__INSIDE_TILE_DETAILS.get(index)
        if new_tile is None:
            return Result.fail(ErrorCode.FATAL_ERROR)

        # increments index and returns tile
        self.__inside_tile_order_index += 1
        return Result.success(new_tile)

    def get_next_outside_tile(self) -> Result:
        """Gets the next outside tile following the randomised order.
        Returns:
            Result: Success - next outside tile. | Fail - ErrorCode.
        """
        if self.is_outside_tiles_depleted():
            return Result.fail(ErrorCode.DEPLETED_OUTSIDE_TILES)

        # gets next tile
        index = self.__outside_tile_order[self.__outside_tile_order_index]
        new_tile = self.__OUTSIDE_TILE_DETAILS.get(index)
        if new_tile is None:
            return Result.fail(ErrorCode.FATAL_ERROR)

        # increments index and returns tile
        self.__outside_tile_order_index += 1
        return Result.success(new_tile)
