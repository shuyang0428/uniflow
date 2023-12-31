"""Model Flow Module."""
from typing import Any, Dict, Sequence

from uniflow.constants import TRANSFORM
from uniflow.flow.flow import Flow
from uniflow.node import Node
from uniflow.op.model.llm_processor import JsonFormattedDataProcessor, LLMDataProcessor
from uniflow.op.model.model_op import ModelOp
from uniflow.op.prompt_schema import GuidedPrompt


class AzureOpenAIModelFlow(Flow):
    """AzureOpenAI Model Flow Class."""

    def __init__(
        self,
        guided_prompt_template: GuidedPrompt,
        model_config: Dict[str, Any],
    ) -> None:
        """AzureOpenAI Model Flow Constructor.

        Args:
            guided_prompt_template (GuidedPrompt): Guided prompt template.
            model_config (Dict[str, Any]): Model config.
        """
        super().__init__()
        if model_config["response_format"]["type"] == "json_object":
            model = JsonFormattedDataProcessor(
                guided_prompt_template=guided_prompt_template,
                model_config=model_config,
            )
        else:
            model = LLMDataProcessor(
                guided_prompt_template=guided_prompt_template,
                model_config=model_config,
            )
        self._model_op = ModelOp(
            name="azure_openai_model_op",
            model=model,
        )

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run Model Flow.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        return self._model_op(nodes)


class TransformAzureOpenAIFlow(AzureOpenAIModelFlow):
    """Transform AzureOpenAI Flow Class."""

    TAG = TRANSFORM
