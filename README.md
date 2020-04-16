# Comparison of Matthews correlation coefficient, bookmaker's informedness, balanced accuracy and markedness

This repository contains the necessary jupyter notebooks to recreate the figures from our manuscrpt from scratch.

* `MCC_BM_BA_MK_samples.ipynb` samples millions of confusion matrices and plots the corresponding metric values 
* `BM_measures_randomness_MCC_and_MK_donot.ipynb` simulates classifiers with known degrees of information/randomness and shows the corresponding metric values for them

# Instructions

Copy the entire repository. 
You can now work with the jupyter notebooks in the usual way.
If you experience any problems with missing packages/dependencies, please create a new conda environment based on the provided file

`conda env create --file=environment.yaml`

# Contact

If you have questions or comments, please contact [niklas(dot)toetsch(at)uni-due(dot)de](mailto:niklas.toetsch@uni-due.de) or create an [issue](https://github.com/niklastoe/MCC_BM_BA_MK/issues).
