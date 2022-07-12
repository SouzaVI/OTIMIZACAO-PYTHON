
    ##CRIANDO LAYOUT DE IMPRESSAO
project = QgsProject.instance()
manager = project.layoutManager()
layout = QgsPrintLayout(project)
layoutName = 'FERTILIDADE'
layout.initializeDefaults()
layout.setName(layoutName)
manager.addLayout(layout)

##ADICIONANDO MAPA
map = QgsLayoutItemMap(layout)
map.setBackgroundColor(QColor(0,0,0,0))
map.setRect(20,20,20,20)
canvas = iface.mapCanvas()
map.setExtent(canvas.extent())
layout.addLayoutItem(map)
map.attemptResize(QgsLayoutSize(225.87, 199.75, QgsUnitTypes.LayoutMillimeters))
map.attemptMove(QgsLayoutPoint(44.96, 5.10, QgsUnitTypes.LayoutMillimeters))

##LEGENDA

legend = QgsLayoutItemLegend(layout)
layout.addLayoutItem(legend)
newFont = QFont("ARIAL", 14)
legend.setStyleFont(QgsLegendStyle.Title,newFont)
legend.setStyleFont(QgsLegendStyle.Subgroup, newFont)
legend.setStyleFont(QgsLegendStyle.SymbolLabel, newFont)
#legend.setLinkedMap(map) # pass a QgsLayoutItemMap object
legend.setLegendFilterByMapEnabled(True)
legend.refresh()
legend.setBackgroundColor(QColor(0,0,0,0))
legend.attemptMove(QgsLayoutPoint(18.0,5.10, QgsUnitTypes.LayoutMillimeters))


##MOVENDO LAYER PARA O TOPO
alayer = QgsProject.instance().mapLayersByName("co")[0]

root = QgsProject.instance().layerTreeRoot()

# Move Layer
myalayer = root.findLayer(alayer.id())
myClone = myalayer.clone()
parent = myalayer.parent()
parent.insertChildNode(0, myClone)
parent.removeChildNode(myalayer)