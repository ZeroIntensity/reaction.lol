# Last Updated: 1/31/21

## Credits

### Developers

Built by [ZeroIntensity](https://github.com/ZeroIntensity) and [2331puppy](https://github.com/2231puppy)

### Images
None of the images reaction.lol uses are ours and have been posted so many times throughout the internet it would be impossible to find the original.

## How to use

### Getting from the API
To get images from the API, we recommend using the `reaction_lol.py` for python. For more on that, go to the `Using the file` section. If you don't want to use the file, you can use the `API Usage` section below.

### API Usage
**Note:** The `image ID` is the name of the file in the database (not including the `rimage_` prefix or the `.png` suffix.)

|Route|Notes|
|----|-----|
|`https://reaction.lol/image`|Gets a random image link. Returns a `json` object with `url` as the key to get the URL of the image.|
|`https://reaction.lol/all`|Gets every image stored URL in the database. Returns a `json` object with the image ID as the key.|
|`https://reaction.lol/get-{image ID}`|Gets a specified image based on its ID. Returns a `json` object with `url` as the key to get the URL of the image. If its not found, it returns `404`.|

### Using the file

**Note:** This part is for the Python `reaction_lol.py` file. 

Using the `reaction_lol.py` file is much easier than getting the request manually.


First, to get a random image, you run the `getimage()` function from the file. The function will automatically return the URL and not the `dict` object. Example:

```py
from reaction_lol import getimage # Import the function

image = getimage() # Get a random image URL

print(image) # Prints the image URL
```

To get a specified image, you must pass in the `image ID` as an argument. If the image is not found, it returns `404`. Example:

```py
from reaction_lol import getimage # Import the function

image = getimage('zIuFMUabtfenFnGfZa') # Grabs the image with the ID "zIuFMUabtfenFnGfZa"

print(image) # Prints the image URL (https://reaction.lol/images/rlimage_zIuFMUabtfenFnGfZa.png)
```

To get everything image from the API, you need to use the `getall()` function. It will return every url in a list. Example:

```py
from reaction_lol import getall # Import the function

images = getall() # Grabs the ID of all images

print(images) # Prints all of the image IDs
```