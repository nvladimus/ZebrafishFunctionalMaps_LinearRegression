# Computing functional maps in zebrafish brain
Workflow:
* Parsing of the behavior/stimulus data into 3 regressors (forward, backward motion of stimulus, and fictive swimming).
* Filtering, rigid registration and correction for XY drift in the imaging data.
* Computing voxel-wise regression of the imaging data with the behavior/stimulus regressors.
* Saving the functional maps of zebrafish brain in 3-colored TIFF files for visual inspection.

Small downsampled datasets are provided in two `raw.zip` files, 350 MB each, 
containing behavior and imaging data acquired with (Zebrascope)[https://www.nature.com/nmeth/journal/v11/n9/full/nmeth.3040.html]. 
The imaging data contains 100 stacks (time points), downsampled to 1.62 micron/px (x,y) and 5 micron/px (z) spatial resolution. Temporal resolution is 0.55 s (time per stack).

Dataset `2014-08-01fish2_H2B/raw.zip` contains brain activity data from *elavl3:GCaMP6-H2B* (nuclear-localized GCaMP6) fish during optomotor response behavior.

Dataset `2016-07-26fish1_cyto/raw.zip` contains analogous data from *elavl3:GCaMP6f* (GCaMP6 expressed in cytosol of neurons).

## Installation
1. Install Python distribution, for example from (Anaconda Python distribution)[https://docs.continuum.io/anaconda/install]. 
2. Instal Thunder libraries required from image processing, by running the following commands in shell (or Anaconda Prompt)
```
pip install https://github.com/thunder-project/thunder/zipball/master
pip install https://github.com/thunder-project/thunder-regression/zipball/master
pip install https://github.com/thunder-project/thunder-registration/zipball/master
```
3. Unpack `2014-08-01fish2_H2B/raw.zip` and `2016-07-26fish1_cyto/raw.zip` files.
4. Launch the IPython notebook environment (Jupyter Notebook).
5. Launch the `FunctionalMaps_2014-08-01fish2(H2B)_downsampled.ipynb`. Change the `expDir` variable to your local data folder. 
6. The code can be executed in local mode (on a single computer), or in distributed mode (in a cluster with (spark)[https://github.com/apache/spark] computing engine installed). 
Set the variable `sparkOn` accordingly.
7. After executing all IPython blocks, functional maps of the fish brain will be saved in file `compositeRGBgamma0.5.tif`, 
red channel for fictive swimming, green for forward stimulus, blue for backward stimulus.

