from djitellopy import Tello
import time

drone = Tello()

try:
    drone.connect()
    print(f"Battery: {drone.get_battery()}%")

    drone.enable_mission_pads()
    drone.set_mission_pad_detection_direction(1)
   
    drone.takeoff()
    print("take off")
    
    drone.move_up(100)
    print("drone move up 100")
  
    while True:
        pad_id = drone.get_mission_pad_id()
        if pad_id == 1:  
            print("Mission Pad 2 detected!")
            drone.go_xyz_speed_mid(x=0, y=0, z=70, speed=10, mid=1)
            time.sleep(3)
            print("x position 1 70:", drone.get_mission_pad_distance_x())
            print("x position 1 70:", drone.get_mission_pad_distance_y())
            print("x position 1 70:", drone.get_mission_pad_distance_z())
            time.sleep(3)
           
    print("Aligning with Mission Pad 2 and landing...")

except Exception as e:
    print(f"An error occurred: {e}")
    drone.land()

finally:
    drone.disable_mission_pads()
    drone.end()