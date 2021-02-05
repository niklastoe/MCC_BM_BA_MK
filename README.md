# The Matthews correlation coefficient (MCC) is more reliable than balanced accuracy, bookmaker informedness, and markedness in two-class confusion matrix evaluation

This repository contains the necessary jupyter notebooks to recreate the figures from our open access publication

Davide Chicco, Niklas Tötsch and Giuseppe Jurman. 
["The Matthews correlation coefficient (MCC) is more reliable than balanced accuracy, bookmaker informedness, and markedness in two-class confusion matrix evaluation"](https://doi.org/10.1186/s13040-021-00244-z). 
BioData Mining 14, 13 (2021)

from scratch.
Please refer to the article for an in-depth discussion of the project.

# Repository content

* `MCC_BM_BA_MK_samples.ipynb` samples millions of confusion matrices and plots the corresponding metric values (Figure 1)
* `high_multicategory_metrics.ipynb` show how positive predictive value (also known as precision) and negative predictive value depend on the prevalence of the data set (Figure 3)
* `BM_measures_randomness_MCC_and_MK_donot.ipynb` simulates classifiers with known degrees of information/randomness and shows the corresponding metric values for them (Figure 4)

# Instructions

Copy the entire repository. 
You can now work with the jupyter notebooks in the usual way.
If you experience any problems with missing packages/dependencies, please create a new conda environment based on the provided file

`conda env create --file=environment.yaml`

# Contact

If you have questions or comments, please contact [niklas(dot)toetsch(at)uni-due(dot)de](mailto:niklas.toetsch@uni-due.de) or create an [issue](https://github.com/niklastoe/MCC_BM_BA_MK/issues).

# Citation


```
@article{Chicco2021,
author = {Chicco, Davide and Tötsch, Niklas and Jurman, Giuseppe},
title = {The Matthews correlation coefficient (MCC) is more reliable than balanced accuracy, bookmaker informedness, and markedness in two-class confusion matrix evaluation},
journal = {BioData Mining},
volume = {14},
page = {13},
issue = {1},
year = {2021},
doi = {10.1186/s13040-021-00244-z},
URL = {https://doi.org/10.1186/s13040-021-00244-z},
eprint = {https://doi.org/10.1186/s13040-021-00244-z}
}
```
