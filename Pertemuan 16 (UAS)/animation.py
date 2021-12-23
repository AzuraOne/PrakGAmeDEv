from math import pi, sin, cos
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import ShowBase
from direct.interval.FunctionInterval import PosInterval
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import ClockObject


def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(0, 0, 0, 1), shadow=(1, 1, 1, 1),
                        parent=base.a2dTopLeft, align=TextNode.ALeft,
                        pos=(0.08, -pos - 0.04), scale=.06)



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

       
        self.inst1 = addInstructions(0.06, "W: Berjalan ke depan")
        self.inst2 = addInstructions(0.12, "A: Berjalan ke samping")
        self.inst3 = addInstructions(0.18,
            "S: Berjalan ke belakang")
        self.inst4 = addInstructions(0.24,
            "D : Berjalan ke kanan")





       
        self.scene = self.loader.loadModel("models/environment") # Melakukan Load pada environtment
        self.scene.reparentTo(self.render) # Melakukan render pada environtment
        self.scene.setPos(-8, 42, 0) # mengatur posisi environtment
        self.scene.setScale(0.25, 0.25, 0.25) # mengatur skala
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
        }) # melakukan load data pada Aktor

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
        self.accept("w",keyState,["Atas", True]) # ketika w dipencet akan mengubah status atas menjadi true
        self.accept("w-up", keyState,["Atas", False]) # ketika w dilepas status atas berubah menjadi false
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
        
        

        self.taskMgr.add(self.gerakanUpate,"Update Gerakan") # berfungsi untuk melakukan looping pada gerakan 
    
    # Menjalankan fungsi status kamera
    def cameraState(self):
        if camera == True:
            self.enableMouse() # mengijinkan menggunakan cursor mouse / menampilkan cursor mouse
        else:
            self.disableMouse() # melakukan disable pada cursor sehingga mouse hilang
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask") # melakukan looping pada fungsi perputaran kamera

    # memutar kamera
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0 # memutar kamera berdasarkan waktu
        angleRadians = angleDegrees * (pi/180) # melakukan setting pada kecepatan perputaran berdasaran angle dan pi / 180
        
        self.camera.setPos(20 * sin(angleRadians), -
                           40 * cos(angleRadians), 3) # posisi akan berputar searah
        self.camera.setHpr(angleDegrees, 0, 0) # perputaran akan berada pada sumbu x
        return Task.cont # menjalankan fungsi task time

    # melakukan update pada Gerakan Panda
    def gerakanUpate(self, task):
        # Jarak Tiap Waktu
        time = ClockObject.getGlobalClock() 
        tick = time.getDt() # mengatur Dt jam

        speed = 10 # kmengatur kecepatan
        position = self.pandaActor.getPos() # membaca posisi panda
        rotation = self.pandaActor.getHpr() # membaca rotasi panda
        
        

        if key['Atas']: # jika tombol atas ditekan makan
            
            position.y -= 0.5 * speed * tick # posisi di sumbu y akan dikurangi 5 sedangkan rotasi x 0
            rotation.x =  0
            

        elif key['Kiri']: # jika pengguna melakukan klik yang menjalankan fungsi kiri akan mengubah arah posisi x dan rotasi sebesar 90 derajat
            
            position.x += 0.5 * speed * tick 
            rotation.x = 90
        elif key['Kanan']:
            
            position.x -= 0.5 * speed * tick
            rotation.x =  270
        elif key['Bawah']:
            
            position.y += 0.5 * speed * tick
            rotation.x =  180
        elif key['Shift']:
            self.cameraState() # keyboard shift berfungsi untuk menghentikan pergerakan kamera yang selalu bergerak


        self.pandaActor.setPos(position) # melakukan set posisi berdasarkan pos
        self.pandaActor.setHpr(rotation) # melakukan set sudut
        
        
        return task.cont

app = MyApp()
app.run()
