import cv2
from djitellopy import Tello
import time
from ultralytics import YOLO

flight_boolean = False
run_boolean = True

green = (0, 255, 0)

green_circle_flag = 1
green_triangle_flag = 1
green_square_flag = 1

green_circle_threshold = 0.90
green_triangle_threshold = 0.90
green_square_threshold = 0.90

yellow = (10, 170, 190)

yellow_circle_flag = 1
yellow_triangle_flag = 1
yellow_square_flag = 1

yellow_circle_threshold = 0.90
yellow_triangle_threshold = 0.90
yellow_square_threshold = 0.90

purple = (90, 60, 120)

purple_circle_flag = 1
purple_triangle_flag = 1
purple_square_flag = 1

purple_circle_threshold = 0.90
purple_triangle_threshold = 0.90
purple_square_threshold = 0.90

model_path = "C:\\Users\\conno\\Python Files\\Python Project\\runs\\detect\\train4\\weights\\best.pt"

model = YOLO(model_path)

def detect_shapes(frame_read):
    global run_boolean

    global green_circle_flag
    global green_triangle_flag
    global green_square_flag

    global yellow_circle_flag
    global yellow_triangle_flag
    global yellow_square_flag

    global purple_circle_flag
    global purple_triangle_flag
    global purple_square_flag

    frame = frame_read.frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)[0]

    # print(f"Results are: {results}")

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        detection_width = abs(x1 - x2)
        detection_height = abs(y1 - y2)

        print(f"Result is: {result}")

        if ((green_circle_flag == 1) and (class_id == 0)):
            if (score > green_circle_threshold):
                # print(f"\n\n\nWe saw a GREEN circle                                                 GREEN CIRCLE FLAG\n\n\n")
                print(f"\n\n\nGreen circle found at width of: {detection_width} and height of: {detection_height}\n\n\n")
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), green, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, green, 3, cv2.LINE_AA)

                if (flight_boolean == 1):
                    green_circle_flag = 0

                drone_behavior(green=1)

        elif ((green_triangle_flag == 1) and (class_id == 1)):
            if (score > green_triangle_threshold):
                # print(f"\n\n\nWe saw a GREEN triangle                                                 GREEN TRIANGLE FLAG\n\n\n")
                print(f"\n\n\nGreen triangle found at width of: {detection_width} and height of: {detection_height}\n\n\n")
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), green, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, green, 3, cv2.LINE_AA)

        elif ((green_square_flag == 1) and (class_id == 2)):
            if (score > green_square_threshold):
                # print(f"\n\n\nWe saw a GREEN square                                                 GREEN SQUARE FLAG\n\n\n")
                print(f"\n\n\nGreen square found at width of: {detection_width} and height of: {detection_height}\n\n\n")
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), green, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, green, 3, cv2.LINE_AA)

        elif ((yellow_circle_flag == 1) and (class_id == 3)):
            if (score > yellow_circle_threshold):
                # print(f"\n\n\nWe saw a YELLOW circle                                                 YELLOW CIRCLE FLAG\n\n\n")
                print(f"\n\n\nYellow circle found at width of: {detection_width} and height of: {detection_height}\n\n\n")
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), yellow, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, yellow, 3, cv2.LINE_AA)

                if (flight_boolean == 1):
                    yellow_circle_flag = 0

                drone_behavior(yellow=1)

        elif ((yellow_triangle_flag == 1) and (class_id == 4)):
            if (score > yellow_triangle_threshold):
                # print(f"\n\n\nWe saw a YELLOW triangle                                                 YELLOW TRIANGLE FLAG\n\n\n")
                print(f"\n\n\nYellow triangle found at width of: {detection_width} and height of: {detection_height}\n\n\n")
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), yellow, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, yellow, 3, cv2.LINE_AA)
            
        elif ((yellow_square_flag == 1) and (class_id == 5)):
            if (score > yellow_square_threshold):
                # print(f"\n\n\nWe saw a YELLOW square                                                 YELLOW SQUARE FLAG\n\n\n")
                print(f"\n\n\nYellow square found at width of: {detection_width} and height of: {detection_height}\n\n\n")
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), yellow, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, yellow, 3, cv2.LINE_AA)

        elif ((purple_circle_flag == 1) and (class_id == 6)):
            if (score > purple_circle_threshold):
                # print(f"\n\n\nWe saw a PURPLE circle                                                 PURPLE CIRCLE FLAG\n\n\n")
                print(f"\n\n\nPurple circle found at width of: {detection_width} and height of: {detection_height}\n\n\n")
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), purple, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, purple, 3, cv2.LINE_AA)

                if (flight_boolean == 1):
                    purple_circle_flag = 0

                drone_behavior(purple=1)

        elif ((purple_triangle_flag == 1) and (class_id == 7)):
            if (score > purple_triangle_threshold):
                # print(f"\n\n\nWe saw a PURPLE triangle                                                 PURPLE TRIANGLE FLAG\n\n\n")
                print(f"\n\n\nPurple triangle found at width of: {detection_width} and height of: {detection_height}\n\n\n")
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), purple, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, purple, 3, cv2.LINE_AA)
            
        elif ((purple_square_flag == 1) and (class_id == 8)):
            if (score > purple_square_threshold):
                # print(f"\n\n\nWe saw a PURPLE square                                                 PURPLE SQUARE FLAG\n\n\n")
                print(f"\n\n\nPurple square found at width of: {detection_width} and height of: {detection_height}\n\n\n")
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), purple, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, purple, 3, cv2.LINE_AA)

        elif ((green_circle_flag == 0) and (yellow_circle_flag == 0) and (purple_circle_flag == 0)):

            print("\n\n\nAll behaviors are done!\n\n\n")
            tello_object.move_up(20)
            tello_object.flip_back()

            run_boolean = False
        else:
            print("\n\n\nThere is an error within the color flagging section\n\n\n")
    
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        run_boolean = False

# act on cirlce color behavior
def drone_behavior(green = 0, yellow = 0, purple = 0):
    movement_amount = 50

    if green == 1:
        print(f"\n\n\nWe acted on a GREEN circle                                                 GREEN CIRCLE BEHAVIOR\n\n\n")

        if flight_boolean == True:
            tello_object.move_up(movement_amount)
            tello_object.move_down(movement_amount * 2)
            tello_object.move_up(movement_amount)

    elif yellow == 1:
        print(f"\n\n\nWe acted on a YELLOW circle                                                YELLOW CIRCLE BEHAVIOR\n\n\n")

        if flight_boolean == True:
            tello_object.move_forward(movement_amount)
            tello_object.move_back(movement_amount * 2)
            tello_object.move_forward(movement_amount)

    elif purple == 1:
        print(f"\n\n\nWe acted on a PURPLE circle                                                PURPLE CIRCLE BEHAVIOR\n\n\n")
        
        if flight_boolean == True:
            tello_object.move_right(movement_amount)
            tello_object.move_left(movement_amount * 2)
            tello_object.move_right(movement_amount)

    else:
        print("There is an error within the drone behavior function")

def main():
    # Connecting to the drone and initializing our Tello object
    global tello_object
    tello_object = Tello()
    tello_object.connect()

    tello_charge = tello_object.get_battery()
    print(f"Current battery is {tello_charge}")

    tello_object.streamon()
    frame_read_value = tello_object.get_frame_read()

    if flight_boolean == True:
        tello_object.takeoff()
        time.sleep(2)

        tello_object.move_up(80)

    while run_boolean == True:
        detect_shapes(frame_read_value)

    cv2.destroyAllWindows()
    tello_object.end()

main()