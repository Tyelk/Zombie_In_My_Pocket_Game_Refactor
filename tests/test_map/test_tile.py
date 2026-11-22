import pytest

from zimp.domain.common.direction import Direction
from zimp.domain.common.tile_effect import TileEffect
from zimp.domain.map.tile import Tile


class TestTile:
    # ========================== Good Day ========================== #
    @pytest.mark.parametrize("rotation_dir", [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST])
    def test_rotate_rotates_to_given_direction(self, rotation_dir) -> None:
        # Arrange
        test_tile = Tile(1, (Direction.NORTH,))

        # Act
        test_tile.rotate(rotation_dir)

        # Assert
        assert test_tile.get_rotation() == rotation_dir

    @pytest.mark.parametrize("rotation_dir, door_direction, rotated_door_direction",
                             [(Direction.NORTH, Direction.WEST, Direction.WEST),
                              (Direction.WEST, Direction.SOUTH, Direction.EAST),
                              (Direction.SOUTH, Direction.EAST, Direction.WEST),
                              (Direction.EAST, Direction.SOUTH, Direction.WEST), ])
    def test_get_door_direction_when_rotated_returns_rotated_direction(self, rotation_dir, door_direction,
                                                                       rotated_door_direction) -> None:
        # Arrange
        test_tile = Tile(1, (door_direction,))
        test_tile.rotate(rotation_dir)

        # Act
        door_directions = test_tile.get_door_directions()

        # Assert
        assert door_directions[0] == rotated_door_direction

    @pytest.mark.parametrize(
        "rotation_dir, first_valid_door, second_valid_door, first_invalid_door, second_invalid_door",
        [(Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.NORTH, Direction.EAST),
         (Direction.WEST, Direction.SOUTH, Direction.EAST, Direction.NORTH, Direction.WEST),
         (Direction.SOUTH, Direction.EAST, Direction.NORTH, Direction.WEST, Direction.SOUTH),
         (Direction.EAST, Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST), ])
    def test_has_door_in_direction_when_rotated_returns_true_on_matching_directions(self, rotation_dir,
                                                                                    first_valid_door,
                                                                                    second_valid_door,
                                                                                    first_invalid_door,
                                                                                    second_invalid_door) -> None:
        # Arrange & Act
        door_directions = (Direction.WEST, Direction.SOUTH)
        test_tile = Tile(1, door_directions)
        test_tile.rotate(rotation_dir)

        # Assert
        assert test_tile.has_door_in_direction(first_valid_door) is True
        assert test_tile.has_door_in_direction(second_valid_door) is True
        assert test_tile.has_door_in_direction(first_invalid_door) is False
        assert test_tile.has_door_in_direction(second_invalid_door) is False

    @pytest.mark.parametrize(
        "rotation_dir, first_valid_door, second_valid_door, first_invalid_door, second_invalid_door",
        [(Direction.NORTH, Direction.EAST, Direction.NORTH, Direction.WEST, Direction.SOUTH),
         (Direction.WEST, Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST),
         (Direction.SOUTH, Direction.WEST, Direction.SOUTH, Direction.NORTH, Direction.EAST),
         (Direction.EAST, Direction.SOUTH, Direction.EAST, Direction.NORTH, Direction.WEST), ])
    def test_has_door_in_opposite_direction_when_rotated_returns_true_on_opposite_directions(self, rotation_dir,
                                                                                             first_valid_door,
                                                                                             second_valid_door,
                                                                                             first_invalid_door,
                                                                                             second_invalid_door) -> None:
        # Arrange & Act
        door_directions = (Direction.WEST, Direction.SOUTH)
        test_tile = Tile(1, door_directions)
        test_tile.rotate(rotation_dir)

        # Assert
        assert test_tile.has_door_in_opposite_direction(first_valid_door) is True
        assert test_tile.has_door_in_opposite_direction(second_valid_door) is True
        assert test_tile.has_door_in_opposite_direction(first_invalid_door) is False
        assert test_tile.has_door_in_opposite_direction(second_invalid_door) is False

    @pytest.mark.parametrize("rotation_dir, zombie_door_direction",
                             [(Direction.NORTH, Direction.EAST), (Direction.WEST, Direction.NORTH),
                              (Direction.SOUTH, Direction.WEST), (Direction.EAST, Direction.SOUTH), ])
    def test_add_zombie_door_when_given_direction_adds_door_in_correct_direction(self, rotation_dir,
                                                                                 zombie_door_direction) -> None:
        # Arrange
        test_tile = Tile(1, (Direction.NORTH,))
        test_tile.rotate(rotation_dir)

        # Act
        test_tile.add_zombie_door(zombie_door_direction)

        # Assert
        assert test_tile.has_door_in_direction(zombie_door_direction) is True

    def test_reset_clears_data_back_to_default_values_and_does_not_change_immutable_data(self) -> None:
        # Arrange
        doors = (Direction.EAST, Direction.WEST)
        effect = TileEffect.BURY_TOTEM
        is_outside = True
        is_exit = False
        is_entry = False
        default_zombie_door_value = None
        default_locked_value = False
        default_rotation_value = Direction.NORTH
        test_tile = Tile(1, doors, effect, is_outside, is_exit, is_entry)
        test_tile.add_zombie_door(Direction.NORTH)
        test_tile.rotate(Direction.SOUTH)
        test_tile.lock()

        # Act
        test_tile.reset()
        first_door_result = test_tile.has_door_in_direction(doors[0])
        second_door_result = test_tile.has_door_in_direction(doors[1])
        effect_result = test_tile.get_tile_effect()
        is_outside_result = test_tile.is_outside()
        is_exit_result = test_tile.is_exit()
        is_entry_result = test_tile.is_entry()
        rotation_result = test_tile.get_rotation()
        zombie_door_result = test_tile.get_data((1, 1)).zombie_door
        locked_result = test_tile.is_locked()

        # Assert
        assert first_door_result is True
        assert second_door_result is True
        assert effect_result == effect
        assert is_outside_result is True
        assert is_exit_result is False
        assert is_entry_result is False
        assert rotation_result == default_rotation_value
        assert zombie_door_result == default_zombie_door_value
        assert locked_result == default_locked_value
