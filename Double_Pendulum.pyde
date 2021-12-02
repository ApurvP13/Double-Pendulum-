r1 = 200
r2 = 200
m1 =40
m2 = 40
a1 = PI/2
a2 = PI/4
a1_v =0.01
a2_v = 0.01
#a1_a = 0.01
#a2_a = -0.001
g =1
px2 = -1
py2 = -1
px1 = -1
py1 = -1
cx = 0
xy = 0
canvas = None

def setup():
    global cx,  cy
    size(900,600)
    cx = width/2
    cy = 50
    global canvas
    canvas = createGraphics(1000,1000)
    canvas.beginDraw()
    canvas.background(0)
    canvas.endDraw()
    
def draw():
    global a1
    global a2
    global canvas
    global a1_v, a2_v, g, px2,py2 , cx, cy, px1, py1
    #background(255)
    
    num1 = -g * (2 * m1 + m2) * sin(a1)
    num2 = -m2 * g * sin(a1-2*a2)
    num3 = -2*sin(a1-a2)*m2
    num4 = a2_v*a2_v*r2 + a1_v*a1_v*cos(a1-a2)
    den = r1 * (2*m1 + m2 -m2*cos(2*a1 - 2*a2))
    
    num5 = 2*sin(a1-a2)
    num6 = (a1_v*a1_v*r1*(m1+m2))
    num7 = g * (m1 + m2) * cos(a1)
    num8 = a2_v*a2_v*r2*cos(a1-a2)
    den2 = r2 * (2*m1 + m2 -m2*cos(2*a1 - 2*a2))
    
    
    image(canvas,0,0)
    stroke(255,255,255)
    strokeWeight(2)
    
    translate(cx,cy)
    
    x1 = r1 * sin(a1)
    y1 = r1 * cos(a1)
    
    x2 = x1+ r2 * sin(a2)
    y2 = y1 + r2 * cos(a2)
    
    line(0,0,x1,y1)
    fill(255,0,0)
    #noStroke()
    circle(x1,y1,m1)
    
    line(x1,y1,x2,y2)
    fill(0,0,255)
    circle(x2,y2,m2)
    
    a1_a = (num1 + num2 + num3*num4) / den
    a2_a = (num5*(num6 + num7 + num8))/den2
    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v
    
    a1_v *= 0.999
    a2_v *= 0.999
   
    
    canvas.beginDraw()
    canvas.translate(cx,cy)
    canvas.strokeWeight(1)
    canvas.stroke(21,244,238)
    if(frameCount >1):
        canvas.line(px2, py2,x2,y2)
        canvas.line(px1,py1,x1,y1)
    canvas.endDraw()
    
    px2 = x2
    py2 = y2
    
    px1 = x1
    py1 = y1
    
