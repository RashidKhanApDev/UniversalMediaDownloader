# GitHub Copilot Custom Instructions for UniversalMediaDownloader

When writing code for this repository, adhere to the following rules:

1. **Tech Stack**: Use Python 3.10+, FastAPI, and standard Python conventions (PEP 8). For frontend, use raw HTML/JS/CSS with glassmorphism aesthetics. No TailwindCSS.
2. **Architecture**: Keep routing logic in `main.py` simple. Offload heavy media processing to background tasks.
3. **Naming**: Use `snake_case` for Python variables and functions, `PascalCase` for classes.
4. **Security**: Never hardcode API keys or absolute system paths. Use environment variables.
5. **Documentation**: Add Google-style docstrings to all new functions.
