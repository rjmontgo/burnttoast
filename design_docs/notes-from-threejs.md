- offload physics to web worker
    ex: https://github.com/schteppe/cannon.js/blob/master/examples/worker.html
- the expensive part isn't really the graphics is physics which are CPU limited
- use a broadphase SAP (may not work for really fast objects)
- allow object sleep
