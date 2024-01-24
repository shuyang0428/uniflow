from uniflow.node import Node
from typing import Dict, Callable
from uniflow.op.op import Op

class ReduceOp(Op):
    def __init__(self, name: str, merge_func: Callable[[Dict, Dict], Dict] = None):
        """Constructor of ReduceOp class for uniflow.

        Args:
            name (str): Name of the op.
            merge_func (Callable[[Dict, Dict], Dict]): Function to merge the value_dicts.
        """
        super().__init__(name)
        self.merge_func = merge_func or self._default_merge

    def _default_merge(self, value_dict_1: Dict, value_dict_2: Dict) -> Dict:
        """Default merge function if no custom function is provided.

        Args:
            value_dict_1 (Dict): The first dictionary to merge.
            value_dict_2 (Dict): The second dictionary to merge.

        Returns:
            Dict: Merged dictionary.
        """
        # Merging strategy: Concatenate keys and values
        merged = {}
        for k1, v1 in value_dict_1.items():
            for k2, v2 in value_dict_2.items():
                merged[f"{k1} {k2}"] = f"{v1} {v2}"
        return merged

    def __call__(self, expand_1: Node, expand_2: Node) -> Node:
        """Call op to merge two nodes into one node.

        Args:
            expand_1 (Node): The first node to merge.
            expand_2 (Node): The second node to merge.

        Returns:
            Node: A new node with merged value_dict.
        """
        merged_value_dict = self.merge_func(expand_1.value_dict, expand_2.value_dict)
        reduce_1 = Node(value_dict=merged_value_dict)
        return reduce_1
