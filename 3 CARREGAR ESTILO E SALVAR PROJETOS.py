import os # This is is needed in the pyqgis console also
from qgis.core import (
    QgsVectorLayer)

project = QgsProject.instance()



################################################################################    
##                              CAMINHO
path_map = "C:/@IGOR/PYTHON/MAPA/app.shp"
###############################################################################

properties = {}
properties["outline_color"] ='#0,0,0,0'

##NOMEANDO VARIAVEIS
layer_name_ctc4 = 'CTC4 20-40 cm' 
layer_name_ctc3 = 'CTC3 10-20 cm' 
layer_name_ctc2 = 'CTC2 0-10 cm'
layer_name_ag2 = 'Argila2 0-10 cm' ##METODO CTC E ARGILA INTERVALO IGUAL
value_field_ctc4 = 'CTC4'
value_field_ctc3 = 'CTC3'
value_field_ctc2 = 'CTC2'
value_field_ag2 = 'ARGILA2'
num_classes = 5
ramp_name_red = 'Reds'
ramp_name_ag = 'ARGILA'

##CONFIGURAÇÃO LABEL SIMBOLOGIA

format = QgsRendererRangeLabelFormat()
format.setFormat("%1 - %2")
format.setPrecision(2)
format.setTrimTrailingZeroes(True)

##METODO DE CLASSIFICAÇÃO PARA CTC E ARGILA


##  IMPORTAÇÃO ARGILA2
ARG2 = QgsVectorLayer(path_map, "Argila2 0-10 cm", "ogr")
if not ARG2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(ARG2)    
    
layer = QgsProject().instance().mapLayersByName('Argila2 0-10 cm')[0]
vals = []
fld = 'ARGILA2'
for f in layer.getFeatures():
    vals.append(f[fld])
# If you don't like these colors, change them out for ones you do, using hexcodes,
# RGB codes etc. as long as the items in this list are valid strings you
# can pass to a QColor constructor 
colors = ['#ffffd4', '#fed98e','#fe9929', '#d95f0e','#993404']
lower = sorted(vals)[0]
upper = sorted(vals)[-1]
step = (upper-lower)/len(colors)
range_list = []
for c in colors:
    cat = [lower, lower+step, c]
    sym = QgsSymbol.defaultSymbol(layer.geometryType())
    sym = QgsFillSymbol.createSimple(properties)
    sym.setColor(QColor(cat[2]))
    rng = QgsRendererRange(cat[0], cat[1], sym, '{0:.1f}-{1:.1f}'.format(cat[0], cat[1]))
    range_list.append(rng)
    lower = (lower+step)
renderer = QgsGraduatedSymbolRenderer(fld, range_list)
layer.setRenderer(renderer)
layer.triggerRepaint()

##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

##SALVAR ARG2

ARGILA2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/ARGILA2.qgz")

##FIM DO PRIMEIRO BLOCO
QgsProject.instance().removeMapLayers( [ARG2.id()] ) ##REMOVE UM LAYER   

################################################################################
##                  INICIO DO SEGUNDO BLOCO
################################################################################
##MO2
MO2 = QgsVectorLayer(path_map, "MO2 0-10 cm", "ogr")
if not MO2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(MO2)

MO2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/mo2%.qml")
MO2.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

##SALVANDO MO2
MO2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/MO2.qgz")

##REMOVENDO MO2

to_be_deleted = project.mapLayersByName('MO2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

###

##MO3
MO3 = QgsVectorLayer(path_map, "MO3 10-20 cm", "ogr")
if not MO3.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(MO3)

MO3.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/mo3%.qml")
MO3.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)


## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()
##SALVANDO MO3
MO3= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/MO3.qgz")

##REMOVENDO MO3

to_be_deleted = project.mapLayersByName('MO3 10-20 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO TERCEIRO BLOCO
################################################################################

## IMPORTACAO CTC2
CTC2 = QgsVectorLayer(path_map, "CTC2 0-10 cm", "ogr")
if not CTC2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(CTC2)

layer = QgsProject().instance().mapLayersByName('CTC2 0-10 cm')[0]
vals = []
fld = 'CTC2'
for f in layer.getFeatures():
    vals.append(f[fld])
# If you don't like these colors, change them out for ones you do, using hexcodes,
# RGB codes etc. as long as the items in this list are valid strings you
# can pass to a QColor constructor 
colors = ['#fee1e1', '#fe8787', '#ff0000', '#ae0000', '#630000']
lower = sorted(vals)[0]
upper = sorted(vals)[-1]
step = (upper-lower)/len(colors)
range_list = []
for c in colors:
    cat = [lower, lower+step, c]
    sym = QgsSymbol.defaultSymbol(layer.geometryType())
    sym = QgsFillSymbol.createSimple(properties)
    sym.setColor(QColor(cat[2]))
    rng = QgsRendererRange(cat[0], cat[1], sym, '{0:.1f}-{1:.1f}'.format(cat[0], cat[1]))
    range_list.append(rng)
    lower = (lower+step)
renderer = QgsGraduatedSymbolRenderer(fld, range_list)
layer.setRenderer(renderer)
layer.triggerRepaint()

##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO CTC2

CTC2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/CTC2.qgz")

##REMOVENDO CTC2
to_be_deleted = project.mapLayersByName('CTC2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

##########################################################################
##########################################################################

## IMPORTACAO CTC3
CTC3 = QgsVectorLayer(path_map, "CTC3 10-20 cm", "ogr")
if not CTC3.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(CTC3)

layer = QgsProject().instance().mapLayersByName('CTC3 10-20 cm')[0]
vals = []
fld = 'CTC3'
for f in layer.getFeatures():
    vals.append(f[fld])
# If you don't like these colors, change them out for ones you do, using hexcodes,
# RGB codes etc. as long as the items in this list are valid strings you
# can pass to a QColor constructor 
colors = ['#fee1e1', '#fe8787', '#ff0000', '#ae0000', '#630000']
lower = sorted(vals)[0]
upper = sorted(vals)[-1]
step = (upper-lower)/len(colors)
range_list = []
for c in colors:
    cat = [lower, lower+step, c]
    sym = QgsSymbol.defaultSymbol(layer.geometryType())
    sym = QgsFillSymbol.createSimple(properties)
    sym.setColor(QColor(cat[2]))
    rng = QgsRendererRange(cat[0], cat[1], sym, '{0:.1f}-{1:.1f}'.format(cat[0], cat[1]))
    range_list.append(rng)
    lower = (lower+step)
renderer = QgsGraduatedSymbolRenderer(fld, range_list)
layer.setRenderer(renderer)
layer.triggerRepaint()


##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO CTC3

CTC3= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/CTC3.qgz")

###REMOVENDO CTC3
to_be_deleted = project.mapLayersByName('CTC3 10-20 cm')[0]
project.removeMapLayer(to_be_deleted.id())

##########################################################################
##########################################################################

## IMPORTACAO CTC4
CTC4 = QgsVectorLayer(path_map, "CTC4 20-40 cm", "ogr")
if not CTC4.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(CTC4)

layer = QgsProject().instance().mapLayersByName('CTC4 20-40 cm')[0]
vals = []
fld = 'CTC4'
for f in layer.getFeatures():
    vals.append(f[fld])
# If you don't like these colors, change them out for ones you do, using hexcodes,
# RGB codes etc. as long as the items in this list are valid strings you
# can pass to a QColor constructor 
colors = ['#fee1e1', '#fe8787', '#ff0000', '#ae0000', '#630000']
lower = sorted(vals)[0]
upper = sorted(vals)[-1]
step = (upper-lower)/len(colors)
range_list = []
for c in colors:
    cat = [lower, lower+step, c]
    sym = QgsSymbol.defaultSymbol(layer.geometryType())
    sym = QgsFillSymbol.createSimple(properties)
    sym.setColor(QColor(cat[2]))
    rng = QgsRendererRange(cat[0], cat[1], sym, '{0:.1f}-{1:.1f}'.format(cat[0], cat[1]))
    range_list.append(rng)
    lower = (lower+step)
renderer = QgsGraduatedSymbolRenderer(fld, range_list)
layer.setRenderer(renderer)
layer.triggerRepaint()

##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO CTC4
CTC4= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/CTC4.qgz")
###REMOVENDO CTC4
to_be_deleted = project.mapLayersByName('CTC4 20-40 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO QUARTO BLOCO
################################################################################

##PH2   
PH2 = QgsVectorLayer(path_map, "pH2 0-10 cm", "ogr")
if not PH2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(PH2) 
    
PH2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/ph2.qml")
PH2.triggerRepaint()

##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO PH2
PH2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/PH2.qgz")
####REMOVENDO PH2
to_be_deleted = project.mapLayersByName('pH2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO QUINTO BLOCO
################################################################################

##PH3   
PH3 = QgsVectorLayer(path_map, "pH3 10-20 cm", "ogr")
if not PH3.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(PH3) 
    
PH3.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/ph3.qml")
PH3.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO PH3
PH2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/PH3.qgz")
####REMOVENDO PH3
to_be_deleted = project.mapLayersByName('pH3 10-20 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO SEXTO BLOCO
################################################################################

##V2

V2 = QgsVectorLayer(path_map, "V2 0-10 cm", "ogr")
if not V2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(V2) 
    
V2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/v2.qml")
V2.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO V2
V2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/V2.qgz")
####REMOVENDO V2
to_be_deleted = project.mapLayersByName('V2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO SETIMO BLOCO
################################################################################

##V3

V3 = QgsVectorLayer(path_map, "V3 10-20 cm", "ogr")
if not V3.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(V3) 
    
V3.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/v3.qml")
V3.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()


## SALVANDO V3
V3= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/V3.qgz")
####REMOVENDO V3
to_be_deleted = project.mapLayersByName('V3 10-20 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO OITAVO BLOCO
################################################################################

##V4

V4 = QgsVectorLayer(path_map, "V4 20-40 cm", "ogr")
if not V4.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(V4) 
    
V4.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/v4.qml")
V4.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()


## SALVANDO V3
V4= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/V4.qgz")
####REMOVENDO V3
to_be_deleted = project.mapLayersByName('V4 20-40 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO NONO BLOCO
################################################################################

##CA2

CA2 = QgsVectorLayer(path_map, "Ca2 0-10 cm", "ogr")
if not CA2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(CA2) 

CA2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/ca2.qml")
CA2.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO CA2
CA2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/CA2.qgz")
####REMOVENDO CA2
to_be_deleted = project.mapLayersByName('Ca2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO NONO BLOCO
################################################################################

##CA3

CA3 = QgsVectorLayer(path_map, "Ca3 10-20 cm", "ogr")
if not CA3.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(CA3) 

CA3.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/ca3.qml")
CA3.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO CA3
CA3= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/CA3.qgz")
####REMOVENDO CA3
to_be_deleted = project.mapLayersByName('Ca3 10-20 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO DECIMO BLOCO
################################################################################

##CA4

CA4 = QgsVectorLayer(path_map, "Ca4 20-40 cm", "ogr")
if not CA4.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(CA4) 

CA4.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/ca4.qml")
CA4.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO CA4
CA4= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/CA4.qgz")
####REMOVENDO CA4
to_be_deleted = project.mapLayersByName('Ca4 20-40 cm')[0]
project.removeMapLayer(to_be_deleted.id())


################################################################################
##                  INICIO DO DECIMO PRIMEIRO BLOCO
################################################################################

##MG2

MG2 = QgsVectorLayer(path_map, "Mg2 0-10 cm", "ogr")
if not MG2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(MG2) 

MG2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/mg2.qml")
MG2.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO MG2
MG2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/MG2.qgz")
####REMOVENDO MG2
to_be_deleted = project.mapLayersByName('Mg2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())


################################################################################
##                  INICIO DO DECIMO PRIMEIRO BLOCO
################################################################################

##MG3

MG3 = QgsVectorLayer(path_map, "Mg3 10-20 cm", "ogr")
if not MG3.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(MG3) 

MG3.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/mg3.qml")
MG3.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO MG2
MG3= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/MG3.qgz")
####REMOVENDO MG2
to_be_deleted = project.mapLayersByName('Mg3 10-20 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 12 BLOCO
################################################################################
K2 = QgsVectorLayer(path_map, "K2 0-10 cm", "ogr")
if not K2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(K2) 

K2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/k2.qml")
K2.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO K2
K2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/K2.qgz")
####REMOVENDO K2
to_be_deleted = project.mapLayersByName('K2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 13 BLOCO
################################################################################

K3 = QgsVectorLayer(path_map, "K3 10-20 cm", "ogr")
if not K3.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(K3) 

K3.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/k3.qml")
K3.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()


## SALVANDO K3
K2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/K3.qgz")
####REMOVENDO K3
to_be_deleted = project.mapLayersByName('K3 10-20 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 14 BLOCO
################################################################################

##P2

P2 = QgsVectorLayer(path_map, "P res2 0-10 cm", "ogr")
if not P2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(P2) 
    
P2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/pres2.qml")
P2.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO P2
P2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/P2.qgz")
####REMOVENDO P2
to_be_deleted = project.mapLayersByName('P res2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 15 BLOCO
################################################################################

##P3

P3 = QgsVectorLayer(path_map, "P res3 10-20 cm", "ogr")
if not P3.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(P3) 
    
P3.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/pres3.qml")
P3.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO P3
P3= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/P3.qgz")
####REMOVENDO P3
to_be_deleted = project.mapLayersByName('P res3 10-20 cm')[0]
project.removeMapLayer(to_be_deleted.id())


################################################################################
##                  INICIO DO 16 BLOCO
################################################################################

##AL2

AL2 = QgsVectorLayer(path_map, "Al2 0-10 cm", "ogr")
if not AL2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(AL2) 

AL2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/al2.qml")
AL2.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO AL2
AL2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/AL2.qgz")
####REMOVENDO AL2
to_be_deleted = project.mapLayersByName('Al2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())


################################################################################
##                  INICIO DO 17 BLOCO
################################################################################

##AL3

AL3 = QgsVectorLayer(path_map, "Al3 10-20 cm", "ogr")
if not AL3.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(AL3) 

AL3.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/al3.qml")
AL3.triggerRepaint()

##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO AL3
AL3= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/AL3.qgz")
####REMOVENDO AL3
to_be_deleted = project.mapLayersByName('Al3 10-20 cm')[0]
project.removeMapLayer(to_be_deleted.id())




################################################################################
##                  INICIO DO 18 BLOCO
################################################################################

##AL4

AL4 = QgsVectorLayer(path_map, "Al4 20-40 cm", "ogr")
if not AL4.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(AL4) 

AL4.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/al4.qml")
AL4.triggerRepaint()

##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO AL4
AL4= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/AL4.qgz")
####REMOVENDO AL4
to_be_deleted = project.mapLayersByName('Al4 20-40 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 19 BLOCO
################################################################################

##S2

S2 = QgsVectorLayer(path_map, "S2 0-10 cm", "ogr")
if not S2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(S2) 

S2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/s2.qml")
S2.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO S2
S2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/S2.qgz")
####REMOVENDO S2
to_be_deleted = project.mapLayersByName('S2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 20 BLOCO
################################################################################

##S4

S4 = QgsVectorLayer(path_map, "S4 20-40 cm", "ogr")
if not S4.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(S4) 

S4.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/s4.qml")
S4.triggerRepaint()
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO S4
S4= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/S4.qgz")
####REMOVENDO S4
to_be_deleted = project.mapLayersByName('S4 20-40 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 21 BLOCO
################################################################################

##B2

B2 = QgsVectorLayer(path_map, "B2 0-10 cm", "ogr")
if not B2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(B2) 
    
B2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/b2.qml")
B2.triggerRepaint()    
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO B2
B2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/B2.qgz")
####REMOVENDO B2
to_be_deleted = project.mapLayersByName('B2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 22 BLOCO
################################################################################

##CU2

CU2 = QgsVectorLayer(path_map, "CU2 0-10 cm", "ogr")
if not CU2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(CU2) 
    
CU2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/cu2.qml")
CU2.triggerRepaint()    
##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO CU2
CU2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/CU2.qgz")
####REMOVENDO CU2
to_be_deleted = project.mapLayersByName('CU2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 23 BLOCO
################################################################################

##MN2

MN2 = QgsVectorLayer(path_map, "Mn2 0-10 cm", "ogr")
if not MN2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(MN2) 
    
MN2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/mn2.qml")
MN2.triggerRepaint()    

##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO MN2
MN2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/MN2.qgz")
####REMOVENDO MN2
to_be_deleted = project.mapLayersByName('Mn2 0-10 cm')[0]
project.removeMapLayer(to_be_deleted.id())


################################################################################
##                  INICIO DO 24 BLOCO
################################################################################

##ZN2

ZN2 = QgsVectorLayer(path_map, "Zn2 0-10 cm", "ogr")
if not ZN2.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(ZN2) 
    
ZN2.loadNamedStyle("C:/@IGOR/PYTHON/MAPA/LEGENDAS/zn2.qml")
ZN2.triggerRepaint()    

##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)

## HABILITANDO ATZ AUTOMATICA
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(True)
legend.adjustBoxSize()
layout.refresh()

##REMOVENDO LAYER CO
layer_to_remove = project.mapLayersByName('co')[0]
layout = project.layoutManager().layoutByName('FERTILIDADE')
legend = [i for i in layout.items() if isinstance(i, QgsLayoutItemLegend)][0]
legend.setAutoUpdateModel(False)
legend.model().rootGroup().removeLayer(layer_to_remove)
legend.adjustBoxSize()
layout.refresh()

## SALVANDO ZN2
ZN2= QgsProject.instance().write("C:/@IGOR/PYTHON/MAPA/PROJETOS/ZN2.qgz")
####REMOVENDO ZN2
#to_be_deleted = project.mapLayersByName('Zn2 0-10 cm')[0]
#project.removeMapLayer(to_be_deleted.id())

################################################################################
##                  INICIO DO 25 BLOCO
################################################################################

##MOVENDO LAYER PARA O TOPO
#alayer = QgsProject.instance().mapLayersByName("co")[0]

#root = QgsProject.instance().layerTreeRoot()

# Move Layer
#myalayer = root.findLayer(alayer.id())
#myClone = myalayer.clone()
#parent = myalayer.parent()
#parent.insertChildNode(0, myClone)
#parent.removeChildNode(myalayer)



































