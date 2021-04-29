from time import clock

class StopWatch: #class name
    def __init__(self): #class constructor
        self.reset(); #class method call

    def reset(self): #clas method
        self._start_time=self._elapsed=0; #set starttime and elapsed time to zero
        self._running=False; #set running false

    def elapsed(self): #class method
        if not self._running:
            return self._elapsed;
        else:
            return clock()-self._start_time;

    def stop(self): #class method definition
        if self._running:
            self._elapsed=clock()-self._start_time
            self._running=False;

    def start(self): #class method
        if not self._running:
            self._start_time=clock()-self._elapsed
            self._running=True;