from djitellopy import tello
from time import sleep
import KeyboardControls as KCModule

#   TELLO OBJECT | CONNECT FUNCTION CALL | KEYBOARD INITIALIZATION    #
KCModule.keyboardInit()
telloObj = tello.Tello()
telloObj.connect()
#   PRINTS OUT BATTERY  #
print(telloObj.get_battery())

#   RC CONTROL VALUES (MOTOR VELOCITY)
#   leftRightVelo, forwardBackwardVelo, upwardDownwardVelo, rotationalVelo = 0, 0, 0, 0
#   SEND RC CONTROL FUNCTION TEST
#   PARAMETERS (LEFT-RIGHT V, FORWARD-BACKWARD V, UPWARD-DOWNWARD V, ROTATIONAL/YAW V
#   ---------------------------------------------------------------------------------
# telloObj.takeoff()                       # TAKE OFF FUNCTION #
# sleep(1)                                 # DELAY FOR 1 SECOND #
# telloObj.send_rc_control(leftRightVelo, forwardBackwardVelo, upwardDownwardVelo , rotationalVelo)   # MOVEMENT #
# sleep(1)                                 #
# telloObj.send_rc_control(0, 0, 0, 0)     # STOP MOTORS #
# telloObj.land()                          # LAND FUNCTION #

#   MANUAL KEYBOARD CONTROLS
#   WASD FOR X-PLANE MOVEMENT | ARROW KEYS FOR Y-PLANE & ROTATIONAL MOVEMENT

def getKeyboardInput():
    leftRightVelo, forwardBackwardVelo, upwardDownwardVelo, rotationalVelo = 0, 0, 0, 0
    speedVal = 60

    if KCModule.keyPressCheck("q") and telloObj.get_battery() > 20: telloObj.takeoff()
    if KCModule.keyPressCheck("e"): telloObj.land()

    if KCModule.keyPressCheck("d"): leftRightVelo = speedVal
    elif KCModule.keyPressCheck("a"): leftRightVelo = -speedVal

    if KCModule.keyPressCheck("w"): forwardBackwardVelo = speedVal
    elif KCModule.keyPressCheck("s"): forwardBackwardVelo = -speedVal

    if KCModule.keyPressCheck("UP"): upwardDownwardVelo = speedVal
    elif KCModule.keyPressCheck("DOWN"): upwardDownwardVelo = -speedVal

    if KCModule.keyPressCheck("RIGHT"): rotationalVelo = speedVal
    elif KCModule.keyPressCheck("LEFT"): rotationalVelo = -speedVal

    return [leftRightVelo, forwardBackwardVelo, upwardDownwardVelo, rotationalVelo]

while True:
   value = getKeyboardInput()
   telloObj.send_rc_control(value[0], value[1], value[2], value[3])
   sleep(0.1)