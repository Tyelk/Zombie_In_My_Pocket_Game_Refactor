import pytest

from zimp.domain.common.direction import Direction
from zimp.domain.map.outside_tile import OutsideTile


class TestOutsideTile:
    def test_is_outside_returns_true(self) -> None:
        # Arrange
        tile = OutsideTile(9, (Direction.NORTH,))

        # Act
        outside_result = tile.is_outside()

        # Assert
        assert outside_result is True

    @pytest.mark.parametrize("is_entry", [True, False])
    def test_is_entry_when_entry_tile_returns_true(self, is_entry) -> None:
        # Arrange
        tile = OutsideTile(9, (Direction.NORTH,), is_entry_tile=is_entry)

        # Act
        exit_result = tile.is_entry()

        # Assert
        assert exit_result is is_entry
