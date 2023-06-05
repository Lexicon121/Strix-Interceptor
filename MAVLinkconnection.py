import tkinter as tk
from pymavlink import mavutil

# Set the connection parameters
# Replace with the IP address of your Pixhawk module
connection_string = 'udpout:192.168.1.2:14550'
baudrate = 57600

# Create a MAVLink connection
mavlink_connection = mavutil.mavlink_connection(
    connection_string, baud=baudrate)

# Wait for the heartbeat message to ensure that the connection is established
mavlink_connection.wait_heartbeat()

# Create the GUI window
root = tk.Tk()
root.title('Strix Drone Control')

# Create a button to arm the drone
arm_button = tk.Button(root, text='Arm Drone',
                       command=lambda: mavlink_connection.arducopter_arm())
arm_button.pack()

# Create a button to disarm the drone
disarm_button = tk.Button(root, text='Disarm Drone',
                          command=lambda: mavlink_connection.arducopter_disarm())
disarm_button.pack()

# Create a button to take off
takeoff_button = tk.Button(root, text='Take Off', command=lambda: mavlink_connection.mav.command_long_send(
    mavlink_connection.target_system, mavlink_connection.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 10))
takeoff_button.pack()

# Create a button to land
land_button = tk.Button(root, text='Land', command=lambda: mavlink_connection.mav.command_long_send(
    mavlink_connection.target_system, mavlink_connection.target_component,
    mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, 0))
land_button.pack()

# Run the GUI main loop
root.mainloop()

# Close the MAVLink connection
mavlink_connection.close()
