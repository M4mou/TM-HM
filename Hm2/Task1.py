from manim import *
from math import *
from sympy import symbols, nonlinsolve
omega = 1
phi = 52
a = 32
b = 4
c = 39
d = 19
e = 32
O1A = 12
O2D = 32
O3E = 18
AB = 46
AD = 29
GH = 14
DE = 53
GF = 25
FH = 14
O4G = 20
class simulation2(Scene):
 
   

    def construct(self):
        def deriv(f,x):
            h = 10**-4
            return (f(x+h) - f(h)) / h
        def xA(t):
            return O1A * cos(omega * t + phi)
        def yA(t):
            return O1A * sin(omega * t + phi)
        def xB(t):
            return 0
        def yB(t):
            xa = xA(t)
            ya = yA(t)
            x, y= symbols("x, y",real=True)
            system  = [(x-xa)**2 + (y - ya)**2 - AB**2 , x]
            solution = nonlinsolve(system,[x, y])
            return max(solution.args[1][1].evalf(),solution.args[0][1].evalf())
        def xC(t):
            xa = xA(t)
            xb = xB(t)
            return (xb - xa) * 2/ 3 + xa
        
        def yC(t):
            ya = yA(t)
            yb = yB(t)
            return (yb - ya) * 2/ 3 + ya
        
        def xD(t):
            xa = xA(t)
            ya = yA(t)
            x, y= symbols("x, y",real=True)
            xo = a + b
            yo = -d
            system  = [(x-xa)**2 + (y - ya)**2 - AD**2 , (x-xo)**2 + (y - yo)**2 - O2D**2 ]
            solution = nonlinsolve(system,[x, y])
            if(solution.args[1][1].evalf() > solution.args[0][1].evalf()):
                return solution.args[1][0].evalf()
            else:
                return solution.args[0][0].evalf()
            
        def yD(t):
            xa = xA(t)
            ya = yA(t)
            x, y= symbols("x, y",real=True)
            xo = a + b
            yo = -d
            system  = [(x-xa)**2 + (y - ya)**2 - AD**2 , (x-xo)**2 + (y - yo)**2 - O2D**2 ]
            solution = nonlinsolve(system,[x, y])
            return max(solution.args[1][1].evalf(),solution.args[0][1].evalf())
        
        def xE(t):
            xd = xD(t)
            yd = yD(t)
            x, y= symbols("x, y",real=True)
            xo = a + b+c
            yo = e
            system  = [(x-xd)**2 + (y - yd)**2 - DE**2 , (x-xo)**2 + (y - yo)**2 - O3E**2 ]
            solution = nonlinsolve(system,[x, y])
            if(solution.args[1][1].evalf() > solution.args[0][1].evalf()):
                return solution.args[1][0].evalf()
            else:
                return solution.args[0][0].evalf()
            
        def yE(t):
            xd = xD(t)
            yd = yD(t)
            x, y= symbols("x, y",real=True)
            xo = a + b+c
            yo = e
            system  = [(x-xd)**2 + (y - yd)**2 - DE**2 , (x-xo)**2 + (y - yo)**2 - O3E**2 ]
            solution = nonlinsolve(system,[x, y])
            if(solution.args[1][1].evalf() > solution.args[0][1].evalf()):
                return solution.args[1][1].evalf()
            else:
                return solution.args[0][1].evalf()
            
        def xF(t):
            xd = xD(t)
            xe = xE(t)
            return (xe - xd) * 3/ 5 + xd
        
        def yF(t):
            yd = yD(t)
            ye = yE(t)
            return (ye - yd) * 3/ 5 + yd
        
        def xG(t):
            xf = xF(t)
            yf = yF(t)
            x, y= symbols("x, y",real=True)
            xo = a 
            yo = e
            system  = [(x-xf)**2 + (y - yf)**2 - GF**2 , (x-xo)**2 + (y - yo)**2 - O4G**2 ]
            solution = nonlinsolve(system,[x, y])
            if(solution.args[1][1].evalf() > solution.args[0][1].evalf()):
                return solution.args[1][0].evalf()
            else:
                return solution.args[0][0].evalf()
        
        def yG(t):
            xf = xF(t)
            yf = yF(t)
            x, y= symbols("x, y",real=True)
            xo = a 
            yo = e
            system  = [(x-xf)**2 + (y - yf)**2 - GF**2 , (x-xo)**2 + (y - yo)**2 - O4G**2 ]
            solution = nonlinsolve(system,[x, y])
            if(solution.args[1][1].evalf() > solution.args[0][1].evalf()):
                return solution.args[1][1].evalf()
            else:
                return solution.args[0][1].evalf()
        
        def xH(t):
            xf = xF(t)
            yf = yF(t)
            x, y= symbols("x, y",real=True)
            xo = xG(t) 
            yo = yG(t)
            system  = [(x-xf)**2 + (y - yf)**2 - FH**2 , (x-xo)**2 + (y - yo)**2 - GH**2 ]
            solution = nonlinsolve(system,[x, y])
            if(solution.args[1][1].evalf() > solution.args[0][1].evalf()):
                return solution.args[1][0].evalf()
            else:
                return solution.args[0][0].evalf()
        
        def yH(t):
            xf = xF(t)
            yf = yF(t)
            x, y= symbols("x, y",real=True)
            xo = xG(t) 
            yo = yG(t)
            system  = [(x-xf)**2 + (y - yf)**2 - FH**2 , (x-xo)**2 + (y - yo)**2 - GH**2 ]
            solution = nonlinsolve(system,[x, y])
            if(solution.args[1][1].evalf() > solution.args[0][1].evalf()):
                return solution.args[1][1].evalf()
            else:
                return solution.args[0][1].evalf()

        ax = Axes(
            x_range=[-20, 100,10], y_range=[-30, 100, 10], axis_config={"include_tip": False},
            x_length=12,y_length= 7
        ).add_coordinates()
        labels = ax.get_axis_labels(x_label="x", y_label="y")

        t = ValueTracker(0)

        initial_point = [ax.coords_to_point(xA(t.get_value()), yB((t.get_value())))]

        textA = Text("A",font_size=20,color=RED)
        textB = Text("B",font_size=20,color=GREEN)
        textC = Text("C",font_size=20,color=BLUE)
        textD = Text("D",font_size=20,color=YELLOW)
        textE = Text("E",font_size=20,color=ORANGE)
        textF = Text("E",font_size=20,color=LIGHT_BROWN)
        textH = Text("H",font_size=20,color=PURPLE)
        textG = Text("E",font_size=20,color=PINK)

        textO1 = Text("O1",font_size=20,color=WHITE)
        textO2 = Text("O2",font_size=20,color=WHITE)
        textO3 = Text("O3",font_size=20,color=WHITE)
        textO4 = Text("O4",font_size=20,color=WHITE)

        dotA = Dot(point=initial_point,radius = 0.08,color=RED)
        dotB = Dot(point=initial_point,radius = 0.08,color=GREEN)
        dotC = Dot(point=initial_point,radius = 0.08,color=BLUE)
        dotD = Dot(point=initial_point,radius = 0.08,color=YELLOW)
        dotE = Dot(point=initial_point,radius = 0.08,color=ORANGE)
        dotF = Dot(point=initial_point,radius = 0.08,color=LIGHT_BROWN)
        dotH = Dot(point=initial_point,radius = 0.08,color=PURPLE)
        dotG = Dot(point=initial_point,radius = 0.08,color=PINK)

        dotO1 = Dot(point = [ax.coords_to_point(0,0)],color = WHITE)
        dotO2 = Dot(point = [ax.coords_to_point(a+b,-d)],color = WHITE)
        dotO3 = Dot(point = [ax.coords_to_point(a+b+c,e)],color = WHITE)
        dotO4 = Dot(point = [ax.coords_to_point(a,e)],color = WHITE)

        textO1.next_to(dotO1)
        textO2.next_to(dotO2)
        textO3.next_to(dotO3)
        textO4.next_to(dotO4)

        lineAB = Line(start=dotA.get_center(),end=dotB.get_center())
        lineAO1 = Line(start=dotA.get_center(),end=dotO1.get_center())
        lineAD = Line(start=dotA.get_center(),end=dotD.get_center())
        lineDO2 = Line(start=dotD.get_center(),end=dotO2.get_center())
        lineDE = Line(start=dotD.get_center(),end=dotE.get_center())
        lineEO3 = Line(start=dotE.get_center(),end=dotO3.get_center())
        lineGO4 = Line(start=dotG.get_center(),end=dotO4.get_center())
        lineFG = Line(start=dotG.get_center(),end=dotO4.get_center())
        lineGH = Line(start=dotG.get_center(),end=dotO4.get_center())
        lineFH = Line(start=dotG.get_center(),end=dotO4.get_center())

        av = Vector([1,1],buff = 0,stroke_width = 3,max_tip_length_to_length_ratio = 0.1,max_stroke_width_to_length_ratio=100)
        def pointupdater(x,func1,func2):    
            val = t.get_value()
            x.move_to(ax.c2p(func1(val), func2(val)))

        def aupdater(x):
            pointupdater(x,xA,yA)
            textA.next_to(x)
            lineAO1.put_start_and_end_on(dotA.get_center(),dotO1.get_center())
          
        def avupdater(x):
            val = t.get_value()
            end = Dot(ax.c2p(deriv(xA,val),deriv(yA,val)) + dotA.get_center())
            av.put_start_and_end_on(dotA.get_center(),end.get_center())
        def bUpdater(x):
            pointupdater(x,xB,yB)
            textB.next_to(x)

        
        def cUpdater(x):
            pointupdater(x,xC,yC)
            textC.next_to(x)

        def fUpdater(x):
            pointupdater(x,xF,yF)
            textF.next_to(x)

        def dUpdater(x):
            pointupdater(x,xD,yD)
            textD.next_to(x)
            lineDO2.put_start_and_end_on(dotD.get_center(),dotO2.get_center())
            lineAD.put_start_and_end_on(dotD.get_center(),dotA.get_center())
        def gUpdater(x):
            pointupdater(x,xG,yG)
            textG.next_to(x)
            lineGO4.put_start_and_end_on(dotG.get_center(),dotO4.get_center())

        
        def hUpdater(x):
            pointupdater(x,xH,yH)
            textH.next_to(x)
            lineFG.put_start_and_end_on(dotF.get_center(),dotG.get_center())
            lineGH.put_start_and_end_on(dotG.get_center(),dotH.get_center())
            lineFH.put_start_and_end_on(dotF.get_center(),dotH.get_center())

        def eUpdater(x):
            pointupdater(x,xE,yE)
            textE.next_to(x)
            lineDE.put_start_and_end_on(dotD.get_center(),dotE.get_center())
            lineEO3.put_start_and_end_on(dotE.get_center(),dotO3.get_center())
    
        def lineUpdater(x):
            x.put_start_and_end_on(dotA.get_center(),dotB.get_center())
        
        dotA.add_updater(aupdater)
        dotB.add_updater(bUpdater)
        dotC.add_updater(cUpdater)
        av.add_updater(avupdater)
        dotD.add_updater(dUpdater)
        dotE.add_updater(eUpdater)
        dotF.add_updater(fUpdater)
        dotG.add_updater(gUpdater)
        dotH.add_updater(hUpdater)
        lineAB.add_updater(lineUpdater)

        self.add(ax, lineFH,lineGH,lineFH,labels,dotF,dotG,dotH,lineGO4, dotE,dotO3,lineEO3,lineDE,textO3,textE,dotA,dotB,textA,textB,lineAB,dotC,textC,dotO1,lineAO1,textO1,dotD,lineDO2,lineAD,dotO2,textO2)
        self.play(t.animate.set_value(10),run_time = 5)
 
        self.wait()