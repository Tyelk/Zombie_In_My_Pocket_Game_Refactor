import pytest

from zimp.domain.common.direction import Direction
from zimp.domain.map.inside_tile import InsideTile


class TestInsideTile:
    def test_is_outside_returns_false(self) -> None:
        # Arrange
        tile = InsideTile(1, (Direction.NORTH,))

        # Act
        outside_result = tile.is_outside()

        # Assert
        assert outside_result is False

    @pytest.mark.parametrize("is_exit", [True, False])
    def test_is_exit_when_exit_tile_returns_true(self, is_exit) -> None:
        # Arrange
        tile = InsideTile(3, (Direction.NORTH,), is_exit_tile=is_exit)

        # Act
        exit_result = tile.is_exit()

        # Assert
        assert exit_result is is_exit
