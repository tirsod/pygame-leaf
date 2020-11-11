import sys
sys.path.append("engine/")
import engine as leaf
import obj

leaf.instantiate(obj.backgroundChanger)
leaf.add_monitor_text(leaf.get_time_12hour, (0.5, 0.8), 32, 0)
leaf.start_game(300, 100)

