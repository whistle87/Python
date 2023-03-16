import threading as th


class TraficLight:
    _colour_ = {'red': 7, 'yellow': 2, 'green': 5}
    keep_going = True



    def running(self, colour=_colour_):
        import time
        def key_capture_thread():
            global keep_going
            input()
            keep_going = False
        key_capture_thread()
        th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
        while keep_going:
            for key in colour:
                print("\n" * 25)
                print(key)
                time.sleep(colour[key])


first_light = TraficLight()
first_light.running()
