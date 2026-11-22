import pytest

from zimp.domain.map.outside_tile import OutsideTile
from zimp.domain.map.outside_tile_factory import OutsideTileFactory


class TestOutsideTileFactory:
    @pytest.mark.parametrize("tile_id", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_create_tile_when_given_valid_id_returns_inside_tile(self,
                                                                 tile_id) -> None:
        # Arrange
        factory = OutsideTileFactory()

        # Act
        tile = factory.create_tile(tile_id)

        # Assert
        assert isinstance(tile, OutsideTile)

    def test_create_tile_when_given_invalid_id_raises_value_error_with_correct_message(
            self) -> None:
        # Arrange
        factory = OutsideTileFactory()

        # Act & Assert
        with pytest.raises(ValueError, match="Unknown outside tile ID: 9999"):
            factory.create_tile(9999)

    def test_get_all_tiles_returns_correct_number_of_tiles(self) -> None:
        # Arrange
        expected_number_of_tiles = 8
        factory = OutsideTileFactory()

        # Act
        tiles = factory.get_all_tiles(list(range(1, 9)))

        # Assert
        assert len(tiles) == expected_number_of_tiles
