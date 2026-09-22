from __future__ import annotations

import sys


def test_top_level_package_exports() -> None:
    """Verify primary public exports from top-level rag_benchmarking package."""
    from rag_benchmarking import (
        METRIC_GROUPS,
        AgentTrace,
        BenchmarkReport,
        EvalResult,
        EvalSample,
        EvaluationRunner,
        MetricGroup,
        RagEval,
        RAGEvaluable,
        ReasoningStep,
        ResultStore,
        RetrievedChunk,
        RunConfig,
        ToolCall,
        ToolCallType,
        __version__,
        validate_evaluable,
    )

    assert __version__ is not None
    assert RagEval is not None
    assert EvaluationRunner is not None
    assert ResultStore is not None
    assert RAGEvaluable is not None
    assert callable(validate_evaluable)
    assert BenchmarkReport is not None
    assert EvalSample is not None
    assert AgentTrace is not None
    assert RunConfig is not None
    assert METRIC_GROUPS is not None
    assert EvalResult is not None
    assert MetricGroup is not None
    assert ReasoningStep is not None
    assert RetrievedChunk is not None
    assert ToolCall is not None
    assert ToolCallType is not None


def test_sdk_entrypoint_export() -> None:
    """Verify public RagEval export from rag_benchmarking.sdk."""
    from rag_benchmarking import RagEval as RootRagEval
    from rag_benchmarking.app.sdk.client import RagEval as ImplRagEval
    from rag_benchmarking.sdk import RagEval as SdkRagEval

    assert RootRagEval is ImplRagEval
    assert SdkRagEval is ImplRagEval


def test_no_top_level_pollution() -> None:
    """Verify app and harness are not importable as top-level packages outside source tree."""
    # When importing rag_benchmarking, it should not inject 'app' or 'harness' into sys.modules
    import rag_benchmarking  # noqa: F401

    assert "app" not in sys.modules
    assert "harness" not in sys.modules
