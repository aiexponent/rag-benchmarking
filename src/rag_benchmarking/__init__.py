"""RAG Benchmarking — Framework-agnostic evaluation harness for RAG and agentic AI systems."""

from importlib.metadata import PackageNotFoundError, version

from rag_benchmarking.app.sdk.client import RagEval
from rag_benchmarking.harness.protocol import RAGEvaluable, validate_evaluable
from rag_benchmarking.harness.result_store import ResultStore
from rag_benchmarking.harness.runner import EvaluationRunner
from rag_benchmarking.harness.schemas import (
    METRIC_GROUPS,
    AgentTrace,
    BenchmarkReport,
    EvalResult,
    EvalSample,
    MetricGroup,
    ReasoningStep,
    RetrievedChunk,
    RunConfig,
    ToolCall,
    ToolCallType,
)

try:
    __version__ = version("rag-benchmarking")
except PackageNotFoundError:
    __version__ = "1.0.2"

__all__ = [
    "__version__",
    "RagEval",
    "EvaluationRunner",
    "ResultStore",
    "RAGEvaluable",
    "validate_evaluable",
    "AgentTrace",
    "BenchmarkReport",
    "EvalResult",
    "EvalSample",
    "MetricGroup",
    "METRIC_GROUPS",
    "ReasoningStep",
    "RetrievedChunk",
    "RunConfig",
    "ToolCall",
    "ToolCallType",
]
