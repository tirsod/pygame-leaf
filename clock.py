from engine import *
import obj

init(300, 100)
instantiate(obj.backgroundChanger)
add_monitor_text(get_time_12hour, Positions.center, 32, 0)
start_game()

