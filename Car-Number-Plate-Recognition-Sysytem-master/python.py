import cv2
import numpy as np

# Read the image (adjust the path if necessary)
image = cv2.imread("Data/img.jpg")  # Modify the path if the image is in a different location

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not load image. Please check the file path.")
else:
    # Resize the image using OpenCV's resize function
    image = cv2.resize(image, (500, int(image.shape[0] * (500 / image.shape[1]))))

    # Convert to grayscale and apply a bilateral filter
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # Detect edges
    edge = cv2.Canny(gray, 170, 200)

    # Find contours
    cnts, _ = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image1 = image.copy()
    cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)

    # Sort contours based on area
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
    NumberPlateCount = None
    image2 = image.copy()
    cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)

    # Loop over contours to find the number plate
    for i in cnts:
        perimeter = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)
        if len(approx) == 4:
            NumberPlateCount = approx
            x, y, w, h = cv2.boundingRect(i)
            crp_img = image[y:y+h, x:x+w]
            
            # Save the cropped number plate image with a valid extension
            cv2.imwrite('number_plate.png', crp_img)
            print(f"Number plate detected and cropped. Saved as 'number_plate.png'")
            break

    # Draw contours on the original image
    cv2.drawContours(image, [NumberPlateCount], -1, (0, 255, 0), 3)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Number Plate", crp_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
