# Dimensionality Reduction & Unsupervised Clustering

## Overview
This project demonstrates dimensionality reduction with Principal Component Analysis (PCA) and unsupervised clustering with K-Means, DBSCAN, and Agglomerative (hierarchical) clustering.

The notebook uses the ten numerical features from scikit-learn's Diabetes dataset. The dataset's target variable is intentionally excluded from PCA and clustering, keeping the workflow unsupervised.

## What the notebook includes
- Standardization of numerical features
- PCA scree plot and cumulative explained-variance plot
- Component counts for 80% and 90% cumulative variance
- K-Means Elbow Method and silhouette-score analysis
- K-Means cluster visualization in a 2D PCA projection
- DBSCAN parameter comparison, cluster counts, and noise detection
- Agglomerative clustering and 2D PCA visualization
- Side-by-side comparison of clustering methods
- Interpretation guidance and limitations

## Requirements
Python 3.9+ and the following packages:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

## How to run
1. Download `dimensionality_reduction_unsupervised_clustering.ipynb`.
2. Open a terminal in the folder where it is saved.
3. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

4. Open the notebook and choose **Kernel → Restart Kernel and Run All Cells** (wording may vary).

The notebook can also be run in Visual Studio Code with the Jupyter extension.

## Project structure

```text
.
├── README.md
└── dimensionality_reduction_unsupervised_clustering.ipynb
```

## Important interpretation notes
- PCA is used to transform features and visualize clusters; the cluster algorithms are fit on all standardized features, not just the first two PCs.
- Two-dimensional plots are projections and may hide structure present in the original feature space.
- Silhouette scores should be considered alongside cluster sizes, parameter sensitivity, and domain context.
- DBSCAN results depend on `eps` and `min_samples`; observations labeled `-1` are treated as noise.
- Clusters found by an algorithm are exploratory groupings and are not automatically meaningful or causal.

## Submission
Upload the notebook (and this README if required) to a public GitHub repository or another platform that supports public notebook access. Test the public URL in a private/incognito browser window before submitting it.

## Author
Add your name, course, institution, and submission date if required.
