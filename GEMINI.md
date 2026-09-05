# Project: Heuristics in Property Portfolio Selection Decisions of Nigerian Pension Funds

This project is a comprehensive research monorepo for a dissertation at Obafemi Awolowo University. It aims to analyze how Nigerian Pension Fund Administrators (PFAs) make real estate investment decisions using heuristics versus algorithmic optimization.

## Project Overview

The system is designed as a multi-tier monorepo consisting of analytical tools, a data persistence layer, and an interactive simulator.

### Core Architecture

- **Analytical Core (Python):** Handles synthetic universe generation, heuristic scoring, and Markowitz Mean-Variance Optimization (MVO).
- **Backend Services (Java/Spring Boot):** Provides an API for data persistence, property querying, and serving the frontend.
- **Interactive Simulator (Next.js):** A public-facing web application that allows users to compare heuristic-driven portfolios with optimized ones.

### Package Breakdown

- `packages/generator`: Python-based property universe generator. Calibrates 80 properties based on Nigerian market indices.
- `packages/optimizer`: Python/FastAPI service for MVO optimization, heuristic engine, and Monte Carlo simulations.
- `packages/research-backend`: Java 17 / Spring Boot 3.2 application for managing property and portfolio data.
- `packages/simulator`: Next.js 14 / TypeScript / Tailwind CSS interactive frontend.
- `packages/utils`: Helper scripts, including PDF data extraction for market reports.

## Building and Running

### Prerequisites

- Python 3.10+
- Java 17+ (Maven)
- Node.js 18+
- Docker & Docker Compose (for PostgreSQL and service orchestration)

### Setup Commands

- **Python Packages:** 

  ```bash
  cd packages/generator && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
  cd packages/optimizer && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
  ```

- **Java Backend:**

  ```bash
  cd packages/research-backend && mvn clean install
  ```

- **Frontend Simulator:**

  ```bash
  cd packages/simulator && npm install
  ```

### Execution (Development)

- **Optimizer API:** `cd packages/optimizer && uvicorn main:app --reload`
- **Research Backend:** `cd packages/research-backend && mvn spring-boot:run`
- **Simulator:** `cd packages/simulator && npm run dev`

## Development Conventions

### Data Integrity & Reproducibility

- **The Frozen Universe Policy:** Once generated, the synthetic property universe in `data/frozen/` is **read-only**. Changing the random seed (default: 42) or calibration parameters after freezing invalidates the study's longitudinal consistency.
- **Market Data:** All secondary market data must be cited in `data/calibration/calibration_notes.md`.

### Technical Standards

- **Python:** Use Pydantic for data validation (especially in extraction and API layers). Prefer `numpy` and `pandas` for all statistical calculations.
- **Java:** Follow standard Spring Boot hexagonal/layered architecture (Entity -> Repository -> Service -> Controller).
- **Testing:** 
  - Python scripts must include basic validation checks (see `packages/generator/validate_universe.py`).
  - Java services require JUnit/Mockito tests for core business logic.
- **Documentation:** Maintain the `implementation-checklist.md` as the primary source of truth for project status and upcoming tasks.

## Key Files

- `implementation-checklist.md`: The master project plan and technical roadmap.
- `data/frozen/`: Contains the ground-truth property universe and market indices.
- `packages/utils/extract_reports.py`: Tool for extracting market data from PDF reports using Gemini 2.5 Flash.
