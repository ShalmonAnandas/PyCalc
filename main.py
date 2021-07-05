import wx 
import calc_gui
import os 



class CalcFrame(calc_gui.MyFrame1): 
    def __init__(self,parent): 
        calc_gui.MyFrame1.__init__(self,parent)


    
    def clear_everything( self, event ):
        self.input_box.SetValue("")

    def backspace( self, event ):
        eq = self.input_box.GetValue()
        eqErase = eq[:-1]
        self.input_box.SetValue(eqErase)

    def input_divide( self, event ):
        x = str(self.input_box.GetValue())
        y = x.split(" / ")
        if len(y) == 1:
            self.input_box.AppendText(" / ")
        else:
            self.input_box.SetValue(str(float(y[0]) / float(y[1])))
            self.input_box.AppendText(" / ")

    def input_multiply( self, event ):
        x = str(self.input_box.GetValue())
        y = x.split(" * ")
        if len(y) == 1:
            self.input_box.AppendText(" * ")
        else:
            self.input_box.SetValue(str(float(y[0]) * float(y[1])))
            self.input_box.AppendText(" * ")

    def input_add( self, event ):
        x = str(self.input_box.GetValue())
        y = x.split(" + ")
        if len(y) == 1:
            self.input_box.AppendText(" + ")
        else:
            self.input_box.SetValue(str(float(y[0]) + float(y[1])))
            self.input_box.AppendText(" + ")

    def input_subtract( self, event ):
        x = str(self.input_box.GetValue())
        y = x.split(" - ")
        if len(y) == 1:
            self.input_box.AppendText(" - ")
        else:
            self.input_box.SetValue(str(float(y[0]) - float(y[1])))
            self.input_box.AppendText(" - ")

    def input_1( self, event ):
        self.input_box.AppendText("1")

    def input_2( self, event ):
        self.input_box.AppendText("2")

    def input_3( self, event ):
        self.input_box.AppendText("3")

    def input_4( self, event ):
        self.input_box.AppendText("4")

    def input_5( self, event ):
        self.input_box.AppendText("5")

    def input_6( self, event ):
        self.input_box.AppendText("6")

    def input_7( self, event ):
        self.input_box.AppendText("7")

    def input_8( self, event ):
        self.input_box.AppendText("8")

    def input_9( self, event ):
        self.input_box.AppendText("9")

    def input_0( self, event ):
        self.input_box.AppendText("0")

    def input_decimal( self, event ):
        self.input_box.AppendText(".")

    def isequal( self, event ):
        x = str(self.input_box.GetValue())
        y = x.split(" + ")
        if len(y) == 2:
            self.input_box.SetValue(str((float(y[0]) + float(y[1]))))
        else:
            pass
        y = x.split(" - ")
        if len(y) == 2:
            self.input_box.SetValue(str((float(y[0]) - float(y[1]))))
        else:
            pass
        y = x.split(" * ")
        if len(y) == 2:
            self.input_box.SetValue(str((float(y[0]) * float(y[1]))))
        else:
            pass
        y = x.split(" / ")
        if len(y) == 2:
            self.input_box.SetValue(str((float(y[0]) / float(y[1]))))
        else:
            pass
        
    
		


app = wx.App(False) 
frame = CalcFrame(None) 
frame.Show(True) 

app.MainLoop() 
