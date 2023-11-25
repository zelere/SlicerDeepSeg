# Comprehensive Brain Tumor Classification System with Slicer and Machine Learning 

## Purpose 
The project aims to support the segmentation and classification process of brain tumors.
This Slicer extension is capable of calculating radiomics features based on automatically or manually segmented MRI scans, and classifying the grade of the brain tumor. For automated segmentation nnU-net is used, which performed among the best solutions in the BraTS2021 competition.  

## Installation
First, download the 3D Slicer from here. Select the version that corresponds to your operating system.

1. Download and unzip this repository.
2. Slicer menu: Edit > Application Settings > Developer
3. Modules > Developer Tools > Extension Wizard
4. Select Extension (choose the folder where you unzipped the repo)

Steps 2-4 are visualized on [Developing Slicer Extensions](https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g420896289_061) slides 8 to 10.

Please adjust the file paths in Slicer-DeepSeg/DeepSeg/DeepSeg.py on line 631 and 632 to match the location on your computer. This feature is still under development.

```
## replace these links based on your directory location
self.radiomicsParamsPath=(r"C:\Users\User\Desktop\Slicer-DeepSeg-main (1)\Slicer-DeepSeg-main\Slicer-DeepSeg\DeepSeg\Settings\Params.yml" )
self.estimatorPath=(r"C:\Users\User\Desktop\Slicer-DeepSeg-main (1)\Slicer-DeepSeg-main\Slicer-DeepSeg\DeepSeg\TumorClassification\b_e_RF_Selec_240.joblib")
```


## Use cases 
### Classification using automated segmentation
- set input FLAIR, T1, T1ce and T2 volumes
- check the `Automated segmentation` checkbox
- select Output `Tumor segmentation` and `Tumor Volume`, where the segmentation results will be stored
- Press  the `Classification` button

### Classification using manual existing segmentation
- set input FLAIR, T1, T1ce and T2 volumes
- select input `Segmentation` ( note that the segmentation layers have to be named Segment_1, Segment_2 and Segment_4 where the number corresponds to the tumor region label (1: non-enhancing tumor core, 2: peritumoral edema, 4: GD-enhancing tumor) )
- uncheck `Automated segmentation` checkbox
- Press  the `Classification` button

### Use adjusted segmentation for classification
- set input FLAIR, T1, T1ce and T2 volumes
- edit the segmentation in the `SegmentEditor` or by pressing the `Edit Segmentation` button
-  note that the segmentation layers have to be named Segment_1, Segment_2 and Segment_4 where the number corresponds to the tumor region label (1: non-enhancing tumor core, 2: peritumoral edema, 4: GD-enhancing tumor)
- uncheck `Automated segmentation` checkbox
- Press  the `Classification` button
### Automated segmentation
- set input FLAIR, T1, T1ce and T2 volumes
- select Output `Tumor segmentation` and `Tumor Volume`, where the segmentation results will be stored
- Press  the `Segmentation` button
 

![GUI]( https://github.com/zelere/SlicerDeepSeg/blob/master/3D%20Slicer%205.2.2%2024_11_2023%2001_34_20.png )
## Acknowledgements
The extension is built on top of the existing [Slicer-DeepSeg extension](https://github.com/razeineldin/Slicer-DeepSeg) 
Zeineldin, Ramy A., Weimann, Pauline, Karar, Mohamed E., Mathis-Ullrich, Franziska and Burgert, Oliver. "Slicer-DeepSeg: Open-Source Deep Learning Toolkit for Brain Tumour Segmentation" Current Directions in Biomedical Engineering, vol. 7, no. 1, 2021, pp. 30-34. https://doi.org/10.1515/cdbme-2021-1007
