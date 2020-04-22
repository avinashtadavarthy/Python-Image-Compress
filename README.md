# Python-Image-Compress
A command line tool to resize and compress a folder full of JPG images

## What does it do?
- The tool can scan through a folder full of JPG/JPEG images and generate compressed images for each of them. In case the image has already been compressed then it would only resize it to an optimal size.
- It uses openCV to compress and resize images.

## How to use it?
### Step 1
Install openCV by running the following on your command line
```
sudo apt update
sudo apt install python3-opencv
```
Test if the installation is successful by running
```
python3 -c "import cv2; print(cv2.__version__)"
```
It should return an output mentioning the version number of openCV being used on the system.

### Step 2
- Clone the repository onto your local machine.
- Navigate to a folder where you would like to compress JPG/JPEG images. 
- Run the 'compressimages.py' file in that directory.
```
python3 <path to compressimages.py>
```

## Example
- To test the program, once the repository has been cloned, execute the following from the ```/data``` directory
```
python3 ../compressimages.py
```
- This would iterate through the files in the ```/data``` folder and generate the compressed images in a subfolder called ```/compressed```.
- The file names of all compressed images would be in the format ```<original_file_name>-min.jpg```.

## Note
It would preferable to keep only the image files in the chosen directory and nothing else.
This project is still under development.
