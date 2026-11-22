from zimp.domain.common.error_code import ErrorCode
from zimp.domain.map.tile_manager import TileManager


class TestTileManager:
    # ========================== Good Day ========================== #

    def test_set_randomizer_seed_when_given_valid_value_returns_none(self) -> None:
        # Arrange
        tile_manager = TileManager()
        valid_seed = 42

        # Act
        result = tile_manager.reset_tile_order(valid_seed)

        # Assert
        assert result is None

    def test_set_randomizer_seed_when_given_valid_value_keeps_tile_order_consistent(self) -> None:
        # Arrange
        tile_manager = TileManager()
        seed = 42
        tile_manager.reset_tile_order(seed)
        expected_inside_ids = [1, 2, 6, 3, 8, 7, 5, 4]
        expected_outside_ids = [11, 10, 13, 12, 9, 15, 14, 16]

        # Act
        actual_inside_ids: list[int] = []
        for _ in expected_inside_ids:
            result = tile_manager.get_next_inside_tile()
            actual_inside_ids.append(result.get_data().get_data((0, 0)).id)

        actual_outside_ids: list[int] = []
        for _ in expected_outside_ids:
            result = tile_manager.get_next_outside_tile()
            actual_outside_ids.append(result.get_data().get_data((0, 0)).id)

        # Assert
        assert actual_inside_ids == expected_inside_ids
        assert actual_outside_ids == expected_outside_ids

    def test_is_inside_tiles_depleted_when_tiles_left_returns_false(self) -> None:
        # Arrange
        tile_manager = TileManager()

        # Act
        result = tile_manager.is_inside_tiles_depleted()

        # Assert
        assert result is False

    def test_is_inside_tiles_depleted_when_no_tiles_left_returns_true(self) -> None:
        # Arrange
        tile_manager = TileManager()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()

        # Act
        result = tile_manager.is_inside_tiles_depleted()

        # Assert
        assert result is True

    def test_is_outside_tiles_depleted_when_tiles_left_returns_false(self) -> None:
        # Arrange
        tile_manager = TileManager()

        # Act
        result = tile_manager.is_outside_tiles_depleted()

        # Assert
        assert result is False

    def test_is_outside_tiles_depleted_when_no_tiles_left_returns_true(self) -> None:
        # Arrange
        tile_manager = TileManager()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()

        # Act
        result = tile_manager.is_outside_tiles_depleted()

        # Assert
        assert result is True

    def test_get_next_inside_tile_when_no_tiles_left_returns_depleted_inside_error(self) -> None:
        # Arrange
        tile_manager = TileManager()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        tile_manager.get_next_inside_tile()
        depleted_error = ErrorCode.DEPLETED_INSIDE_TILES

        # Act
        result = tile_manager.get_next_inside_tile()

        # Assert
        assert result.is_fail() is True
        assert result.get_error_code() == depleted_error

    def test_get_next_outside_tile_when_no_tiles_left_returns_depleted_outside_error(self) -> None:
        # Arrange
        tile_manager = TileManager()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        tile_manager.get_next_outside_tile()
        depleted_error = ErrorCode.DEPLETED_OUTSIDE_TILES

        # Act
        result = tile_manager.get_next_outside_tile()

        # Assert
        assert result.is_fail() is True
        assert result.get_error_code() == depleted_error

    # ========================== Bad Day ========================== #

    def test_set_randomizer_seed_when_given_invalid_value_returns_randomizer_seed_error(self) -> None:
        # Arrange
        tile_manager = TileManager()
        invalid_seed = "42"
        randomizer_seed_error = ErrorCode.INVALID_TYPE_RANDOMIZER_SEED

        # Act
        result = tile_manager.reset_tile_order(invalid_seed)

        # Assert
        assert result == randomizer_seed_error
