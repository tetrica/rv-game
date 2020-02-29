class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        self.explored = False

        # By default, if a tile is blocked, it also blocks sight
        self.block_sight = blocked if block_sight is None else block_sight