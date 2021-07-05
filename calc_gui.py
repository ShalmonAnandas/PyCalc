# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.input_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 270,60 ), 0 )
		self.input_box.SetFont( wx.Font( 33, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gbSizer1.Add( self.input_box, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )

		self.ceButton = wx.Button( self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.ceButton, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.backspaceButton = wx.Button( self, wx.ID_ANY, u"Backspace", wx.DefaultPosition, wx.Size( 130,60 ), 0 )
		gbSizer1.Add( self.backspaceButton, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.divideButton = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.divideButton, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.oneButton = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.oneButton, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.twoButton = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.twoButton, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.threeButton = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.threeButton, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.addButton = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.addButton, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.fourButton = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.fourButton, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.fiveButton = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.fiveButton, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.sixButton = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.sixButton, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.subtractButton = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.subtractButton, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.sevenButton = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.sevenButton, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.eightButton = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.eightButton, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.nineButton = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.nineButton, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.multiplyButton = wx.Button( self, wx.ID_ANY, u"*", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.multiplyButton, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.isequalButton = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.isequalButton, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.zeroButton = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 130,60 ), 0 )
		gbSizer1.Add( self.zeroButton, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.decimalButton = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		gbSizer1.Add( self.decimalButton, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()
		gbSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.ceButton.Bind( wx.EVT_BUTTON, self.clear_everything )
		self.backspaceButton.Bind( wx.EVT_BUTTON, self.backspace )
		self.divideButton.Bind( wx.EVT_BUTTON, self.input_divide )
		self.oneButton.Bind( wx.EVT_BUTTON, self.input_1 )
		self.twoButton.Bind( wx.EVT_BUTTON, self.input_2 )
		self.threeButton.Bind( wx.EVT_BUTTON, self.input_3 )
		self.addButton.Bind( wx.EVT_BUTTON, self.input_add )
		self.fourButton.Bind( wx.EVT_BUTTON, self.input_4 )
		self.fiveButton.Bind( wx.EVT_BUTTON, self.input_5 )
		self.sixButton.Bind( wx.EVT_BUTTON, self.input_6 )
		self.subtractButton.Bind( wx.EVT_BUTTON, self.input_subtract )
		self.sevenButton.Bind( wx.EVT_BUTTON, self.input_7 )
		self.eightButton.Bind( wx.EVT_BUTTON, self.input_8 )
		self.nineButton.Bind( wx.EVT_BUTTON, self.input_9 )
		self.multiplyButton.Bind( wx.EVT_BUTTON, self.input_multiply )
		self.isequalButton.Bind( wx.EVT_BUTTON, self.isequal )
		self.zeroButton.Bind( wx.EVT_BUTTON, self.input_0 )
		self.decimalButton.Bind( wx.EVT_BUTTON, self.input_decimal )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clear_everything( self, event ):
		event.Skip()

	def backspace( self, event ):
		event.Skip()

	def input_divide( self, event ):
		event.Skip()

	def input_1( self, event ):
		event.Skip()

	def input_2( self, event ):
		event.Skip()

	def input_3( self, event ):
		event.Skip()

	def input_add( self, event ):
		event.Skip()

	def input_4( self, event ):
		event.Skip()

	def input_5( self, event ):
		event.Skip()

	def input_6( self, event ):
		event.Skip()

	def input_subtract( self, event ):
		event.Skip()

	def input_7( self, event ):
		event.Skip()

	def input_8( self, event ):
		event.Skip()

	def input_9( self, event ):
		event.Skip()

	def input_multiply( self, event ):
		event.Skip()

	def isequal( self, event ):
		event.Skip()

	def input_0( self, event ):
		event.Skip()

	def input_decimal( self, event ):
		event.Skip()


