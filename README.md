# Python script to add and remove watermark using opencv library
### Sample image:
![image info](./sample/sample_image.png "Sample image")


## To add the watermark to an image:
```
python mark.py --image <image_path> --add --text <Text for watermark>
```
The image will be saved as `<timestamp>.png` inside `result/` folder
 which will be created automatically if doesn't exist.
 
- If `mark.py` is executed with all default arguments as `python mark.py`, resulting image will be: 
<br><br>
![image info](./result/20200826-140526.png "After watermark")

## To remove the watermark from an image:
```
python mark.py --image <image_path> --remove --text <Exact text used for applying watermark>
```

- If `mark.py` is executed with all default arguments to remove watermark as `python mark.py --image ./result/20200826-140526.png --remove`, resulting image will be: 
<br><br>
![image info](./result/20200826-141542.png "After removing watermark")

## To-do:
- Reversing watermark over-exposes the image, which needs to be fixed
- Add other features 

Sample image taken from <a href='https://vignette.wikia.nocookie.net/onepiece/images/6/6d/Monkey_D._Luffy_Anime_Post_Timeskip_Infobox.png/revision/latest/scale-to-width-down/340?cb=20200429191518'>here</a>
