# Deployment & Setup Guide - AgriGuard: InsectVision

Complete step-by-step instructions for deploying and running AgriGuard: InsectVision.

## System Requirements

### Minimum Requirements
- Python 3.8+
- 4 GB RAM
- 2 GB disk space (for dependencies)

### Recommended (for Training)
- Python 3.9+
- 8+ GB RAM
- GPU with CUDA support (NVIDIA recommended)
- 5+ GB disk space

### GPU Setup (Optional but Recommended)
If you have an NVIDIA GPU:
```bash
# Install CUDA and cuDNN - follow TensorFlow GPU setup:
# https://www.tensorflow.org/install/gpu

# Verify TensorFlow GPU detection:
python -c "import tensorflow as tf; print('GPUs:', len(tf.config.list_physical_devices('GPU')))"
```

---

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/AgriGuard-InsectVision.git
cd AgriGuard-InsectVision
```

### 2. Create Virtual Environment (Recommended)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Expected Installation Time**: 5-10 minutes

**Verify Installation**:
```bash
python -c "import tensorflow as tf; print(f'TensorFlow {tf.__version__} installed')"
```

---

## Quick Test (No Training)

Run the demo notebook with pre-trained models:

```bash
jupyter notebook QUICK_DEMO_NO_TRAINING.ipynb
```

**What this does**:
- Loads pre-trained models (if available)
- Evaluates on your test dataset
- Generates confusion matrices and metrics
- Complete in < 5 minutes

**Expected Output**:
- Accuracy percentage for each model
- Confusion matrix visualization
- Model comparison chart

---

## Full Training (Recommended)

### Step 1: Prepare Your Dataset

Create this directory structure:
```
AGRO/
├── train/
│   ├── Pests_Grasshopper/
│   │   ├── image_001.jpg
│   │   ├── image_002.jpg
│   │   └── ...
│   ├── Pests_Locust/
│   ├── Benign_Bee/
│   ├── Benign_Butterfly/
│   ├── Disease_Leaf_Spot/
│   ├── Disease_Powdery_Mildew/
│   ├── Disease_Rust/
│   ├── Beneficial_Ladybug/
│   ├── Beneficial_Spider/
│   ├── Crop_Health_Good/
│   ├── Crop_Health_Average/
│   ├── Crop_Health_Poor/
│   ├── Weed_Broadleaf/
│   ├── Weed_Grassy/
│   └── Other/
└── test/
    ├── Pests_Grasshopper/
    ├── Pests_Locust/
    └── ... (same 15 classes)
```

**Image Requirements**:
- Format: JPG/PNG
- Minimum: 100 images per class in training set
- Recommended: 500+ images per class
- Images will be resized to 224×224

### Step 2: Run the Full Notebook

```bash
jupyter notebook NEW_FINAL_VERSION_8_9_INSECT_DETECTION.ipynb
```

**Execution Flow**:
1. **Cell 1**: Import libraries and check TensorFlow (1 min)
2. **Cell 2-4**: Load and preprocess data (5 min)
3. **Cell 5-8**: Build and compile models (2 min)
4. **Cell 9-12**: Train VGG16 (8-10 min)
5. **Cell 13-16**: Train ResNet50 (12-15 min)
6. **Cell 17-20**: Train MobileNetV2 (5-7 min)
7. **Cell 21-24**: Train Xception (15-20 min)
8. **Cell 25+**: Generate visualizations and ensemble results (5 min)

**Total Training Time**:
- GPU: 45 min - 1 hour
- CPU: 2-3 hours

### Step 3: Monitor Progress

The notebook prints progress for each:
- **Data loading**: Number of train/test samples per class
- **Model training**: Per-epoch accuracy and loss
- **Evaluation**: Confusion matrices and metrics
- **Ensemble**: Combined model accuracy

### Step 4: Review Results

Generated files:
```
├── VGG_model.keras              # Trained model
├── ResNet50.keras
├── MobileNetV2.keras
├── Xception.keras
├── vgg16_model_history.csv      # Training history
├── resnet50_model_history.csv
├── mobilenetv2_model_history.csv
├── xception_model_history.csv
├── confusion_matrix_*.png       # Visualizations
├── model_accuracy_comparison.png
└── training_curves.png
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'tensorflow'"

**Solution**:
```bash
# Ensure virtual environment is activated
pip install --upgrade tensorflow

# Verify:
python -c "import tensorflow; print(tensorflow.__version__)"
```

### Issue: GPU Not Detected

**Solution**:
```bash
# Check if GPU is available
python -c "import tensorflow as tf; print(tf.config.list_physical_devices())"

# If empty, GPU drivers need setup - see GPU Setup section above
```

### Issue: Out of Memory (OOM) Error

**Solution**:
```python
# Reduce batch size in notebook:
BATCH_SIZE = 16  # Change from 32 to 16

# Or use MobileNetV2 (smallest model)
# Skip larger models like ResNet50 or Xception
```

### Issue: Dataset Not Found

**Solution**:
```bash
# Verify paths are correct:
# - AGRO/train/<class_name>/ exists
# - AGRO/test/<class_name>/ exists
# - Images are in JPG format

# List your dataset:
ls AGRO/train/
```

### Issue: Training Stops Unexpectedly

**Solution**:
```
# Common causes:
1. Low disk space (need 2+ GB)
2. Corrupted images in dataset
3. Mixed image formats (use JPG only)

# Resume from last saved checkpoint:
# Models are saved as best weights, automatically loaded
```

---

## Performance Optimization

### For Speed (GPU)
```python
# Already optimized:
# - Mixed precision training
# - Parallel data loading
# - GPU-accelerated operations
```

### For Memory (Limited Resources)
```python
# Reduce batch size
BATCH_SIZE = 16

# Use MobileNetV2 only
# (not all models)

# Reduce image size
IMG_SIZE = 160  # from 224
```

### For Best Results
```python
# Use all models
# Run on GPU
# Ensure 500+ images per class
# Use balanced dataset (equal samples per class)
```

---

## Model Deployment

### Save Only Production Model
```python
# After training, copy best model:
import shutil
shutil.copy('Xception.keras', 'production_model.keras')
```

### Load for Inference
```python
from tensorflow.keras.models import load_model

model = load_model('Xception.keras')

# Predict single image
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np

img = keras_image.load_img('sample.jpg', target_size=(224, 224))
img_array = keras_image.img_to_array(img) / 255.0
prediction = model.predict(np.expand_dims(img_array, axis=0))
predicted_class = np.argmax(prediction)
```

---

## Pushing to GitHub

### 1. Initialize Git
```bash
git init
git add -A
git commit -m "Initial commit: Insect detection ML pipeline"
```

### 2. Create GitHub Repository
- Go to github.com → New Repository
- Name: `AgriGuard-InsectVision`
- Add to your CV

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/AgriGuard-InsectVision.git
git branch -M main
git push -u origin main
```

### What's Visible on GitHub:
- ✅ Notebook code (all fixes applied)
- ✅ Documentation (README, RESULTS, this guide)
- ✅ Demo outputs (proof of performance)
- ❌ Dataset (too large, ignored)
- ❌ Model files (too large, can be generated)

---

## Next Steps

1. **Test Locally**: Run quick demo first
2. **Train Models**: Run full notebook with your data
3. **Review Results**: Check generated visualizations
4. **Push to GitHub**: Share your portfolio
5. **Update CV**: Link to repository

---

## Support

For issues:
1. Check the Troubleshooting section above
2. Review the notebook comments
3. Check TensorFlow documentation: https://www.tensorflow.org/

---

**Last Updated**: 2026-05-15  
**Author**: AgriGuard: InsectVision Development Team  
**License**: MIT
