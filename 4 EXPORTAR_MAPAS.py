from PyQt5.QtWidgets import QFileDialog
import os
import processing


folderpath = QFileDialog.getExistingDirectory(None, 'Selecione a pasta de entrada')
outputpath = QFileDialog.getExistingDirectory(None, 'Selecione a pasta de saída')


print (folderpath)
print (outputpath)


for root, dirs, files in os.walk (folderpath):
    for file in files:
        if file.endswith ('.qgz') or file.endswith ('.qgs'):
            arq = os.path.join (root, file)
            #print (arq)
            
            try:
                file_pdf = str (file).replace ('qgz', 'pdf')
            except:
                file_pdf = str (file).replace ('qgs', 'pdf')

            
            try:
                file_img = str (file).replace ('qgz', 'png')
            except:
                file_img = str (file).replace ('qgs', 'png')
            
            try:
                file_name = str (file).replace ('qgz', '')
            except:
                file_name = str (file).replace ('qgs', '')


            project = QgsProject.instance()
            project.read(arq)
            manager = project.layoutManager()
            layouts_list = manager.printLayouts()
            for layout in layouts_list:
                name_layout = layout.name()
                print (layout.name())
                file_img = file_name + '_' + name_layout + '_' + file_img
                file_img = os.path.join (root, file_img)
                #print (file_img)
                file_pdf = file_name + '_' +  name_layout + '_' +  file_pdf
                file_pdf = os.path.join (root,  file_pdf)
                #print (file_pdf)
                exporter = QgsLayoutExporter(layout)
                #fn = 'D://_teste_export_maps//_teste.pdf'
                camada_atlas = (layout.atlas().coverageLayer ())
                #exporter.exportToImage(file_img, QgsLayoutExporter.ImageExportSettings())
                #exporter.exportToPdf(file_pdf, QgsLayoutExporter.PdfExportSettings())

                if camada_atlas == None:
                    print ('Fluxo mapa unico')
                    exporter.exportToImage(file_img, QgsLayoutExporter.ImageExportSettings())
                    #exporter.exportToPdf(file_pdf, QgsLayoutExporter.PdfExportSettings())
                else:
                    print ('Fluxo mapa atlas')
                    processing.run("native:atlaslayouttoimage", {'LAYOUT':name_layout,'COVERAGE_LAYER':None,'FILTER_EXPRESSION':'','SORTBY_EXPRESSION':'','SORTBY_REVERSE':False,'FILENAME_EXPRESSION':'\'{0}_\'||@atlas_pagename'.format (file_name + '_' + name_layout ),'FOLDER':outputpath,'LAYERS':None,'EXTENSION':8,'DPI':None,'GEOREFERENCE':True,'INCLUDE_METADATA':True,'ANTIALIAS':True})
                    #file_pdf = root+ '/' + name_layout + '_' +  file_pdf

                    #processing.run("native:atlaslayouttopdf", {'LAYOUT':name_layout,'COVERAGE_LAYER':None,'FILTER_EXPRESSION':'','SORTBY_EXPRESSION':'','SORTBY_REVERSE':False,'OUTPUT': '{0}'.format (file_pdf) ,'LAYERS':None,'DPI':None,'FORCE_VECTOR':False,'GEOREFERENCE':True,'INCLUDE_METADATA':True,'DISABLE_TILED':False,'SIMPLIFY':True,'TEXT_FORMAT':0})
 
print ('Finalizado') 

