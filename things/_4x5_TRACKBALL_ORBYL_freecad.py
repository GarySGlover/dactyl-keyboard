
import FreeCAD
import ImportGui
import Mesh

def closeDocs():
    documentList = App.listDocuments()

    for doc in documentList:
        App.closeDocument(doc)

def process_item(filename):
    closeDocs()
    ImportGui.open(filename + '.step')
    Gui.Selection.addSelection("Unnamed", 'Solid')
    obj = Gui.Selection.getSelection()
    Mesh.export(obj, filename + '_freecad.stl')

files = [ "/home/clover/dactyl-keyboard/things/_4x5_TRACKBALL_ORBYL_right","/home/clover/dactyl-keyboard/things/_4x5_TRACKBALL_ORBYL_left","/home/clover/dactyl-keyboard/things/_4x5_TRACKBALL_ORBYL_right_plate","/home/clover/dactyl-keyboard/things/_4x5_TRACKBALL_ORBYL_left_plate" ]

documentList = App.listDocuments()

for doc in documentList:
    App.closeDocument(doc)


for file in files:
    try:
        process_item(file)
    except Exception as err:
        print(f"Error {err=}, {type(err)=}")


print('Done')
