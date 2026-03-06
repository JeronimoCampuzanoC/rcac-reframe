# Project ReFrame: RCAC Test Orchestration

This repository contains the implementation and automation of **ReFrame**, a specialized regression testing framework, for the **Negishi cluster**. The project transitions manual system checks into a suite of automated, reproducible Python-based tests to ensure system stability and performance reliability.

## Tool Versions

- ReFrame: `4.10.0-dev.1+998bf083`
- Conda: `25.3.1`
- Python: `3.10.19`

---

## 📂 Repository Structure

The project is organized into modular components for CLI management, data tracking, and ReFrame-specific logic:

- **`cli/`**: Command-line application modules, including entrypoints, configuration, reporting, and runners.
- **`reframe/`**: The core testing logic.
  - **`settings/`**: System configuration profiles (e.g., Slurm configuration).
  - **`suites/`**: YAML definitions for different run types like nightly, weekly, or cluster upgrades.
  - **`tests/`**: Categorized test implementations:
    - **`sanity/`**: "Smoke" tests for filesystem availability, environment integrity, and basic connectivity.
    - **`performance/`**: Benchmarks for DRAM (STREAM), CPU (HPL), and Interconnect (OSU).
    - **`regression/`**: Specialized checks to prevent the recurrence of known issues.
- **`data/artifacts/`**: Storage for test run results and diagnostic logs.
- **`docs/`**: Detailed usage guides and project documentation.

---

## Installation

Conda was used to install ReFrame. We created a Conda environment called `reframe-env` with Python `3.10.19`, due to dependencies that are not available in the default Python module on Negishi.

Load Conda, create the environment, and activate it:

```bash
module load conda
conda create -n reframe-env python=3.10.19 -y
conda activate reframe-env
```

Then run:

```bash
pushd /path/to/install/prefix
git clone -q --depth 1 --branch 4.10.0-dev.1+998bf083 https://github.com/reframe-hpc/reframe.git
pushd reframe && ./bootstrap.sh && popd
export PATH=$(pwd)/bin:$PATH
popd
```

To make this persistent on each shell start:

```bash
nano ~/.bashrc
```

Add:

```bash
export PATH=/home/jcampuz/reframeImpl/reframe/bin:$PATH
```

Then reload:

```bash
source ~/.bashrc
```
