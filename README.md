# Project ReFrame: RCAC Test Orchestration

This repository contains the implementation and automation of **ReFrame**, a specialized regression testing framework, for the **Negishi cluster**. The project transitions manual system checks into a suite of automated, reproducible Python-based tests to ensure system stability and performance reliability.

---

## 📂 Repository Structure

The project is organized into modular components for CLI management, data tracking, and ReFrame-specific logic:

* **`cli/`**: Command-line application modules, including entrypoints, configuration, reporting, and runners.
* **`reframe/`**: The core testing logic.
    * **`settings/`**: System configuration profiles (e.g., Slurm configuration).
    * **`suites/`**: YAML definitions for different run types like nightly, weekly, or cluster upgrades.
    * **`tests/`**: Categorized test implementations:
        * **`sanity/`**: "Smoke" tests for filesystem availability, environment integrity, and basic connectivity.
        * **`performance/`**: Benchmarks for DRAM (STREAM), CPU (HPL), and Interconnect (OSU).
        * **`regression/`**: Specialized checks to prevent the recurrence of known issues.
* **`data/artifacts/`**: Storage for test run results and diagnostic logs.
* **`docs/`**: Detailed usage guides and project documentation.
