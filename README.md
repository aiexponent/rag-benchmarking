<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/aiexponent/rag-benchmarking/main/.github/brand/og-rag-benchmarking-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/aiexponent/rag-benchmarking/main/.github/brand/og-rag-benchmarking-light.png">
    <img src="https://raw.githubusercontent.com/aiexponent/rag-benchmarking/main/.github/brand/og-rag-benchmarking-dark.png" alt="RAG Benchmarking — EU AI Act Article 15 Accuracy Evaluation Harness" width="100%"/>
  </picture>
  <h1 align="center">RAG Benchmarking</h1>
  <p align="center"><em>Framework-agnostic evaluation harness for RAG and agentic AI systems.</em></p>
  <p align="center">
    <a href="https://pypi.org/project/rag-benchmarking/"><img src="https://img.shields.io/pypi/v/rag-benchmarking.svg?style=flat-square&color=0D5463" alt="PyPI version"></a>
    <a href="https://github.com/aiexponent/rag-benchmarking/actions"><img src="https://img.shields.io/github/actions/workflow/status/aiexponent/rag-benchmarking/ci.yml?branch=main&style=flat-square&label=CI" alt="CI"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-0D5463.svg?style=flat-square" alt="License: Apache 2.0"></a>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.11%2B-0D5463.svg?style=flat-square" alt="Python 3.11+"></a>
    <a href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689"><img src="https://img.shields.io/badge/EU%20AI%20Act-Article%2015-0D5463.svg?style=flat-square" alt="EU AI Act Article 15"></a>
    <a href="#privacy"><img src="https://img.shields.io/badge/telemetry-zero-0B7A4B.svg?style=flat-square" alt="Zero telemetry"></a>
    <a href="#evidence-status"><img src="https://img.shields.io/badge/evidence_status-VALIDATED-B68A2E.svg?style=flat-square" alt="Evidence status: VALIDATED"></a>
  </p>
</div>

---

> **RAG Benchmarking provides empirical, deterministic accuracy and faithfulness evidence for EU AI Act Article 15 (Accuracy, Robustness, Cybersecurity) and Annex IV technical documentation. Apache 2.0, AS IS.**
>
> RAG Benchmarking turns model evaluation, retrieval quality, and agentic trace verification into an automated developer workflow and CI gate. Measures classic retrieval and generation quality alongside agentic tool-use fidelity, outputting structured JSON benchmark reports and SQLite run histories. RAG Benchmarking is an engineering evaluation harness; it is **not** a notified body and does not constitute formal legal certification.

---

## The Problem

Under the EU AI Act ([Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)), providers and deployers of **high-risk AI systems** (governed by Article 6 and Annex III) face mandatory statutory obligations under **Article 15 (Accuracy, Robustness, and Cybersecurity)**:

* **Statutory Requirement**: High-risk AI systems must achieve appropriate levels of accuracy, robustness, and cybersecurity, and perform consistently throughout their lifecycle. Declared metrics and levels of accuracy must be documented in technical documentation (Annex IV §2(b)) and instructions for use (Article 13).
* **Provisional Enforcement Deadline**: Stand-alone high-risk systems under Annex III must comply by **2 December 2027** (under the Digital Omnibus simplification package).
* **Statutory Non-Compliance Penalties**: Fines up to **€15,000,000 or 3% of total worldwide annual turnover** under Article 99(4).
* **The Hallucination & Evidence Deficit**: Teams deploying RAG or autonomous agentic workflows struggle to prove that retrieved context is grounded, citations are truthful, and tools are called accurately across system updates and model migrations.

**RAG Benchmarking** provides the empirical evaluation infrastructure directly in your terminal and CI/CD pipeline:

> *"How do we measure, benchmark, and mathematically verify accuracy and faithfulness across model migrations and retrieval changes?"*

Bring your own RAG or agent pipeline. Evaluate against 12+ classic and agentic-era metrics across curated golden datasets. Output audit-ready benchmark reports with zero telemetry.

Built by [AI Exponent LLC](https://aiexponent.com). Apache 2.0. Runs entirely offline or via local API service after `pip install`.

---

## Quick Start

```bash
pip install rag-benchmarking
```

### 1. Python SDK Evaluation

```python
from rag_benchmarking import RagEval

# Initialize evaluation client
client = RagEval(api_url="http://localhost:5001", api_key="your-key")

# Works with LangChain
# result = my_chain.invoke({"query": "What is Article 15?"})
# sample = RagEval.from_langchain(result)

# Or any standard dictionary with question / contexts / answer
sample = {
    "question": "What documentation must high-risk AI system deployers maintain under Article 26?",
    "contexts": [
        "Article 26(5) requires deployers of high-risk AI systems to keep system logs for at least six months."
    ],
    "answer": "Deployers must keep logs generated by high-risk AI systems for at least six months where appropriate.",
}

# Run benchmark evaluation
report = client.evaluate([sample], metrics=["faithfulness", "answer_relevancy"])
print(report["metrics"])
# Output: {"faithfulness": 0.962, "answer_relevancy": 0.845}
```

### 2. Evaluate Agentic Traces

```python
from rag_benchmarking import RagEval

client = RagEval(api_url="http://localhost:5001", api_key="your-key")

trace = {
    "question": "What is the GPAI compliance deadline under Article 111?",
    "final_answer": "Obligations for general-purpose AI models apply from 2 August 2025.",
    "tool_calls": [
        {
            "tool_name": "eu_act_search",
            "tool_input": {"query": "GPAI deadline Article 111"},
            "tool_output": "Chapter V obligations apply from 2 August 2025.",
            "step_index": 0,
        }
    ],
}

report = client.evaluate_agent(trace, metrics=["source_attribution_accuracy", "tool_call_accuracy"])
print(report["metrics"])
```

### 3. CLI Evaluation

```bash
# Run evaluation across the 50-sample golden QA dataset
python scripts/evaluate.py --dataset data/golden/qa.jsonl --metric-group classic --output report.json
```

### 4. Running the Evaluation Server

```bash
# Clone the repository
git clone https://github.com/aiexponent/rag-benchmarking.git
cd rag-benchmarking

# Start the evaluation server & vector store
docker compose up -d

# OpenAPI docs available at: http://localhost:5001/docs
```

---

## Why RAG Benchmarking

| Evaluation Method | Cost | Turnaround | Deterministic / Repeatable? | Offline / Zero-Telemetry? |
| :--- | :--- | :--- | :--- | :--- |
| **Big 4 Consulting** | €50K–€150K per audit¹ | 4–8 Weeks | ❌ No (Advisory opinion) | ❌ No (NDAs & data sharing) |
| **Enterprise Cloud Eval SaaS** | $20K–$60K/year¹ | Days | ⚠️ Partial | ❌ No (Transfers prompts to cloud) |
| **Internal Spreadsheets** | "Free" | Days | ❌ No (Human error) | ⚠️ Manual |
| **RAG Benchmarking** | **Free (Apache 2.0)** | **< 60 seconds** | **✅ Yes (Deterministic hash & golden sets)** | **✅ Yes (100% offline, zero network)** |

<sup>¹ Indicative market figures gathered from public AI evaluation engagement quotes and enterprise LLMOps pricing pages. Not a formal benchmark; figures vary by evaluation volume, model family, and vendor.</sup>

---

## System Architecture

RAG Benchmarking operates as a deterministic, decoupled evaluation pipeline:

```mermaid
graph TB
    subgraph Inputs ["1. Input Specifications"]
        INP1["Polyglot RAG Pipelines<br/><code>LangChain · LlamaIndex · Custom RAG</code>"]
        INP2["Agentic Execution Traces<br/><code>Tool calls · Reasoning steps · Citations</code>"]
        INP3["Curated Golden Datasets<br/><code>data/golden/qa.jsonl (50 enterprise QA samples)</code>"]
    end

    subgraph Core ["2. Evaluation & Metric Engines"]
        RUN["EvaluationRunner<br/><code>rag_benchmarking.harness.runner</code>"]
        CLASSIC["Classic Generation Engine<br/><code>faithfulness · answer_relevancy · context_precision</code>"]
        RETRIEVAL["Deterministic Retrieval Engine<br/><code>Precision@K · Recall@K · MRR · NDCG</code>"]
        AGENTIC["Agentic Trace Scorer<br/><code>tool_call_accuracy · source_attribution · necessity</code>"]
    end

    subgraph Integrity ["3. Persistence & Integrity"]
        STORE["ResultStore (SQLite)<br/><code>runs · samples · metric_distributions</code>"]
        COMP["Run Comparator<br/><code>Model regression & drift analysis</code>"]
        HASH["RFC 8785 Canonical Digest<br/><code>SHA-256 audit trail signature</code>"]
    end

    subgraph Outputs ["4. Audit-Ready Artifacts"]
        OUT1["BenchmarkReport JSON<br/><code>Article 15 technical documentation pack</code>"]
        OUT2["FastAPI REST Interface<br/><code>/v1/evaluate · /v1/runs/compare</code>"]
        OUT3["Rich Terminal UI<br/><code>Distribution tables & pass/fail verdicts</code>"]
    end

    INP1 & INP2 & INP3 --> RUN
    RUN --> CLASSIC & RETRIEVAL & AGENTIC
    CLASSIC & RETRIEVAL & AGENTIC --> STORE
    STORE --> COMP --> HASH
    HASH --> OUT1 & OUT2 & OUT3

    style Inputs fill:#F5F4EF,stroke:#E4E2DC,color:#0F1419
    style Core fill:#E6F4F1,stroke:#0D5463,color:#0D5463
    style Integrity fill:#FAF0E6,stroke:#B68A2E,color:#0F1419
    style Outputs fill:#F5F4EF,stroke:#E4E2DC,color:#0F1419
```

---

## What RAG Benchmarking Does

- **Framework-Agnostic Adapters**: Native adapters for LangChain, LlamaIndex, Haystack, and raw Python dictionaries.
- **12+ Specialized Metrics**: Evaluates factual grounding, retrieval precision, citation accuracy, and agentic tool selection.
- **Pre-Packaged Golden Evaluation Dataset**: Includes 50 curated enterprise question-context-answer samples across 10 regulatory and domain topics.
- **Statutory Article 15 Declarations**: Generates the exact declared accuracy and faithfulness metrics required by Annex IV technical documentation packs.
- **Embedded SQLite Persistence**: Local database stores all historic runs, enabling instant diffs and regression testing between model versions.
- **Zero-Telemetry Guarantee**: 100% local and offline execution. Prompts, documents, and evaluation scores never leave your infrastructure.

---

## Supported Evaluation Metrics

### 1. Generation & RAG Quality Metrics

| Metric | Description | Evaluator Type |
| :--- | :--- | :--- |
| `faithfulness` | Measures factual consistency of the answer against retrieved context (hallucination detection) | LLM Judge |
| `answer_relevancy` | Measures whether the generated answer directly addresses the original question | LLM Judge |
| `context_precision` | Measures whether ground-truth relevant chunks are ranked higher in retrieved context | LLM Judge |
| `context_recall` | Measures whether retrieved context contains all facts required to answer the question | LLM Judge |

### 2. Deterministic Retrieval Metrics

| Metric | Description | Evaluator Type |
| :--- | :--- | :--- |
| `precision_at_k` | Proportion of top-K retrieved documents that are relevant | Deterministic |
| `recall_at_k` | Proportion of all relevant documents captured in top-K retrieval | Deterministic |
| `mrr` | Mean Reciprocal Rank of the first relevant retrieved document | Deterministic |
| `ndcg_at_k` | Normalized Discounted Cumulative Gain accounting for position relevance | Deterministic |

### 3. Agentic-Era Trace Metrics

| Metric | Description | Evaluator Type |
| :--- | :--- | :--- |
| `source_attribution_accuracy` | Verifies whether citations match actual retrieved chunk identifiers | Deterministic |
| `agent_faithfulness` | Evaluates factual grounding across every intermediate reasoning step | LLM Judge |
| `tool_call_accuracy` | Verifies whether the agent selected appropriate tools for the sub-task | LLM Judge |
| `retrieval_necessity` | Measures whether external retrieval was genuinely required or superfluous | LLM Judge |

### Metric Groups
Evaluate pre-configured metric suites with a single parameter:
```python
report = client.evaluate(samples, metric_group="classic")      # faithfulness, answer_relevancy, context_precision, context_recall
report = client.evaluate(samples, metric_group="retrieval")    # precision@k, recall@k, mrr, ndcg@k
report = client.evaluate(samples, metric_group="agentic_v1")   # source_attribution, agent_faithfulness, tool_accuracy
report = client.evaluate(samples, metric_group="full")         # all supported metrics
```

---

## Interactive Artifact Previews

<details>
  <summary><b>📊 View Structured Benchmark Report Output (JSON)</b></summary>

```json
{
  "$schema": "https://schemas.aiexponent.com/rag-benchmarking/v1/report.schema.json",
  "schema_version": "1.0.0",
  "report_id": "rep_rag_20260615_7b3a9c",
  "pipeline_id": "enterprise-customer-rag-v2",
  "evaluated_at": "2026-06-15T10:30:00Z",
  "evaluation_context": {
    "framework": "rag-benchmarking-harness",
    "version": "1.0.2",
    "dataset": "golden-qa-50",
    "dataset_uri": "https://github.com/aiexponent/rag-benchmarking/blob/main/data/golden/qa.jsonl",
    "sample_count": 50,
    "model": "gemini-2.5-flash",
    "embedder": "text-embedding-004"
  },
  "regulatory_mapping": {
    "framework": "EU AI Act",
    "article": "Article 15 (Accuracy, Robustness and Cybersecurity)",
    "threshold_policy": "high_risk_minimum_standards_v1",
    "verdict": "PASS"
  },
  "metrics": {
    "faithfulness": 0.958,
    "answer_relevancy": 0.942,
    "context_recall": 0.915,
    "context_precision": 0.928,
    "citation_precision": 0.978,
    "groundedness": 0.962
  },
  "compliance_summary": {
    "status": "CONFORMING",
    "minimum_faithfulness_required": 0.900,
    "measured_faithfulness": 0.958,
    "maximum_hallucination_tolerated": 0.080,
    "measured_hallucination": 0.042,
    "audit_trail_signature": "sha256:d8a29b4e11c52b7a9e3d8f4c2e6b0a1f5c7e9d3b2a8f1e0c4b6d8a2f1e9c7b5a"
  }
}
```
</details>

<details>
  <summary><b>📄 View Golden QA Dataset Sample (JSONL)</b></summary>

```json
{
  "sample_id": "03fd8be3-1051-4213-acda-0fc242447018",
  "question": "What does RAG stand for and what problem does it solve?",
  "contexts": [
    "RAG stands for Retrieval-Augmented Generation. It combines information retrieval with large language model generation.",
    "Traditional LLMs are limited to knowledge from their training data. RAG allows dynamic access to external knowledge at inference time."
  ],
  "answer": "RAG stands for Retrieval-Augmented Generation. It solves the hallucination problem by grounding LLM responses in retrieved documents.",
  "ground_truths": [
    "RAG stands for Retrieval-Augmented Generation and reduces hallucination by grounding responses in retrieved documents."
  ],
  "relevant_doc_ids": ["rag-1", "rag-2"]
}
```
</details>

<details>
  <summary><b>⚙️ View Starter Configuration (.env)</b></summary>

```bash
# LLM Judge Provider
LLM_PROVIDER=gemini              # gemini (recommended) or openai
GEMINI_API_KEY=your-gemini-key
OPENAI_API_KEY=your-openai-key

# Vector Store (for built-in RAG pipeline)
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your-qdrant-key

# API Authentication & Security
API_KEY=your-secure-api-key
ENFORCE_API_KEY=true
```
</details>

---

## CI/CD Integration & Exit Codes

Integrate RAG Benchmarking into your CI/CD pipeline as an automated accuracy gate to prevent regression and hallucinations:

```yaml
# .github/workflows/accuracy-gate.yml
name: AI Accuracy & Faithfulness Gate
on: [pull_request, push]

jobs:
  accuracy-benchmark:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install rag-benchmarking
      - name: Run Benchmark Gate
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: |
          python scripts/evaluate.py \
            --dataset data/golden/qa.jsonl \
            --metric-group classic \
            --min-faithfulness 0.90 \
            --output benchmark-report.json
      - uses: actions/upload-artifact@v4
        with:
          name: benchmark-evidence
          path: benchmark-report.json
```

### Exit Code Contract

RAG Benchmarking implements deterministic UNIX exit codes for scripting, pre-commit hooks, and CI gates:

| Exit Code | Meaning | CI Gate Behavior |
| :--- | :--- | :--- |
| `0` | **COMPLIANT / PASS** | All accuracy, faithfulness, and retrieval metrics satisfy configured threshold policies. |
| `1` | **THRESHOLD BREACH** | One or more evaluation metrics fell below the required compliance threshold (e.g. faithfulness < 0.90). |
| `2` | **CONFIG / ERROR** | Malformed dataset, invalid schema, missing target, or LLM judge provider connection failure. |

---

## CLI & SDK Command Reference

| Interface | Method / Script | Description |
|---|---|---|
| **Python SDK** | `RagEval.evaluate(samples, metrics=...)` | Evaluates question-context-answer samples across selected metric suites. |
| **Python SDK** | `RagEval.evaluate_agent(trace, metrics=...)` | Evaluates multi-step agent traces for tool accuracy and source attribution. |
| **Python SDK** | `RagEval.from_langchain(result)` | Adapter converting LangChain invocation dictionaries into `EvalSample` instances. |
| **Python SDK** | `RagEval.from_llamaindex(response)` | Adapter converting LlamaIndex response objects into `EvalSample` instances. |
| **Harness Engine** | `EvaluationRunner.run(dataset, config)` | Core evaluation pipeline executing LLM judges and deterministic math scorers. |
| **Persistence** | `ResultStore.save_run(report)` | Persists benchmark runs, sample scores, and distributions into SQLite. |
| **CLI Script** | `python scripts/evaluate.py [OPTIONS]` | CLI runner supporting dataset files, metric groups, and threshold gates. |
| **REST Server** | `uvicorn rag_benchmarking.app.main:app` | FastAPI server exposing `/v1/evaluate` and `/v1/runs` endpoints. |

---

## EU AI Act Article 15 — Empirical Evidence Scope

`rag-benchmarking` is an **evaluation harness** that provides empirical accuracy and faithfulness measurements for RAG and agentic AI systems. Those metrics serve as critical input to Article 15 technical documentation, but do **not** constitute conformity assessment by themselves.

```mermaid
graph LR
    RAG["rag-benchmarking\nevaluation harness"]
    FAITH["Faithfulness & Grounding\n(LLM-judge)"]
    RET["Retrieval Quality & Precision\n(deterministic)"]
    AGENT["Agentic Tool & Attribution\n(trace evaluation)"]
    REPORT["BenchmarkReport\n(Empirical telemetry for\nArticle 15(1) accuracy declarations)"]

    RAG --> FAITH --> REPORT
    RAG --> RET --> REPORT
    RAG --> AGENT --> REPORT

    style RAG fill:#FAF0E6,stroke:#B68A2E,color:#0F1419
    style FAITH fill:#F5F4EF,stroke:#E4E2DC,color:#0F1419
    style RET fill:#F5F4EF,stroke:#E4E2DC,color:#0F1419
    style AGENT fill:#F5F4EF,stroke:#E4E2DC,color:#0F1419
    style REPORT fill:#E6F4F1,stroke:#0D5463,color:#0D5463
```

### What this tool covers
* **Article 15(1) — Declared accuracy metrics in instructions for use**: Produces reproducible accuracy and faithfulness benchmarks that providers cite in technical documentation (Annex IV §2(b)) and instructions for use (Article 13).

### What this tool does NOT cover
* **Article 15 Robustness**: Robustness under the EU AI Act entails adversarial input testing, out-of-distribution resilience, and perturbation analysis. (A faithfulness scorer is not an adversarial robustness test).
* **Article 15 Cybersecurity**: Jailbreak resistance, prompt injection defenses, and pipeline security require dedicated runtime defenses.
* **Conformity Assessment**: High-risk AI systems require formal conformity assessment procedures under Article 43. Benchmark reports provide supporting technical evidence, not regulatory certification.

---

## AiExponent Ecosystem Integration

`rag-benchmarking` integrates directly into the AiExponent regulatory compliance toolchain:

```mermaid
graph LR
    LCC["LCC\n(Art. 53 Licenses)"]
    RAG["rag-benchmarking\n(Art. 15 Accuracy)"]
    RF["RiskForge\n(Art. 9 Risk Management)"]
    DOC["Document Analyser\n(Annex IV Tech Docs)"]

    LCC -->|"license compliance SBOM"| RF
    RAG -->|"benchmark_report.json\naccuracy evidence"| RF
    RF -->|"tamper-evident RMF"| DOC

    style RAG fill:#FAF0E6,stroke:#B68A2E,color:#0F1419
    style LCC fill:#F5F4EF,stroke:#E4E2DC,color:#0F1419
    style RF fill:#E6F4F1,stroke:#0D5463,color:#0D5463
    style DOC fill:#F5F4EF,stroke:#E4E2DC,color:#0F1419
```

---

## Configuration

Configure evaluation parameters via `.env`:

```bash
# LLM Judge Provider
LLM_PROVIDER=gemini              # gemini (recommended) or openai
GEMINI_API_KEY=your-gemini-key
OPENAI_API_KEY=your-openai-key

# Optional Vector Store (for built-in reference RAG pipeline)
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your-qdrant-key

# API Authentication & Security
API_KEY=your-secure-api-key
ENFORCE_API_KEY=true
```

---

## Project Structure

```
src/
  rag_benchmarking/
    __init__.py          # Public exports (RagEval, EvaluationRunner, ResultStore, ...)
    sdk/                 # Dedicated SDK entrypoint (from rag_benchmarking.sdk import RagEval)
    harness/             # Framework-agnostic benchmark harness
      schemas.py         # EvalSample, AgentTrace, BenchmarkReport, RunConfig
      protocol.py        # RAGEvaluable Protocol — plug-in interface
      runner.py          # EvaluationRunner — metric orchestration
      result_store.py    # SQLite persistence & run comparisons
    app/
      api/               # FastAPI endpoints (/v1/evaluate, /v1/runs)
      eval/              # RAGAS and custom metric runners
      retrieval/         # Chunking, embeddings, Qdrant store, reranker
      engine/            # RAGEngine reference implementation
      llm/               # Unified LLM client (OpenAI & Gemini)
      config/            # Pydantic settings & environment configuration
data/
  golden/qa.jsonl        # 50-sample golden evaluation dataset (10 domains)
```

---

## Important Disclaimers

RAG Benchmarking is an engineering evaluation harness designed to automate empirical testing, hallucination scoring, and accuracy declarations.

1. **Not Legal Advice**: Use of RAG Benchmarking does not constitute legal counsel, statutory audit, or regulatory compliance certification.
2. **Not a Notified Body**: RAG Benchmarking produces technical documentation artifacts under Annex IV; it does not replace third-party conformity assessment under Article 43 where required.
3. **Model Dependencies**: Metrics scored via LLM-as-a-Judge reflect the evaluation model's assessment and should be paired with deterministic retrieval metrics and human oversight.

---

## Privacy & Zero-Telemetry Guarantee

<a name="privacy"></a>

RAG Benchmarking operates completely locally and offline with **zero telemetry**, no phone-home calls, and no usage analytics. Your proprietary golden datasets, test prompts, system architectures, and evaluation outputs remain strictly within your local environment or private VPC.

---

## Releases

| Version | Highlights |
|---|---|
| **[v1.0.2](https://github.com/aiexponent/rag-benchmarking/releases/tag/v1.0.2)** | Dual-mode enterprise banners, 4-layer architecture, 'Why RAG Benchmarking' matrix, artifact inspector, namespace isolation (`rag_benchmarking`), unmasked CI gates (`mypy`, `pip-audit`, `lcc`), Contributor Covenant 2.1 Code of Conduct, 5-tool reciprocal footer, flat-square badges, and Dependabot. |
| [v1.0.1](https://github.com/aiexponent/rag-benchmarking/releases/tag/v1.0.1) | Agent endpoint shape parity (`scores` → `metrics`), SDK plural `ground_truths` docstring alignment, Gemini 2.5 Flash default. |
| [v1.0.0](https://github.com/aiexponent/rag-benchmarking/releases/tag/v1.0.0) | Production baseline release: Path A reframing, schema reconciliation, authenticity pass, 50-sample golden dataset. |

---

## Contributing

We welcome community contributions! Please review [CONTRIBUTING.md](CONTRIBUTING.md) for local setup, commit conventions, and testing instructions.

```bash
git clone https://github.com/aiexponent/rag-benchmarking.git
cd rag-benchmarking
pip install -e ".[test,lint]"
make lint
make test
```

---

## License

[Apache 2.0](LICENSE) — free to use, modify, and distribute.

Built by [AI Exponent LLC](https://aiexponent.com) — `hello@aiexponent.com`

---

*Part of the AiExponent open-source AI governance toolchain:*  
[litmusai](https://github.com/aiexponent/litmusai) (Art. 5) · 
[license-compliance-checker](https://github.com/aiexponent/license-compliance-checker) (Art. 53) · 
**rag-benchmarking** (Art. 15) · 
[riskforge](https://github.com/aiexponent/riskforge) (Art. 9) · 
[agentic-document-analyser](https://github.com/aiexponent/agentic-document-analyser) (Art. 9 / Annex IV)

---

<div align="center">
  <sub>
    <a href="https://aiexponent.com">aiexponent.com</a> ·
    <a href="mailto:hello@aiexponent.com">hello@aiexponent.com</a> ·
    Built in the open · Apache 2.0
  </sub>
</div>
