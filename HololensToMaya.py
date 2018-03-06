import maya.cmds as cmds

sessionId = 0
trackedCubeId = 0
currentBoxName = ''
singleFilter = "All Files (*.*)"
dialogResuls = cmds.fileDialog2(fileMode=1, caption="Select Log File")

if dialogResuls != None : 
    filePath = dialogResuls[0]
    qbfile = open(filePath,'r')
    
    for aline in qbfile.readlines():
        if aline.startswith('Begin Logger Session'):
            sessionId = sessionId + 1
            currentBoxName = 'cameraProxy' + str(sessionId)
            cmds.polyCube( name=currentBoxName)
        values = aline.split(',')
        if values[0] == 'Log Entry' and currentBoxName != '':
            frameValue = values[1]
            positionValues = values[2].split(' ')
            rotationValues = values[3].split(' ')
            cmds.setKeyframe(currentBoxName, time=eval(frameValue), attribute='translateX', v=eval(positionValues[0]))
            cmds.setKeyframe(currentBoxName, time=eval(frameValue), attribute='translateY', v=eval(positionValues[1]))
            cmds.setKeyframe(currentBoxName, time=eval(frameValue), attribute='translateZ', v=eval(positionValues[2]))
            
            cmds.setKeyframe(currentBoxName, time=eval(frameValue), attribute='rotateX', v=eval(rotationValues[0]))
            cmds.setKeyframe(currentBoxName, time=eval(frameValue), attribute='rotateY', v=eval(rotationValues[1]))
            cmds.setKeyframe(currentBoxName, time=eval(frameValue), attribute='rotateZ', v=eval(rotationValues[2]))
        
        if values[0] == 'Tracker Entry':
            trackedCubeId = trackedCubeId + 1
            frameValue = values[1]
            positionValues = values[2].split(' ')
            trackedCubeName = 'trackedCube' + str(trackedCubeId)
            cmds.polyCube( name=trackedCubeName)
            cmds.setKeyframe(trackedCubeName, time=eval(frameValue), attribute='translateX', v=eval(positionValues[0]))
            cmds.setKeyframe(trackedCubeName, time=eval(frameValue), attribute='translateY', v=eval(positionValues[1]))
            cmds.setKeyframe(trackedCubeName, time=eval(frameValue), attribute='translateZ', v=eval(positionValues[2]))
            cmds.setKeyframe(trackedCubeName, time=eval(frameValue), attribute='scaleX', v=.1)
            cmds.setKeyframe(trackedCubeName, time=eval(frameValue), attribute='scaleY', v=.1)
            cmds.setKeyframe(trackedCubeName, time=eval(frameValue), attribute='scaleZ', v=.1)
            
            
    qbfile.close()