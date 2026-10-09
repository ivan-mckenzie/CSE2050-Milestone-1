from typing import Any, Optional


class Node:
    """node class"""
    def __init__(self, item: Any, link: "Node | None" = None) -> None:
        """inits a node"""
        self.item = item
        self.link = link    

