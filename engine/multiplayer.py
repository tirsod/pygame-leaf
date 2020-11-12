import requests
import socketio
import socketio.exceptions
import eventlet
import threading
from event import Event


class Multiplayer(Event):
    def __init__(self, hosturl):
        super().__init__()
        sio = socketio.Client()
        sio_sv = socketio.Server(async_mode='eventlet', logger=True)
        self.ip = hosturl

        def start_server():
            # wrap with a WSGI application
            app = socketio.WSGIApp(sio_sv)

            eventlet.wsgi.server(eventlet.listen(('localhost', 8000)), app)

        @sio_sv.event
        def connect(sid, environ):
            sio_sv.emit('connected', {'id': sid}, to=sid)

        #@sio_sv.on('pito')
        #def pito(sid, data):
            #print('recibi pito: '+str(data))
            #self.verga = str(data)

        def connect_server():
            try:
                sio.connect(self.ip)

                #sio.emit('pito', data={'yes': 3})

            except socketio.exceptions.ConnectionError:
                self.events["error"]()

        @sio.event
        def connected(data):
            self.events["connected"]()
            #print("I'm connected! " + str(data))


        server_thread = threading.Thread(target=start_server)
        server_thread.start()

        client_thread = threading.Thread(target=connect_server)
        client_thread.start()
