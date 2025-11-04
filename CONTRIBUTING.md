# Contributing to InGen Systems - YouTube Retrieval Console

First off, thank you for considering contributing to this project! 🦖

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected behavior**
- **Actual behavior**
- **Screenshots** (if applicable)
- **System information** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case**: Why would this be useful?
- **Possible implementation**: If you have ideas
- **Examples**: Similar features in other apps

### Pull Requests

- Fill in the required template
- Follow the style guidelines
- Include screenshots for UI changes
- Update documentation as needed
- Add tests if applicable

## Development Setup

1. **Fork and clone the repository**
```bash
git clone https://github.com/your-username/jurassic-youtube-downloader.git
cd jurassic-youtube-downloader
```

2. **Create a virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a new branch**
```bash
git checkout -b feature/your-feature-name
```

## Style Guidelines

### Python Code Style

- Follow **PEP 8** style guide
- Use **4 spaces** for indentation (no tabs)
- Maximum line length: **100 characters**
- Use descriptive variable names
- Add comments for complex logic

### Comments Style

Write comments as if you're a beginner explaining the code:
```python
# Good: Simple, clear explanation
# Loop through each file and check if it exists
for file in files:
    if file.exists():
        process_file(file)

# Bad: Too formal or AI-like
# Iterate through the file collection, verifying existence prior to processing
```

### UI/UX Guidelines

- Maintain the Jurassic Park theme (amber/orange and green colors)
- Use Courier New font for consistency
- Keep the retro terminal aesthetic
- Test all UI changes at 1024x768 resolution minimum

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests after the first line

Examples:
```
Good:
Add FFmpeg installation dialog
Fix progress bar animation timing
Update README with installation steps

Bad:
Added some stuff
fixed bug
updates
```

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Example:**
```
feat(ui): Add blinking animation to live indicator

Implement blinking effect for the LIVE FEED indicator
and the "Ready to initialize..." text to enhance the
Jurassic Park terminal aesthetic.

Closes #123
```

## Pull Request Process

1. **Update documentation** for any user-facing changes
2. **Update CHANGELOG.md** with your changes
3. **Test thoroughly** on Windows 10/11
4. **Ensure no linting errors**
5. **Update README.md** if adding new features
6. **Add screenshots** for visual changes
7. **Request review** from maintainers

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Comments are clear and beginner-friendly
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] All tests pass
- [ ] No merge conflicts
- [ ] Screenshots added (if UI changes)

## Testing

### Manual Testing

Before submitting a PR, test:

1. **Fresh Installation**
   - Delete `.venv` folder
   - Run `run_gui.bat`
   - Verify auto-installation works

2. **Core Features**
   - Download MP4 video
   - Download MP3 audio (with FFmpeg)
   - Download WEBM video
   - Cancel download mid-way
   - Run System Diagnostics

3. **UI Elements**
   - Test all keyboard shortcuts (F1, F2, F3)
   - Verify blinking animations
   - Check progress bar smoothness
   - Test custom T-Rex image loading

4. **Error Handling**
   - Invalid URL
   - No internet connection
   - Missing dependencies
   - FFmpeg not installed (MP3)

## Areas for Contribution

### High Priority
- [ ] Add support for playlist downloads
- [ ] Implement download queue system
- [ ] Add subtitle download option
- [ ] Create macOS/Linux compatibility

### Medium Priority
- [ ] Add video preview before download
- [ ] Implement download history
- [ ] Add dark/light theme toggle (while keeping JP aesthetic)
- [ ] Create portable executable version

### Low Priority
- [ ] Add more keyboard shortcuts
- [ ] Implement drag-and-drop URL support
- [ ] Add system tray icon
- [ ] Create installer wizard

## Questions?

Feel free to:
- Open an issue with the `question` label
- Start a discussion on GitHub Discussions
- Reach out to maintainers

---

**Thank you for contributing! 🦖⚡**

*"Life finds a way... to make great software."*

