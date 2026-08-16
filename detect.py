from ultralytics import YOLO
import cv2
import os

# ==========================================
# AI TRAFFIC MANAGEMENT SYSTEM
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "yolo11n.pt")
INPUT_VIDEO = os.path.join(
    BASE_DIR,
    "input",
    "traffic_fixed.mp4"
)

OUTPUT_VIDEO = os.path.join(
    BASE_DIR,
    "output",
    "traffic_management_result.mp4"
)

# Vehicle classes in COCO dataset
VEHICLE_CLASSES = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck"
}

# ==========================================
# Load YOLO model
# ==========================================

print("Loading YOLO model...")

model = YOLO(MODEL_PATH)

print("YOLO model loaded successfully!")

# ==========================================
# Open input video
# ==========================================

cap = cv2.VideoCapture(INPUT_VIDEO)

if not cap.isOpened():
    raise Exception("Could not open input video.")

fps = cap.get(cv2.CAP_PROP_FPS)

width = int(
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
)

height = int(
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
)

total_frames = int(
    cap.get(cv2.CAP_PROP_FRAME_COUNT)
)

print("FPS:", fps)
print("Resolution:", width, "x", height)
print("Total frames:", total_frames)

# ==========================================
# Create output video
# ==========================================

fourcc = cv2.VideoWriter_fourcc(
    *"mp4v"
)

out = cv2.VideoWriter(
    OUTPUT_VIDEO,
    fourcc,
    fps,
    (width, height)
)

# ==========================================
# Traffic density function
# ==========================================

def get_density(vehicle_count):

    if vehicle_count <= 5:
        return "LOW"

    elif vehicle_count <= 12:
        return "MEDIUM"

    else:
        return "HIGH"


# ==========================================
# Process video
# ==========================================

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(
        frame,
        verbose=False
    )

    result = results[0]

    vehicle_count = 0

    # --------------------------------------
    # Count vehicles
    # --------------------------------------

    if result.boxes is not None:

        for box in result.boxes:

            class_id = int(
                box.cls[0]
            )

            if class_id in VEHICLE_CLASSES:

                vehicle_count += 1

    # --------------------------------------
    # Draw YOLO detections
    # --------------------------------------

    annotated_frame = result.plot()

    # --------------------------------------
    # Calculate traffic density
    # --------------------------------------

    density = get_density(
        vehicle_count
    )

    # --------------------------------------
    # Display traffic information
    # --------------------------------------

    cv2.rectangle(
        annotated_frame,
        (10, 10),
        (350, 100),
        (0, 0, 0),
        -1
    )

    cv2.putText(
        annotated_frame,
        "AI TRAFFIC MANAGEMENT",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Vehicles: {vehicle_count}",
        (20, 62),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Traffic Density: {density}",
        (20, 88),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2
    )

    # --------------------------------------
    # Save frame
    # --------------------------------------

    out.write(
        annotated_frame
    )

    frame_count += 1

    if frame_count % 100 == 0:

        print(
            f"Processed "
            f"{frame_count}/{total_frames} frames"
        )


# ==========================================
# Release resources
# ==========================================

cap.release()

out.release()

print()
print("==========================================")
print("PROCESSING COMPLETED")
print("==========================================")
print("Output:", OUTPUT_VIDEO)





