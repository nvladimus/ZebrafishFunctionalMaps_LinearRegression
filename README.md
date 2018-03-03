# Computing functional maps of zebrafish brain
This code processes light-sheet data in several steps:
* parsing behavior/stimulus time series into 3 regressors,
* preprocessing imaging stacks: median filtering, rigid registration and correction for XY drift,
* computing functional maps by linear regression,
* saving the functional maps.

## Getting started
The code can be executed as Python Jupyter notebooks, using a personal computer or a cluster. Two downsampled datasets are provided in `raw.zip` files, 350 MB each, containing behavior and imaging data acquired with [Zebrascope](https://www.nature.com/nmeth/journal/v11/n9/full/nmeth.3040.html).

### Prerequisites
#### Local computer
OS: Windows 7 or higher, or macOS X.

[Jupyter Notebook](http://jupyter.org/install) (tested with Anaconda).

Installed Thunder libraries for image processing. For installing, run the following commands in shell (or Anaconda Prompt)
```
pip install https://github.com/thunder-project/thunder/zipball/master
pip install https://github.com/thunder-project/thunder-regression/zipball/master
pip install https://github.com/thunder-project/thunder-registration/zipball/master
```
(optional, for test before cluster deployment): [Spark](http://spark.apache.org/docs/latest/)

#### Computer cluster
The cluster needs to have distributed computing engine [`Spark`](https://github.com/apache/spark) running. Consult the official [Spark documentation](http://spark.apache.org/docs/latest/) for details. 

### Installing 
Clone or download this repository. Download file [`2014-08-01fish2_H2B/raw.zip`](https://github.com/optofish-paper/ZebrafishFunctionalMaps_LinearRegression/blob/master/2014-08-01fish2_H2B/raw.zip?raw=true) separately (350 MB).

Start the Jupyter Notebook environment.

Open the `FunctionalMaps_2014-08-01fish2(H2B).ipynb`. Change the raw data path to your folder 
```
expDir = `C:/../ZebrafishFunctionalMaps_LinearRegression-master/2014-08-01fish2_H2B/`
```

### Running the test
#### On local computer
Execute the code cells in `FunctionalMaps_2014-08-01fish2(H2B).ipynb`, starting from top. By default, the code runs on your local computer.

If all blocks run successfully, functional maps of the fish brain will be saved in file `compositeRGBgamma0.5.tif` after about 15 min. The TIFF red channel contains mapping for fictive swimming, green for forward stimulus, blue for backward stimulus. The file can be opened, for example, in [Fiji](https://fiji.sc/).

#### On computer cluster
Launch the Jupyter notebook environment on **master** node running a Spark cluster. Start the `FunctionalMaps_2014-08-01fish2(H2B).ipynb` notebook and change execution to distributed mode:
```
sparkOn = True
```
Then execute the code cells in sequential order, as before. The resulting functional maps will be saved in TIFF file.

### Datasets
Dataset `2014-08-01fish2_H2B/raw.zip` contains brain activity data from *elavl3:GCaMP6-H2B* (nuclear-localized GCaMP6f) fish during optomotor response behavior.
Dataset `2016-07-26fish1_cyto/raw.zip` contains analogous data from *elavl3:GCaMP6f* (GCaMP6f expressed in cytosol of neurons).

Each set contains 100 stacks (time points), downsampled to 1.62 micron/px (x,y) and 5 micron/px (z) spatial resolution. Temporal resolution is 0.55 s/stack.
