# Dehazing-Improved-Algorithm

> Research repo for: **Lower Bound on Transmission + Adaptive BF-Net (assumed improv.)**  
> Based on: *Lower Bound on Transmission Using Non-Linear Bounding Function in Single Image Dehazing* (Raikwar & Tapaswi, IEEE TIP 2020).


---


## Overview
This repo contains:
- the **base algorithm** implementation reproducing the lower-bound BF dehazing method from the paper,  
- an **assumed (basic) improvement** called **Adaptive BF-Net (ABF-Net)** — a lightweight per-pixel BF predictor + adaptive ζ estimator that refines transmission estimates and preserves color/edges,  
- notebooks, scripts, and example results (placeholders) to be replaced by final experiments.

**Why this improvement (assumption)?**  
The original method computes a non-linear bounding function δ(x,y) modeled as `δ ≈ 1 / minIh^α` with α ≈ 0.5 and uses a global ζ control. We assume a learnable per-pixel δ predictor and a small region-wise ζ predictor will adapt better to local scene content (sky vs non-sky) and produce tighter lower bounds with little runtime cost. 

---

## Repo structure

| Path | Purpose |
|------|---------|
| `README.md` | this file |
| `LICENSE` | MIT License |
| `requirements.txt` | pip dependencies |
| `data/` | sample images (small), evaluation sets (links or placeholder) |
| `src/` | production code |
| `src/base_dehaze.py` | re-implementation of paper method (Eq.3–7, smoothing) |
| `src/abf_net.py` | assumed improvement code (ABF-Net model + inference wrapper) |
| `src/utils.py` | helpers (I/O, metrics, visualization) |
| `notebooks/` | quick experiments & qualitative comparisons |
| `models/` | pretrained weights (placeholders) |
| `results/` | placeholder images, CSV metrics, plots |
| `docs/` | short report, slides, and paper pdf |
| `.gitignore` | ignore large data, checkpoints, __pycache__ |

---

## Quick start — install & run

```bash
# 1) clone
git clone https://github.com/<your-username>/Dehazing-Improved-Algorithm.git
cd Dehazing-Improved-Algorithm

# 2) environment
python -m venv venv
source venv/bin/activate       # mac/linux
# .\venv\Scripts\activate      # windows

pip install -r requirements.txt

# 3) run base method (example)
python src/base_dehaze.py --input data/sample_images/hazy1.jpg --output results/base/hazy1_dehazed.png

# 4) run improved method (assumed)
python src/abf_net.py --input data/sample_images/hazy1.jpg --output results/improved/hazy1_dehazed.png --weights models/abf_net.pth

# 5) evaluate (placeholders)
python src/evaluate.py --pred results/improved/ --gt data/gt_images/ --metrics results/evaluation_improved.csv
