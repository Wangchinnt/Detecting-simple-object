# Detecting simple object using Opencv
### Description
Here is our project for the Digital Image Processing course:
- Amazing simple object detection based on its color(in this case objects are Rubiks, Oranges, pill bottles)
- We also provide tools such as getting an object's color and picking a color in the HSV color space
### KeyPoint
#### 1. Steps involved:
i.Detect the object in the real-time.

ii.Track the object as it moves around in real time. Draw a rectangle around it.
#### 2. Assumptions:
1. There is an object in real-time.

2. The object is the largest color object in real-time.

3. We can specify the desired size of the rectangle of the object's boundary.

4. HSV color space is used to detect the object. Hence we convert the input RGB image to HSV color space.

5. The script is suitable for real-time tracking as it has a very good frame rate (>32 FPS).

6. The object can be partially occluded and our script will still successfully track the ball.

7. In addition, the tools support getting the color limit of the object.
### Contributors
- [21020042-Tạ Quang Chiến](https://github.com/Wangchinnt) (25%)
- [21021453-Hà Tùng Anh](https://github.com/HaTungAnh) (15%)
- [21021470-Đồng Văn Dương](https://github.com/Rouxxs) (15%)
- [21020187-Phạm Anh Đức](https://github.com/anhduc291203) (15%)
- [21020623-Nguyễn Đức Hải](https://github.com/DucHai972) (15%)
- [21020251-Trần Hoàng Vũ](https://github.com) (15%)
### Requirements: (with versions we tested on)
- #### python(3.11.1)
- #### opencv(4.7.0)
- #### numpy(1.24.2)
### Installation
#### To run this project, you will need to have Python and OpenCV installed on your computer. You can install OpenCV using the following command:
```sh
pip install opencv-python 
pip install numpy
```
### Usage
To use this project, simply run the following command:
```sh
python detect_object.py
```
Or if u want to use some tools that we provided, then:
```sh
python "NameOfToolsFile.py"
```
### Result

  The result is great. Some objects are successfully detected. Also if the object loses the frame, we catch it later when it comes into the frame.

https://user-images.githubusercontent.com/66167308/236725586-524fbe27-67ec-4439-8997-73dccf957479.mp4

https://user-images.githubusercontent.com/66167308/236725592-c4b30b7a-0b3e-4cdd-b057-b2ab356fc5ee.mp4

https://user-images.githubusercontent.com/66167308/236725606-9a9ef7b7-5b27-40ff-b2dc-4aa43b226fc7.mp4

### The limitations
1.There are certain objects that we can't detect because their color are quite mixed.

2.Need to update the script if want to track a object of different color

3.In order to detect the object with the color we want, we need to have a high quality input as well as get the correct range of that color in the HSV color space.

### Contact

WuangChin - https://www.facebook.com/wangchinn.t - tachien2003@gmail.com

### Acknowledgements
This project was inspired by [Tutorial on Detecting Color using OpenCV and Python](https://pysource.com/2019/02/15/detecting-colors-hsv-color-space-opencv-with-python)


