from mlflow.entities._mlflow_object import _MlflowObject


class FeedbackSource(_MlflowObject):
    """
    Source of the feedback (human, LLM as a judge with GPT-4, etc).
    """

    def __init__(self, source_type, source_id, metadata=None):
        """Construct a new mlflow.entities.FeedbackSource instance.

        Args:
            source_type: The type of the feedback source (FeedbackSourceType).
            source_id: An identifier for the source, e.g. Databricks user ID or LLM judge ID.
            metadata: Additional metadata about the source, e.g. human-readable name, inlined LLM
            judge parameters, etc.
        """
        self.source_type = source_type
        self.source_id = source_id
        self.metadata = metadata or {}

    def to_dictionary(self):
        return {
            "source_type": self.source_type,
            "source_id": self.source_id,
            "metadata": self.metadata,
        }


class FeedbackSourceType:
    AI_JUDGE = "AI_JUDGE"
    HUMAN = "HUMAN"