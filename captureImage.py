import cv2

image_counter = 0
cap = cv2.VideoCapture(1)

def capture_frame(image_counter):
    ret, frame = cap.read()
    if ret:
        # Convert the frame to JPEG format
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]  # Adjust JPEG quality as needed
        result, jpeg_image = cv2.imencode('.jpg', frame, encode_param)
        if result:
            # Save the JPEG image
            image_filename = f"captured_image{image_counter}.jpg"
            with open(image_filename, 'wb') as f:
                f.write(jpeg_image)
            print("Image captured successfully.")
            image_counter += 1
        else:
            print("Error: Unable to encode frame to JPEG.")
    else:
        print("Error: Unable to capture frame.")

    return image_counter


def open_capture(image_counter):
  if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

  while True:
    ret, frame = cap.read()  # Continously read a frame
    if not ret:
      print("Error: Failed to read frame.")
      break
              #(Frame Name, Frame)
    cv2.imshow('Frame', frame)  # Display the frame
    
    key = cv2.waitKey(1)

    if key == ord('c'): # Press 'c' to capture frame
      image_counter = capture_frame(image_counter)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
      break
