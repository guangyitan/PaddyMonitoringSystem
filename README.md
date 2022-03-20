# Application of Deep Learning Technique in Paddy Growth Classification
This repository contains 2 main parts.
1. Paddy Monitoring System
2. Paddy Growth CLassification Deep Learning Model

## Dataset
[Annotated Dataset Link](https://drive.google.com/drive/folders/179R-TmXyWHYqAnzQoYHvlBOA2y7-yRmh?usp=sharing)

[Raw Dataset Link](https://drive.google.com/drive/folders/1lCyH_PZ2LKDOxcen_Wc39hY-2W_aDgG_?usp=sharing)

There are 2 folders in the Google Drive 

1. **annotated_dataset**: filtered images with json annotations 
2. **raw_dataset**: contains all paddy images collected.

All paddy images were collected from the paddy field at Tanjung Keling, Melaka, Malaysia between 26th April 2021 and 5th November 2021.

# Problem Statement of this project
The process of classifying paddy growth is important for farmers to make harvesting decisions. However, existing paddy growth classification system is performed, after harvesting is done which is used to confirm maturity and immaturity of the paddy yield at the warehouse.  

Furthermore, such system often relies on satellite or aerial imaging. 
The main focus of this project is to develop a paddy growth classification system using deep learning. The model developed will then be implemented in a monitoring system to assist farmers in monitoring large area of paddy field with their growth, before harvesting is done.

# Screenshot of the System UI
### System User Interface (Main View)
![image](https://user-images.githubusercontent.com/83216707/159158252-fb6d3ec3-f2e4-4264-a298-c2f6ab30dbff.png)

### System User Interface (Add New Paddy Area)
![image](https://user-images.githubusercontent.com/83216707/159158303-93b8d341-cfe5-41af-b185-56cecf22003f.png)

### System User Interface (Paddy Area Details)
![image](https://user-images.githubusercontent.com/83216707/159158346-021b3991-40bd-49c2-94ac-d62eff44d6ca.png)

# Model Performance
### Model trained using dataset 1
![image](https://user-images.githubusercontent.com/83216707/159159198-74655759-97ff-4ae9-a187-8d726e303dfd.png)

### Model trained using dataset 2
![image](https://user-images.githubusercontent.com/83216707/159159228-b057dff0-b5b8-4d4e-b8d3-57a39684764d.png)

### Comparison of small and large dataset (4 image per GPU)
![image](https://user-images.githubusercontent.com/83216707/159159250-d6d26dbe-f87e-4402-9352-44b5e76165f8.png)

### Model performance with different IOU
![image](https://user-images.githubusercontent.com/83216707/159159285-b259545d-515e-4ce4-a409-a36f74f0fae6.png)

