[![DOI](https://zenodo.org/badge/90018285.svg)](https://zenodo.org/badge/latestdoi/90018285)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Computing functional maps of zebrafish brain
This code processes light-sheet data in several steps:
* parsing behavior/stimulus time series into 3 regressors,
* preprocessing imaging stacks: rigid registration and correction for XY drift,
* computing functional maps by linear regression,
* saving the functional maps.

## Getting started
The code can be executed as Python Jupyter notebooks, using a personal computer or a cluster. Two downsampled datasets are provided in `raw.zip` files (350 MB each), containing behavior and imaging data.

### Prerequisites
#### Local computer
OS: Windows 7 or higher, macOS X.

[Jupyter Notebook](http://jupyter.org/install), recommended installation: Anaconda, Python 2.7 or 3.6.

Installed Thunder libraries for image processing. For installing, run the following commands in shell (or Anaconda Prompt)
```
pip install https://github.com/thunder-project/thunder/zipball/master
pip install https://github.com/thunder-project/thunder-regression/zipball/master
pip install https://github.com/thunder-project/thunder-registration/zipball/master
```

#### Computer cluster
The cluster needs to have distributed computing engine [`Spark`](https://github.com/apache/spark) running. Consult the official [Spark documentation](http://spark.apache.org/docs/latest/) for details. See example on setting [Spark on Janelia cluster](https://github.com/freeman-lab/spark-janelia).

### Installation
Clone or download this repository. Download file [`2014-08-01fish2_H2B/raw.zip`](https://github.com/optofish-paper/ZebrafishFunctionalMaps_LinearRegression/blob/master/2014-08-01fish2_H2B/raw.zip?raw=true) separately (350 MB).

Start the Jupyter Notebook environment.

Open the notebook file [FunctionalMaps_2014-08-01fish2(H2B).ipynb](FunctionalMaps_2014-08-01fish2(H2B).ipynb). Set the path to raw data downloaded and unzipped on your local computer: 
```
expDir = `C:/../ZebrafishFunctionalMaps_LinearRegression-master/2014-08-01fish2_H2B/`
```

### Running the notebooks
#### On local computer
Execute the code cells in `FunctionalMaps_2014-08-01fish2(H2B).ipynb`, starting from top. By default, the code runs on your local computer.

If all blocks run successfully, functional maps of the fish brain will be saved in file `../proc/compositeRGBgamma0.5.tif` after about 15 min. The TIFF red channel contains mapping for fictive swimming, green for forward stimulus, blue for backward stimulus. The file can be opened, for example, in [Fiji](https://fiji.sc/).

#### On computer cluster
Launch the Jupyter notebook environment on **master** node running a Spark cluster. Start the `FunctionalMaps_2014-08-01fish2(H2B).ipynb` notebook and change execution to distributed mode:
```
sparkOn = True
```
Then execute the code cells in sequential order, as before. The resulting functional maps will be saved in TIFF file.

### Datasets
[2014-08-01fish2_H2B/raw.zip](https://github.com/optofish-paper/ZebrafishFunctionalMaps_LinearRegression/blob/master/2014-08-01fish2_H2B/raw.zip?raw=true) contains brain activity data from *elavl3:GCaMP6-H2B* (nuclear-localized GCaMP6f) fish during optomotor response behavior.

[2016-07-26fish1_cyto/raw.zip](https://github.com/optofish-paper/ZebrafishFunctionalMaps_LinearRegression/blob/master/2016-07-26fish1_cyto/raw.zip?raw=true) contains brain activity data from *elavl3:GCaMP6f* (GCaMP6f expressed in the cytosol of neurons).

Each set contains 100 stacks (time points), downsampled to 1.62 micron/px (x,y) and 5 micron/px (z) spatial resolution. Temporal resolution is 0.55 s/stack.

### Citation
If you use the code or data, please cite the original paper:

*Brain-wide circuit interrogation at the cellular level guided by online analysis of neuronal function.* [Vladimirov et al, Nat. Methods, 2018](http://dx.doi.org/10.1038/s41592-018-0221-x).

To cite this code specifically, please use the following DOI 

[![DOI](https://zenodo.org/badge/90018285.svg)](https://zenodo.org/badge/latestdoi/90018285)
