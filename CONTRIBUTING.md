# Contributing Guidelines

Thank you for your interest in the AgriGuard: InsectVision project!

## How to Contribute

### Reporting Issues
1. Check existing issues first
2. Provide clear description with:
   - Python version
   - TensorFlow version
   - Error message (full traceback)
   - Steps to reproduce

### Improving Documentation
- Fix typos or clarify instructions
- Add examples or use cases
- Improve README or guides

### Code Improvements
- Model architecture enhancements
- Data augmentation strategies
- Ensemble method optimizations
- Performance improvements

### Dataset Contributions
- Link to new insect datasets
- Class distribution analysis
- Data quality improvements

## Development Setup

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/AgriGuard-InsectVision.git
cd AgriGuard-InsectVision

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows

# Install dependencies
pip install -r requirements.txt
```

## Testing Your Changes

Before submitting a pull request:
1. Run the notebook to ensure no errors
2. Test with different dataset sizes
3. Verify outputs are generated correctly
4. Update documentation if needed

## Commit Guidelines

```
Format: [TYPE] Brief description

Types:
- [FEATURE] New functionality
- [FIX] Bug fix
- [DOCS] Documentation update
- [REFACTOR] Code reorganization
- [TEST] Test additions

Example:
[FEATURE] Add VGG16 model variant
[FIX] Resolve GPU memory leak in batch processing
[DOCS] Clarify dataset structure requirements
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "[FEATURE] Description"`
4. Push to fork: `git push origin feature/your-feature`
5. Submit pull request with detailed description

## Code Style

- Python: Follow PEP 8
- Notebook cells: Keep focused on single task
- Comments: Explain "why" not just "what"
- Variable names: Use descriptive names

## Areas for Contribution

### High Priority
- ✅ Support for additional CNN architectures (EfficientNet, DenseNet)
- ✅ Automated hyperparameter tuning
- ✅ Cross-validation framework
- ✅ Real-time inference API

### Medium Priority
- 📊 Additional ensemble methods (Voting variants, Blending)
- 📊 Class imbalance handling (SMOTE, weighted loss)
- 📊 Explainability (LIME, SHAP)

### Nice to Have
- 🎨 Web UI for inference
- 🎨 Model compression (quantization, pruning)
- 🎨 Multi-GPU support optimization

## Code of Conduct

- Be respectful and constructive
- Welcome diverse perspectives
- Help others learn
- No harassment or discrimination

## Questions?

- Open an issue with [QUESTION] tag
- Check existing documentation first

Thank you for contributing! 🌱

---

**Last Updated**: 2026-05-15
