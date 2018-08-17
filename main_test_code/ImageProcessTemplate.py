import cv2
from matplotlib import pyplot as plt

if __name__ == '__main__':

    namedWindowKeyValue = 'inputImage'
    # input path
    inputFileName = '../resource/ouzel1.jpg'
    inputImage = cv2.imread(inputFileName, cv2.IMREAD_UNCHANGED)

    # TODO: someting
    # outputImage = process(inputImage)
    b,g,r = cv2.split(inputImage)
    outputImage = g

    # MARK: show & write
    # case 1: using plot
    plt.subplot(121), plt.imshow(inputImage, 'gray'), plt.title('inputImage')
    plt.subplot(122), plt.imshow(outputImage, 'gray'), plt.title('outputImage')
    plt.show()

    # case 2: for single Image
    # cv2.namedWindow(namedWindowKeyValue, cv2.WINDOW_NORMAL)
    # cv2.imshow(namedWindowKeyValue, inputImage)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

