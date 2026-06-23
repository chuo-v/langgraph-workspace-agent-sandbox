# langgraph-workspace-agent-sandbox

A dedicated, isolated sandbox environment designed for functional testing and validating the capabilities of the [langgraph-workspace-agent](https://github.com/chuo-v/langgraph-workspace-agent).

This repository acts as a safe, automated testbed for evaluating the agent's performance across file-system manipulations, code editing, pre-commit validations, and multi-suite GitOps workflows (automated pull requests and branch management).

## 📁 Repository Structure

```text
langgraph-workspace-agent-sandbox/
├── config/
│ └── toggle_settings.yaml # Sandbox behavioral configuration toggles
├── latex/
│ └── test-doc.tex # Sample LaTeX source file for formatting/compilation tasks
│ └── test-doc.pdf # Compiled reference PDF document
├── scripts/
│ └── data_processor.py # Core baseline target script for evaluation tasks
├── tests/
│ ├── test_data_processor.py # Unit tests verifying Python logic and arguments
│ └── test_documentation.py # Linting tests verifying Markdown structure and validity
├── .gitignore # Standard exclusions for OS, Python, and LaTeX build files
└── README.md # Project documentation
```

## 🛠️ Integrated Verification Suites

The sandbox comes pre-configured with two distinct verification layers to simulate standard industry CI/CD gates. This dual-suite architecture ensures that the workspace agent can seamlessly validate changes across different testing paradigms (such as unit testing and documentation linting) during its execution lifecycle.

### 1. Code Quality & Formatting (Pre-Commit Tiers)

Managed via localized Docker isolation, the codebase enforces strict compliance checks using **Ruff**:

* **Ruff Format:** Formats files to comply with PEP 8 standards.
* **Ruff Check & Fix:** Automatically analyzes, reports, and refactors syntax errors or stylistic issues.

### 2. Evaluation CI Suites

The test suites are constructed using Python's native `unittest` framework to provide standard, structured log outputs optimized for agent debugging:

* **Data Processor Unit Tests (`tests/test_data_processor.py`):** Validates baseline script execution, argument passing, and edge-case type parsing.
* **Documentation Validation (`tests/test_documentation.py`):** Ensures project files and titles conform to markdown specs and checks for empty or broken documentation links.

## 🚀 Running the Tests Locally

You can manually execute the validation suites from the repository root using the following commands:

```bash
# Run the Data Processor verification suite
python tests/test_data_processor.py

# Run the Documentation validation suite
python tests/test_documentation.py
```