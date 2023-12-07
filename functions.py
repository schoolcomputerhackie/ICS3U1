app.compiled = []
app.polygon = ''
def comp():
    counter = 0
    for i in app.compiled:
        try:
            print("Line("+str(app.compiled[counter][0])+", "+str(app.compiled[counter][1])+', '+str(app.compiled[counter+1][0])+', '+str(app.compiled[counter+1][1])+')')
        except:
            pass
        counter += 1
def polycomp():
    counter = 0
    app.polygon = 'Polygon('
    print(len(app.compiled))
    for i in app.compiled:
        if not counter+1 == len(app.compiled):
            print(counter)
            app.polygon = app.polygon + str(app.compiled[counter][0])+", "+str(app.compiled[counter][1])+", "
        else:
            app.polygon = app.polygon + str(app.compiled[counter][0])+", "+str(app.compiled[counter][1])+")"
        
        counter += 1
    print(app.polygon)

def onMousePress(mouseX,mouseY):
    app.compiled.append([mouseX,mouseY])

def onKeyPress(key):
    if key == 'r':
        app.compiled = []
        
    if key == 'p':
        comp()
    if key == 'x':
        polycomp()
