from math import pi, sin, cos

from direct.interval.FunctionInterval import PosInterval
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import ClockObject

key = {
    "Kiri": False,
    "Kanan": False,
    "Atas": False,
    "Bawah": False,
    "Shift": False

}
# Mengatur Kamera
camera = False
def CameraStatus(stats):
    camera = stats
    
# mengatur status
def keyState(type, stats):
    key[type] = stats


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setPos(-8, 42, 0)
        self.scene.setScale(0.25, 0.25, 0.25)
        # Meload Music
        self.music = self.loader.loadSfx("assets/Grasswalk.mp3")
        # Looping Music
        self.music.setLoop(True)
        # Menjalankan Music
        self.music.play()
        # Menjalankan Music dengan volume
        self.music.setVolume(0.9)
    
        # Menjalankan Camera
        self.cameraState()

        
        self.pandaActor = Actor("models/panda-model", {
            "walk": "models/panda-walk4"
        })

        # melakukan set besar aktor
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        # Menampilkan layar
        self.pandaActor.reparentTo(self.render)

        

        # posInterval1 = self.pandaActor.posInterval(13, Point3(0,-10,0), startPos=Point3(0,10,0))
        # posInterval2 = self.pandaActor.posInterval(13, Point3(0,10,0), startPos=Point3(0,-10,0))
        # hprInterval1 = self.pandaActor.hprInterval(1, Point3(180, 0,0), startHpr=Point3(0,0,0))
        # hprInterval2 = self.pandaActor.hprInterval(1, Point3(0, 0,0), startHpr=Point3(180,0,0))

        # self.pandaPace = Sequence(posInterval1, hprInterval1, posInterval2, hprInterval2, name="pandaPace")
        # self.pandaPace.loop()

        # Membuat controller
        # Tombol Atas
        self.accept("w",keyState,["Atas", True])
        self.accept("w-up", keyState,["Atas", False])
        # Tombol kanan
        self.accept("d",keyState,["Kanan", True])
        self.accept("d-up", keyState,["Kanan", False])
        # Tombol Kiri
        self.accept("a",keyState,["Kiri", True])
        self.accept("a-up", keyState,["Kiri", False])
        # Tombol Bawah
        self.accept("s",keyState,["Bawah", True])
        self.accept("s-up", keyState,["Bawah", False])

        self.accept("shift", keyState, ["Shift", True])
        self.accept("shift-up", keyState, ["Shift", False])
        
        

        self.taskMgr.add(self.gerakanUpate,"Update Gerakan")
    
    # Menjalankan fungsi status kamera
    def cameraState(self):
        if camera == True:
            self.enableMouse()
        else:
            self.disableMouse()
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    # memutar kamera
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi/180)
        
        self.camera.setPos(20 * sin(angleRadians), -
                           40 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    # melakukan update pada Gerakan Panda
    def gerakanUpate(self, task):
        # Jarak Tiap Waktu
        time = ClockObject.getGlobalClock()
        tick = time.getDt()

        speed = 10
        position = self.pandaActor.getPos()
        rotation = self.pandaActor.getHpr()
        
        

        if key['Atas']:
            
            position.y -= 0.5 * speed * tick
            rotation.x =  0
            

        elif key['Kiri']:
            
            position.x += 0.5 * speed * tick
            rotation.x = 90
        elif key['Kanan']:
            
            position.x -= 0.5 * speed * tick
            rotation.x =  270
        elif key['Bawah']:
            
            position.y += 0.5 * speed * tick
            rotation.x =  180
        elif key['Shift']:
            self.cameraState()


        self.pandaActor.setPos(position)
        self.pandaActor.setHpr(rotation)
        
        
        return task.cont

app = MyApp()
app.run()
