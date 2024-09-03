from sort_functions import *
from search_functions import *
from PixelFunctions import *

def main():
    IMG_NAME = 'monkey'

    with Image.open(IMG_NAME + '.jpg') as im:
        pixels, yiq_pixels = storePixels(im)
        print("Stored")
        mergeSort(yiq_pixels)
        pixels_to_image(im, yiq_pixels)
        print("Sorted")

        target = (183/255, 198/255, 144/255)
        yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])
        subi = binary_search_sub([r[0][0] for r in yiq_pixels],
                                 0, len(yiq_pixels) - 1, yiq_target[0])
        grayscale(im,pixels)
        pixels_to_points(im, yiq_pixels[subi:])
    
    
    while True:
        user = input('Type Q to save image\nType R to reverse what is highlighted\nType T to adjust tolerance\nType C to change targeted color')
        if user == "Q":
            im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')
            break
            
        elif user == "R":
            grayscale(im, pixels)
            pixels_to_points(im, yiq_pixels[:subi])
            break

        elif user == "T":
            userTol = int(input("On a scale of one to ten, how sensitive would you like the tolerance?\n(1 being most sensitive)"))
            tol = int(len(yiq_pixels)/userTol)
            pixels_to_points(im, yiq_pixels[(subi-tol):])
            break

        elif user == "C":
            userTargetR = int(input("What Red value woulld you like to target? (0-255)"))
            userTargetG = int(input("What Green value woulld you like to target? (0-255)"))
            userTargetB = int(input("What Blue value woulld you like to target? (0-255)"))
            userTarget = (userTargetR/255, userTargetG/255, userTargetB/255)

            with Image.open(IMG_NAME + '.jpg') as uim:
                pixels, yiq_userPixels = storePixels(uim)
                print("Stored")
                mergeSort(yiq_userPixels)
                pixels_to_image(uim, yiq_userPixels)

                yiq_userTarget = colorsys.rgb_to_yiq(userTarget[0], userTarget[1], userTarget[2])
                subi = binary_search_sub([r[0][0] for r in yiq_userPixels],
                                 0, len(yiq_userPixels) - 1, yiq_userTarget[0])
                grayscale(uim,pixels)
                pixels_to_points(uim, yiq_userPixels[subi:])
            break

# end of main():
 

if __name__ == '__main__':
    main()