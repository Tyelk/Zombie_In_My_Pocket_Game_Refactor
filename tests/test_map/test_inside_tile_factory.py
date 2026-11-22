import pytest

from zimp.domain.map.inside_tile import InsideTile
from zimp.domain.map.inside_tile_factory import InsideTileFactory


class TestInsideTileFactory:
    @pytest.mark.parametrize("tile_id", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_create_tile_when_given_valid_id_returns_inside_tile(self,
                                                                 tile_id) -> None:
        # Arrange
        factory = InsideTileFactory()

        # Act
        tile = factory.create_tile(tile_id)

        # Assert
        assert isinstance(tile, InsideTile)

    def test_create_tile_when_given_invalid_id_raises_value_error_with_correct_message(
            self) -> None:
        # Arrange
        factory = InsideTileFactory()

        # Act & Assert
        with pytest.raises(ValueError, match="Unknown inside tile ID: 999"):
            factory.create_tile(999)

    def test_get_all_tiles_returns_correct_number_of_tiles(self) -> None:
        # Arrange
        expected_number_of_tiles = 8
        factory = InsideTileFactory()

        # Act
        tiles = factory.get_all_tiles(list(range(1, 9)))

        # Assert
        assert len(tiles) == expected_number_of_tiles
