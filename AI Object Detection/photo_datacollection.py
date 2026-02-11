import cv2
import os # For managing file paths

# Initialize the camera (0 for default webcam, or specify a video file)
cap = cv2.VideoCapture(0) 

# Create a directory to save images if it doesn't exist
output_folder = "captured_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

img_counter = 0
photo_rate = 20
image_offest = 0

photo_counter = 0
photo_limiter = 250

shape = "square"

while (photo_counter < photo_limiter):
    ret, frame = cap.read() # Read a frame from the camera
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Camera Feed", frame) # Display the live camera feed

    # Automate capture based on a condition (e.g., time interval, object detection)
    # For demonstration, we'll use a simple counter and save every few frames
    if img_counter % photo_rate == 0:  # Save an image every 30 frames (adjust as needed)
        # img_name = os.path.join(output_folder, f"green_{shape}_close_{image_offest + (img_counter // photo_rate)}.png")
        # img_name = os.path.join(output_folder, f"green_{shape}_far_{image_offest + (img_counter // photo_rate)}.png")

        # img_name = os.path.join(output_folder, f"yellow_{shape}_close_{image_offest + (img_counter // photo_rate)}.png")
        # img_name = os.path.join(output_folder, f"yellow_{shape}_far_{image_offest + (img_counter // photo_rate)}.png")

        # img_name = os.path.join(output_folder, f"purple_{shape}_close_{image_offest + (img_counter // photo_rate)}.png")
        img_name = os.path.join(output_folder, f"purple_{shape}_far_{image_offest + (img_counter // photo_rate)}.png")
        cv2.imwrite(img_name, frame)
        print(f"{img_name} saved!")

        photo_counter += 1

    img_counter += 1

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy windows
cap.release()
cv2.destroyAllWindows()