#---------------------------------------------------
#--------------- PROGRAM START ---------------------
from robodk.robolink import * # API to communicate with RoboDK
from robodk.robomath import * # basic matrix operations
from robodk.robodialogs import *
from robodk.robofileio import *

RDK = Robolink()

# Generate the points curve path
#POINTS = MakePoints(P_START, P_END, NUM_POINTS)

# Ask the user to pick a file

# Input file name
#input_csv = getFileName(path_file) + ".csv"
input_csv = "C:\\Users\\nurbi\\Desktop\\abcPoint.csv"

# Output list to store the transformed data
output_data = []

# Read data from the input CSV file
with open(input_csv, 'r') as file:
    lines = file.readlines()

# Remove the header if it exists
header = lines.pop(0) if lines and ',' in lines[0] else None

# Process each line
output_data.append([500, float(lines[0].strip().split(',')[0])* -0.353 +600,
                    float(lines[0].strip().split(',')[1])* -0.353 +700])
for line in lines:
    if "#" in line:
        output_data.append([600, output_data[-1][1], output_data[-1][2]])
        continue
    
    # Assuming X is the first column and Y is the second column
    x, y = map(float, line.strip().split(','))
    
    # Convert X and Y to mm (multiply by 25.4)
    x_mm = -x * 0.353 +500
    y_mm = -y * 0.353 +700

    # Append a new row to the output data list
    output_data.append([600, x_mm, y_mm])
    
POINTS = output_data

# Initialize the RoboDK API
RDK = Robolink()

# turn off auto rendering (faster)
RDK.Render(False)

# Promt the user to select a robot (if only one robot is available
# it will select that robot automatically)
robot = RDK.ItemUserPick('Select a robot', ITEM_TYPE_ROBOT)

# Turn rendering ON before starting the simulation
RDK.Render(True)

# Abort if the user hits Cancel
if not robot.Valid():
    quit()

# Retrieve the robot reference frame
reference = robot.Parent()

# Use the robot base frame as the active reference
robot.setPoseFrame(reference)

# get the current orientation of the robot (with respect to the active
# reference frame and tool frame)
pose_ref = robot.Pose()
print(Pose_2_TxyzRxyz(pose_ref))

# a pose can also be defined as xyzwpr / xyzABC
#pose_ref = TxyzRxyz_2_Pose([100,200,300,0,0,pi])
#-------------------------------------------------------------
# Option 1: Move the robot using the Python script
# We can automatically force the "Create robot program" action usinga RUNMODE state
# RDK.setRunMode(RUNMODE_MAKE_ROBOTPROG)
# Iterate through all the points
for i in range(len(output_data)):
    # update the reference target with the desired XYZ coordinates
    pose_i = pose_ref
    pose_i.setPos(POINTS[i])
    # Move the robot to that target:
    robot.MoveJ(pose_i)
# Done, stop program execution
