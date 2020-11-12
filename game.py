import sys
sys.path.append("engine/")
import engine as leaf
import obj
import threading
import multiplayer


mp = multiplayer.Multiplayer('http://127.0.0.1:5000')

def connected():
    leaf.add_monitor_text(lambda: "conectado", (0.5, 0.8), 32, 0)
    pass

def error():
    leaf.add_monitor_text(lambda: "error", (0.5, 0.8), 32, 0)
    pass

mp.on("connected", lambda: connected())
mp.on("error", lambda: error())

leaf.instantiate(obj.backgroundChanger)
leaf.start_game(300, 100)
