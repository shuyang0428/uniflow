from typing import Dict, Callable, Tuple

from uniflow.node import Node
from uniflow.op.op import Op

class ExpandOp(Op):
    def __init__(self, name: str, split_func: Callable[[Dict], Tuple[Dict, Dict]] = None):
        """Constructor of ExpandOp class for uniflow.

        Args:
            name (str): Name of the op.
            split_func (Callable[[Dict], Tuple[Dict, Dict]]): Function to split the value_dict into two.
        """
        super().__init__(name)
        self.split_func = split_func or self._default_split

    def _default_split(self, value_dict: Dict) -> Tuple[Dict, Dict]:
        """Default split function if no custom function is provided.

        Args:
            value_dict (Dict): The dictionary to split.

        Returns:
            Tuple[Dict, Dict]: Two dictionaries, split from the original.
        """
        n = len(value_dict)
        keys = list(value_dict.keys())
        return (
            {k: value_dict[k] for k in keys[: n // 2]},
            {k: value_dict[k] for k in keys[n // 2 :]},
        )

    def __call__(self, root: Node) -> Tuple[Node, Node]:
        """Call op to split the root node into two nodes.

        Args:
            root (Node): The root node to split.

        Returns:
            Tuple[Node, Node]: Two new nodes, split from the root node.
        """
        value_dict_1, value_dict_2 = self.split_func(root.value_dict)

        # Provide a name when creating new Node instances
        expand_1 = Node(name="expand_1", value_dict=value_dict_1)
        expand_2 = Node(name="expand_2", value_dict=value_dict_2)

        return expand_1, expand_2
