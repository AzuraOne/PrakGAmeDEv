#!/usr/bin/env python

from panda3d.core import *
from decimal import *
getcontext().prec = 2


loadPrcFileData("", "audio-library-name p3openal_audio")

from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import *

def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(0, 0, 0, 1), shadow=(1, 1, 1, 1),
                        parent=base.a2dTopLeft, align=TextNode.ALeft,
                        pos=(0.08, -pos - 0.04), scale=.06)


def addTitle(text):
    return OnscreenText(text=text, style=1, pos=(-0.1, 0.09), scale=.08,
                        parent=base.a2dBottomRight, align=TextNode.ARight,
                        fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1))


class MediaPlayer(ShowBase):

    def __init__(self, media_file):

        ShowBase.__init__(self)

        self.title = addTitle("Panda3D: Tutorial - Media Player")
        self.inst1 = addInstructions(0.06, "P: Play/Pause")
        self.inst2 = addInstructions(0.12, "S: Stop and Rewind")
        self.inst3 = addInstructions(0.18,
            "M: Slow Motion / Normal Motion toggle")
        self.inst4 = addInstructions(0.24,
            "arrow up : higher sound, Arrow Down : lower sound")

        self.tex = MovieTexture("name")
        self.volume = 0.1
        
        success = self.tex.read(media_file)
        assert success, "Failed to load video!"

        cm = CardMaker("My Fullscreen Card")
        cm.setFrameFullscreenQuad()


        cm.setUvRange(self.tex)


        # Button 
        DirectButton(text=("Play", "Pause"), pos=(0, 0.9, 0.9),
                 scale=.05, command=self.playpause)
        DirectButton(text=("Stop"), pos=(0.2, 0.7, 0.9),
                 scale=.05, command=self.stopsound)
        self.slider = DirectSlider(range=(0, 10), value=1, pageSize=3, pos=(0.6, 0.7, 0.9), scale=0.3, orientation= DGG.HORIZONTAL, command=self.AdjustVolume)
       



        card = NodePath(cm.generate())
        card.reparentTo(self.render2d)
        card.setTexture(self.tex)

        self.sound = loader.loadSfx(media_file)
        self.sound.setVolume(self.volume)

        self.tex.synchronizeTo(self.sound)

        self.accept('p', self.playpause)
        self.accept('P', self.playpause)
        self.accept('s', self.stopsound)
        self.accept('S', self.stopsound)
        self.accept('m', self.fastforward)
        self.accept('M', self.fastforward)
        self.accept('arrow_up', self.AdjustSound,["arrow_up"])
        self.accept('arrow_up-up', self.AdjustSound, [''])
        self.accept('arrow_down', self.AdjustSound,['arrow_down'])
        self.accept('arrow_down-up', self.AdjustSound,[''])

    def stopsound(self):
        self.sound.stop()
        self.sound.setPlayRate(1.0)

    def fastforward(self):
        if self.sound.status() == AudioSound.PLAYING:

            t = self.sound.getTime()
            self.sound.stop()
            if self.sound.getPlayRate() == 1.0:
                self.sound.setPlayRate(0.5)
            else:
                self.sound.setPlayRate(1.0)
            self.sound.setTime(t)
            self.sound.play()

    def playpause(self):
        if self.sound.status() == AudioSound.PLAYING:
            
            t = self.sound.getTime()
            self.sound.stop()
            self.sound.setTime(t)
        else:
            self.sound.play()
    def AdjustVolume(self):
        if self.sound.status() == AudioSound.PLAYING:
            t = self.sound.getTime()
            self.sound.stop()
            print(self.slider['value'])
            self.sound.setVolume(self.slider['value'])

    def AdjustSound(self, status):
        print("test")
        if status == "arrow_up" and self.volume <= 1.0:
            
            t = self.sound.getTime()
            self.sound.stop()
            self.volume += 0.1
            self.sound.setTime(t)
            print(self.volume)
        if status == "arrow_down" and self.volume >= 0.0:
            t = self.sound.getTime()
            self.sound.stop()
            self.volume -= 0.1
            self.sound.setTime(t)
            print(self.volume)
        else:
            self.sound.play()

media = input("Masukkan nama file untuk diputar : ")
            
player = MediaPlayer(media)
player.run()
