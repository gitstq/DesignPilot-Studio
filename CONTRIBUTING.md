# 🤝 Contributing to DesignPilot Studio

Thank you for your interest in contributing to DesignPilot Studio! This document provides guidelines for contributing.

## 📋 How to Contribute

### Reporting Bugs
1. Check if the bug has already been reported in [Issues](https://github.com/gitstq/DesignPilot-Studio/issues)
2. If not, create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment info (OS, Python version)

### Suggesting Features
1. Open an issue with the `[Feature]` label
2. Describe the feature and its use case
3. If possible, provide examples of how it would work

### Submitting Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Add tests for new functionality
5. Run tests: `python tests/test_core.py`
6. Commit with conventional commit format:
   - `feat: add new feature`
   - `fix: fix bug`
   - `docs: update documentation`
   - `refactor: code refactoring`
7. Push and create a Pull Request

## 🏗️ Development Setup

```bash
# Clone the repository
git clone https://github.com/gitstq/DesignPilot-Studio.git
cd DesignPilot-Studio

# No dependencies needed! Just Python 3.8+
python -m src.cli --help

# Run tests
python tests/test_core.py
```

## 📝 Code Style
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to all public functions/classes
- Keep functions focused and small

## 📄 License
By contributing, you agree that your contributions will be licensed under the MIT License.
