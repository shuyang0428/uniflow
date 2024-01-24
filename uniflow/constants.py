"""Flow constants."""
from uniflow.flow.expand_reduce_flow import ExpandReduceFlow

ROOT_NAME = "root"
OUTPUT_NAME = "output"

# Flow Types
EXTRACT = "extract"
TRANSFORM = "transform"
RATER = "rater"

EXPAND_REDUCE = "expand_reduce"

flow_dict = {EXPAND_REDUCE: ExpandReduceFlow}
