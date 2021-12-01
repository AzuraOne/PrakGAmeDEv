import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d.core import TextNode

from direct.gui.DirectGui import DirectFrame

# Add some text
bk_text = "Kelompok 6"
textObject = OnscreenText(text=bk_text, pos=(0.0, 0.70), scale=0.10,
                          fg=(6, 6, 6, 6), align=TextNode.ACenter,
                          mayChange=1)
# Callback function to set text
v = [0]


def setText(status=None):

    bk_text = "CurrentValue : %s" % v
    textObject.setText(bk_text)
    


def itemSel(arg):
    if arg == "Pilih Anggota Kelompok":
        l1 = DirectLabel(text="Kelompok 6", text_scale=0.07)
        l2 = DirectLabel(text="Kelas D", text_scale=0.08)
        l3 = DirectLabel(text="UNS", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(1, 0, 0, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in []:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='tampan.jpg', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Anggota 1":
        
        

        l1 = DirectLabel(text="Nama : Clarissa Putri Aurellia", text_scale=0.07)
        l2 = DirectLabel(text="NIM : V3920015", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),


            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(1, 0, 1, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'HOBI', 'Nonton,', 'Masak']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='clar.png', pos=(0.45, 0, -0.45), scale=0.35,)


    if arg == "Anggota 2":
        l1 = DirectLabel(text="Nama  : Augesvina Seiyusanda L", text_scale=0.07)
        l2 = DirectLabel(text="NIM : V3920011", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
             decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(0, 0, 1, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'HOBI', 'Nonton,', 'Desain']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='auges.png', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Anggota 3":
        l1 = DirectLabel(text="Nama : Alfida Shofiya Mufti", text_scale=0.07)
        l2 = DirectLabel(text="Nim : V3920005", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
             decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),


            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(0, 1, 0, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'HOBI', 'Gamer,', 'Masak']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='sofi.png', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Anggota 4":
        l1 = DirectLabel(text="Nama : Hildanniar Fauzi", text_scale=0.07)
        l2 = DirectLabel(text="Nim : V3920026", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),


            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(1, 1, 0, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'HOBI', 'Gamer', 'Membaca']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='hildan.png', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Anggota 5":
        l1 = DirectLabel(text="Nama : Farhanang Wahyu Aprian", text_scale=0.07)
        l2 = DirectLabel(text="Nim : V3920021", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(0.0, 0.7, -0.05, 0.59),
            frameColor=(0, 1, 1, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'HOBI', 'Coding', 'Gaming']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='farhanang.jpg', pos=(0.45, 0, -0.45), scale=0.35,)


# Create a frame
menu = DirectOptionMenu(text="options", scale=0.1, initialitem=2,
                        items=["Pilih Anggota Kelompok", "Anggota 1",
                               "Anggota 2", "Anggota 3", "Anggota 4", "Anggota 5"],
                        highlightColor=(0.65, 0.1, 0.1, 1),
                        command=itemSel, textMayChange=1)


def showValue():
    return menu


# Procedurally select a item
menu.set(0)

# Run the program
base.run()
