# jio-analysis-agent

This repository contains the `jio-analysis-agent` project, which includes a `KundaliSiderealChart` class for astrological chart calculations and associated utilities.

## Setup

To set up the project and its development environment, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/jio-analysis-agent.git
    cd jio-analysis-agent
    ```

2.  **Install `uv` (if you don't have it):**

    `uv` is a fast Python package installer and resolver. If you don't have it, install it using pip:

    ```bash
    brew install uv
    ```

3.  **Create and Activate a Virtual Environment:**

    It's highly recommended to use a virtual environment to manage project dependencies.

    ```bash
    uv venv --python 3.11
    ```

    Activate the environment:

    *   On macOS/Linux:

        ```bash
        source .venv/bin/activate
        ```

    *   On Windows:

        ```bash
        .venv\Scripts\activate
        ```

4.  **Install Dependencies:**

    Compile the `requirements.in` file to `requirements.txt` to pin package versions, then install them:

    ```bash
    uv pip compile requirements.in -o requirements.txt
    uv pip install -r requirements.txt
    ```

## Running Tests

To ensure the project's functionality is working as expected, you can run the unit tests:

1.  **Activate your virtual environment** (if not already active, see Setup section).

2.  **Execute pytest:**

    ```bash
    python -m pytest
    ```

    This command will discover and run all tests located in the `test/` directory.

3.  **Freeze Environment (after tests pass):**

    After all tests pass and you are satisfied with the environment, you can freeze the installed packages to `requirements.txt`:

    ```bash
    uv pip freeze > requirements.txt
    ```

## Project Structure

*   `chart/`: Contains the core logic for astrological chart calculations.
    *   `kundali_sidereal_chart.py`: Main class for Kundali chart generation.
    *   `utils.py`: Utility functions used across the project.
    *   `data_processor.py`: (Planned) For data processing functionalities.
*   `test/`: Contains unit tests for the `chart/` module.
    *   `test_kundali_sidereal_chart.py`: Unit tests for `kundali_sidereal_chart.py`.
*   `requirements.in`: Unpinned project dependencies.
*   `requirements.txt`: Pinned project dependencies (generated from `requirements.in`).
*   `.github/instructions/`: Contains detailed instructions and plans for development tasks.