# lough model pass 3



# ----------------------------------------------

# Script Recorded by ANSYS Electronics Desktop Version 2020.1.0

# 20:04:29  7 09, 2021

# ----------------------------------------------

import ScriptEnv

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

oDesktop.RestoreWindow()



# Open aedt file

oDesktop.OpenProject("D:/script2/ML_aedt/ML_v2.aedt")



# Make project

oProject = oDesktop.SetActiveProject("ML_v2")

oProject.InsertDesign("HFSS", "HFSS_ML_v1", "DrivenTerminal", "")

oDesign = oProject.SetActiveDesign("HFSS_ML_v1")

#oDesign.RenameDesignInstance("HFSSDesign1", "HFSS_name") # project name



# Make setup

#oDesign.SetSolutionType("DrivenTerminal", False)

oModule = oDesign.GetModule("AnalysisSetup")

oModule.InsertSetup("HfssDriven", 

	[

		"NAME:Setup1",

		"AdaptMultipleFreqs:="	, False,

		"Frequency:="		, "40kHz",

		"MaxDeltaE:="		, 0.1,

		"MaximumPasses:="	, 5,

		"MinimumPasses:="	, 5,

		"MinimumConvergedPasses:=", 1,

		"PercentRefinement:="	, 30,

		"IsEnabled:="		, True,

		[

			"NAME:MeshLink",

			"ImportMesh:="		, False

		],

		"BasisOrder:="		, 0,

		"DoLambdaRefine:="	, False,

		"DoMaterialLambda:="	, True,

		"SetLambdaTarget:="	, False,

		"Target:="		, 0.3333,

		"UseMaxTetIncrease:="	, False,

		"UseDomains:="		, False,

		"UseIterativeSolver:="	, False,

		"SaveRadFieldsOnly:="	, False,

		"SaveAnyFields:="	, True,

		"IESolverType:="	, "Auto",

		"LambdaTargetForIESolver:=", 0.15,

		"UseDefaultLambdaTgtForIESolver:=", True,

		"IE Solver Accuracy:="	, "Balanced"

	])



# Set variable

oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:air",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "199mm"

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:l1",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "16mm"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:l2",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "85mm"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:l3",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "l1"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:h1",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "81mm"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:d1",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "6.54mm"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:move_tx",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "6.54mm + 3mm"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:move_rx",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "6.54mm + 3mm"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:w1",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "39mm"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:space1",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "9mm"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:space2",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "48mm"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:Num",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "6"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:offset_tx",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "3/2*move_tx"

					

				]

			]

		]

	])



	

oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:offset_rx",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "6/2*move_tx"

					

				]

			]

		]

	])





oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:N1",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "3"

					

				]

			]

		]

	])



oDesign.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:LocalVariableTab",

			[

				"NAME:PropServers", 

				"LocalVariables"

			],

			[

				"NAME:NewProps",

				[

					"NAME:N2",

					"PropType:="		, "VariableProp",

					"UserDef:="		, True,

					"Value:="		, "6"

					

				]

			]

		]

	])



# Make boundary

oEditor = oDesign.SetActiveEditor("3D Modeler")

oEditor.CreateBox(

	[

		"NAME:BoxParameters",

		"XPosition:="		, "-air",

		"YPosition:="		, "-air",

		"ZPosition:="		, "-air",

		"XSize:="		, "2*air",

		"YSize:="		, "2*air",

		"ZSize:="		, "2*air"

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Air",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 1,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"vacuum\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])

oModule = oDesign.GetModule("BoundarySetup")

oModule.AssignRadiation(

	[

		"NAME:Rad1",

		"Objects:="		, ["Air"],

		"IsFssReference:="	, False,

		"IsForPML:="		, False

	])



# Make core

oEditor.CreateBox(

	[

		"NAME:BoxParameters",

		"XPosition:="		, "-w1/2",

		"YPosition:="		, "-2*l1-l2",

		"ZPosition:="		, "-l3-h1/2",

		"XSize:="		, "w1",

		"YSize:="		, "4*l1+2*l2",

		"ZSize:="		, "2*l3+h1"

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Core",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"ferrite_LP3_per3500\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])

oEditor.CreateBox(

	[

		"NAME:BoxParameters",

		"XPosition:="		, "-w1/2",

		"YPosition:="		, "-l1",

		"ZPosition:="		, "-h1/2",

		"XSize:="		, "w1",

		"YSize:="		, "-l2",

		"ZSize:="		, "h1"

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Core_sub1",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"ferrite_LP3_per3500\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])

oEditor.CreateBox(

	[

		"NAME:BoxParameters",

		"XPosition:="		, "-w1/2",

		"YPosition:="		, "l1",

		"ZPosition:="		, "-h1/2",

		"XSize:="		, "w1",

		"YSize:="		, "l2",

		"ZSize:="		, "h1"

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Core_sub2",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"ferrite_LP3_per3500\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])

oEditor.Subtract(

	[

		"NAME:Selections",

		"Blank Parts:="		, "Core",

		"Tool Parts:="		, "Core_sub1,Core_sub2"

	], 

	[

		"NAME:SubtractParameters",

		"KeepOriginals:="	, False

	])





# Tx

oEditor.CreatePolyline(

	[

		"NAME:PolylineParameters",

		"IsPolylineCovered:="	, True,

		"IsPolylineClosed:="	, False,

		[

			"NAME:PolylinePoints",

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space1",

				"Y:="			, "-l1-space1",

				"Z:="			, "0mm"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2",

				"Y:="			, "-l1-space1",

				"Z:="			, "0mm"

			],

			[

				"NAME:PLPoint",

				"X:="			, "-w1/2-space1",

				"Y:="			, "-l1-space1",

				"Z:="			, "-0*move_tx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "-w1/2-space1",

				"Y:="			, "l1+space1",

				"Z:="			, "-1/3*move_tx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space1",

				"Y:="			, "l1+space1",

				"Z:="			, "-2/3*move_tx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space1",

				"Y:="			, "-l1",

				"Z:="			, "-3/3*move_tx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space1",

				"Y:="			, "-l1-space1",

				"Z:="			, "-3/3*move_tx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2",

				"Y:="			, "-l1-space1",

				"Z:="			, "-3/3*move_tx"

			]

		],

		[

			"NAME:PolylineSegments",

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 0,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 1,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 2,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 3,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 4,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 5,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 6,

				"NoOfPoints:="		, 2

			]

		],

		[

			"NAME:PolylineXSection",

			"XSectionType:="	, "None",

			"XSectionOrient:="	, "Auto",

			"XSectionWidth:="	, "0mm",

			"XSectionTopWidth:="	, "0mm",

			"XSectionHeight:="	, "0mm",

			"XSectionNumSegments:="	, "0",

			"XSectionBendType:="	, "Corner"

		]

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Tx1",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])



oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DCmdTab",

			[

				"NAME:PropServers", 

				"Tx1:CreatePolyline:1"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Type",

					"Value:="		, "Circle"

				],

				[

					"NAME:Number of Segments",

					"Value:="		, "Num"

				],

				[

					"NAME:Width/Diameter",

					"Value:="		, "d1"

				]

			]

		]

	])



oEditor.Copy(

	[

		"NAME:Selections",

		"Selections:="		, "Tx1"

	])	



oEditor.Paste()
oEditor.Move(
   [
    "NAME:Selections",
    "Selections:="		, "Tx2",
    "NewPartsModelFlag:="	, "Model"
   ],
   [
    "NAME:TranslateParameters",
    "TranslateVectorX:="	, "0",
    "TranslateVectorY:="	, "0",
    "TranslateVectorZ:="	, "-1*move_tx+offset_tx"
   ])
oEditor.Paste()
oEditor.Move(
   [
    "NAME:Selections",
    "Selections:="		, "Tx3",
    "NewPartsModelFlag:="	, "Model"
   ],
   [
    "NAME:TranslateParameters",
    "TranslateVectorX:="	, "0",
    "TranslateVectorY:="	, "0",
    "TranslateVectorZ:="	, "-2*move_tx+offset_tx"
   ])




	

oEditor.Move(

	[

		"NAME:Selections",

		"Selections:="		, "Tx1",

		"NewPartsModelFlag:="	, "Model"

	], 

	[

		"NAME:TranslateParameters",

		"TranslateVectorX:="	, "0",

		"TranslateVectorY:="	, "0",

		"TranslateVectorZ:="	, "offset_tx"

	])





oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DPolylineTab",

			[

				"NAME:PropServers", 

				"Tx1:CreatePolyline:2:Segment0"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Point1",

					"X:="			, "w1/2+space1+3mm",

					"Y:="			, "-l1-space1",

					"Z:="			, "0mm"

				]

			]

		]

	])





oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DPolylineTab",

			[

				"NAME:PropServers", 

				"Tx3:CreatePolyline:2:Segment6"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Point2",

					"X:="			, "w1/2+space1+5mm",

					"Y:="			, "-l1-space1",

					"Z:="			, "-4/4*move_tx"

				]

			]

		]

	])



oEditor.CreatePolyline(

	[

		"NAME:PolylineParameters",

		"IsPolylineCovered:="	, True,

		"IsPolylineClosed:="	, False,

		[

			"NAME:PolylinePoints",

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space1+0mm",

				"Y:="			, "-l1-space1",

				"Z:="			, "offset_tx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space1+5mm",

				"Y:="			, "-l1-space1",

				"Z:="			, "offset_tx"

			]

		],

		[

			"NAME:PolylineSegments",

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 0,

				"NoOfPoints:="		, 2

			]

		],

		[

			"NAME:PolylineXSection",

			"XSectionType:="	, "None",

			"XSectionOrient:="	, "Auto",

			"XSectionWidth:="	, "0mm",

			"XSectionTopWidth:="	, "0mm",

			"XSectionHeight:="	, "0mm",

			"XSectionNumSegments:="	, "0",

			"XSectionBendType:="	, "Corner"

		]

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Tx_in",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])

oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DCmdTab",

			[

				"NAME:PropServers", 

				"Tx_in:CreatePolyline:1"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Type",

					"Value:="		, "Rectangle"

				],

				[

					"NAME:Width/Diameter",

					"Value:="		, "d1"

				],

				[

					"NAME:Height",

					"Value:="		, "d1"

				]

			]

		]

	])



oEditor.CreatePolyline(

	[

		"NAME:PolylineParameters",

		"IsPolylineCovered:="	, True,

		"IsPolylineClosed:="	, False,

		[

			"NAME:PolylinePoints",

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space1+0mm",

				"Y:="			, "-l1-space1",

				"Z:="			, "offset_tx-3*move_tx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space1+5mm",

				"Y:="			, "-l1-space1",

				"Z:="			, "offset_tx-3*move_tx"

			]

		],

		[

			"NAME:PolylineSegments",

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 0,

				"NoOfPoints:="		, 2

			]

		],

		[

			"NAME:PolylineXSection",

			"XSectionType:="	, "None",

			"XSectionOrient:="	, "Auto",

			"XSectionWidth:="	, "0mm",

			"XSectionTopWidth:="	, "0mm",

			"XSectionHeight:="	, "0mm",

			"XSectionNumSegments:="	, "0",

			"XSectionBendType:="	, "Corner"

		]

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Tx_out",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])

oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DCmdTab",

			[

				"NAME:PropServers", 

				"Tx_out:CreatePolyline:1"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Type",

					"Value:="		, "Rectangle"

				],

				[

					"NAME:Width/Diameter",

					"Value:="		, "d1"

				],

				[

					"NAME:Height",

					"Value:="		, "d1"

				]

			]

		]

	])



oEditor.Unite(

	[

		"NAME:Selections",

		"Selections:="		, "Tx_in,Tx_out,Tx1,Tx2,Tx3"

	], 

	[

		"NAME:UniteParameters",

		"KeepOriginals:="	, False

	])





# Rx

oEditor.CreatePolyline(

	[

		"NAME:PolylineParameters",

		"IsPolylineCovered:="	, True,

		"IsPolylineClosed:="	, False,

		[

			"NAME:PolylinePoints",

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space2",

				"Y:="			, "-l1-space2",

				"Z:="			, "0mm"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2",

				"Y:="			, "-l1-space2",

				"Z:="			, "0mm"

			],

			[

				"NAME:PLPoint",

				"X:="			, "-w1/2-space2",

				"Y:="			, "-l1-space2",

				"Z:="			, "-0*move_rx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "-w1/2-space2",

				"Y:="			, "l1+space2",

				"Z:="			, "-1/3*move_rx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space2",

				"Y:="			, "l1+space2",

				"Z:="			, "-2/3*move_rx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space2",

				"Y:="			, "-l1",

				"Z:="			, "-3/3*move_rx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space2",

				"Y:="			, "-l1-space2",

				"Z:="			, "-3/3*move_rx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2",

				"Y:="			, "-l1-space2",

				"Z:="			, "-3/3*move_rx"

			]

		],

		[

			"NAME:PolylineSegments",

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 0,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 1,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 2,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 3,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 4,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 5,

				"NoOfPoints:="		, 2

			],

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 6,

				"NoOfPoints:="		, 2

			]

		],

		[

			"NAME:PolylineXSection",

			"XSectionType:="	, "None",

			"XSectionOrient:="	, "Auto",

			"XSectionWidth:="	, "0mm",

			"XSectionTopWidth:="	, "0mm",

			"XSectionHeight:="	, "0mm",

			"XSectionNumSegments:="	, "0",

			"XSectionBendType:="	, "Corner"

		]

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Rx1",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])



oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DCmdTab",

			[

				"NAME:PropServers", 

				"Rx1:CreatePolyline:1"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Type",

					"Value:="		, "Circle"

				],

				[

					"NAME:Number of Segments",

					"Value:="		, "Num"

				],

				[

					"NAME:Width/Diameter",

					"Value:="		, "d1"

				]

			]

		]

	])



oEditor.Copy(

	[

		"NAME:Selections",

		"Selections:="		, "Rx1"

	])

	



oEditor.Paste()
oEditor.Move(
   [
    "NAME:Selections",
    "Selections:="		, "Rx2",
    "NewPartsModelFlag:="	, "Model"
   ],
   [
    "NAME:TranslateParameters",
    "TranslateVectorX:="	, "0",
    "TranslateVectorY:="	, "0",
    "TranslateVectorZ:="	, "-1*move_rx+offset_rx"
   ])
oEditor.Paste()
oEditor.Move(
   [
    "NAME:Selections",
    "Selections:="		, "Rx3",
    "NewPartsModelFlag:="	, "Model"
   ],
   [
    "NAME:TranslateParameters",
    "TranslateVectorX:="	, "0",
    "TranslateVectorY:="	, "0",
    "TranslateVectorZ:="	, "-2*move_rx+offset_rx"
   ])
oEditor.Paste()
oEditor.Move(
   [
    "NAME:Selections",
    "Selections:="		, "Rx4",
    "NewPartsModelFlag:="	, "Model"
   ],
   [
    "NAME:TranslateParameters",
    "TranslateVectorX:="	, "0",
    "TranslateVectorY:="	, "0",
    "TranslateVectorZ:="	, "-3*move_rx+offset_rx"
   ])
oEditor.Paste()
oEditor.Move(
   [
    "NAME:Selections",
    "Selections:="		, "Rx5",
    "NewPartsModelFlag:="	, "Model"
   ],
   [
    "NAME:TranslateParameters",
    "TranslateVectorX:="	, "0",
    "TranslateVectorY:="	, "0",
    "TranslateVectorZ:="	, "-4*move_rx+offset_rx"
   ])
oEditor.Paste()
oEditor.Move(
   [
    "NAME:Selections",
    "Selections:="		, "Rx6",
    "NewPartsModelFlag:="	, "Model"
   ],
   [
    "NAME:TranslateParameters",
    "TranslateVectorX:="	, "0",
    "TranslateVectorY:="	, "0",
    "TranslateVectorZ:="	, "-5*move_rx+offset_rx"
   ])




oEditor.Move(

	[

		"NAME:Selections",

		"Selections:="		, "Rx1",

		"NewPartsModelFlag:="	, "Model"

	], 

	[

		"NAME:TranslateParameters",

		"TranslateVectorX:="	, "0",

		"TranslateVectorY:="	, "0",

		"TranslateVectorZ:="	, "offset_rx"

	])





oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DPolylineTab",

			[

				"NAME:PropServers", 

				"Rx1:CreatePolyline:2:Segment0"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Point1",

					"X:="			, "w1/2+space2+5mm",

					"Y:="			, "-l1-space2",

					"Z:="			, "0mm"

				]

			]

		]

	])





oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DPolylineTab",

			[

				"NAME:PropServers", 

				"Rx6:CreatePolyline:2:Segment6"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Point2",

					"X:="			, "w1/2+space2+3mm",

					"Y:="			, "-l1-space2",

					"Z:="			, "-4/4*move_rx"

				]

			]

		]

	])



oEditor.CreatePolyline(

	[

		"NAME:PolylineParameters",

		"IsPolylineCovered:="	, True,

		"IsPolylineClosed:="	, False,

		[

			"NAME:PolylinePoints",

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space2+0mm",

				"Y:="			, "-l1-space2",

				"Z:="			, "offset_rx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space2+5mm",

				"Y:="			, "-l1-space2",

				"Z:="			, "offset_rx"

			]

		],

		[

			"NAME:PolylineSegments",

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 0,

				"NoOfPoints:="		, 2

			]

		],

		[

			"NAME:PolylineXSection",

			"XSectionType:="	, "None",

			"XSectionOrient:="	, "Auto",

			"XSectionWidth:="	, "0mm",

			"XSectionTopWidth:="	, "0mm",

			"XSectionHeight:="	, "0mm",

			"XSectionNumSegments:="	, "0",

			"XSectionBendType:="	, "Corner"

		]

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Rx_in",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])

oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DCmdTab",

			[

				"NAME:PropServers", 

				"Rx_in:CreatePolyline:1"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Type",

					"Value:="		, "Rectangle"

				],

				[

					"NAME:Width/Diameter",

					"Value:="		, "d1"

				],

				[

					"NAME:Height",

					"Value:="		, "d1"

				]

			]

		]

	])



oEditor.CreatePolyline(

	[

		"NAME:PolylineParameters",

		"IsPolylineCovered:="	, True,

		"IsPolylineClosed:="	, False,

		[

			"NAME:PolylinePoints",

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space2+0mm",

				"Y:="			, "-l1-space2",

				"Z:="			, "offset_rx-6*move_rx"

			],

			[

				"NAME:PLPoint",

				"X:="			, "w1/2+space2+5mm",

				"Y:="			, "-l1-space2",

				"Z:="			, "offset_rx-6*move_rx"

			]

		],

		[

			"NAME:PolylineSegments",

			[

				"NAME:PLSegment",

				"SegmentType:="		, "Line",

				"StartIndex:="		, 0,

				"NoOfPoints:="		, 2

			]

		],

		[

			"NAME:PolylineXSection",

			"XSectionType:="	, "None",

			"XSectionOrient:="	, "Auto",

			"XSectionWidth:="	, "0mm",

			"XSectionTopWidth:="	, "0mm",

			"XSectionHeight:="	, "0mm",

			"XSectionNumSegments:="	, "0",

			"XSectionBendType:="	, "Corner"

		]

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Rx_out",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])

oEditor.ChangeProperty(

	[

		"NAME:AllTabs",

		[

			"NAME:Geometry3DCmdTab",

			[

				"NAME:PropServers", 

				"Rx_out:CreatePolyline:1"

			],

			[

				"NAME:ChangedProps",

				[

					"NAME:Type",

					"Value:="		, "Rectangle"

				],

				[

					"NAME:Width/Diameter",

					"Value:="		, "d1"

				],

				[

					"NAME:Height",

					"Value:="		, "d1"

				]

			]

		]

	])



oEditor.Unite(

	[

		"NAME:Selections",

		"Selections:="		, "Rx_in,Rx_out,Rx1,Rx2,Rx3,Rx4,Rx5,Rx6"

	], 

	[

		"NAME:UniteParameters",

		"KeepOriginals:="	, False

	])







# ===========================================================================================

# Make Sheet

# ===========================================================================================



# 

oEditor.CreateRectangle(

	[

		"NAME:RectangleParameters",

		"IsCovered:="		, True,

		"XStart:="		, "w1/2+space1+5mm",

		"YStart:="		, "-l1-space1-d1/2",

		"ZStart:="		, "offset_tx-d1/2",

		"Width:="		, "d1",

		"Height:="		, "-3*move_tx+d1",

		"WhichAxis:="		, "X"

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Ter1_Rec1",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])



oEditor.CreateRectangle(

	[

		"NAME:RectangleParameters",

		"IsCovered:="		, True,

		"XStart:="		, "w1/2+space2+5mm",

		"YStart:="		, "-l1-space2-d1/2",

		"ZStart:="		, "offset_rx-d1/2",

		"Width:="		, "d1",

		"Height:="		, "-6*move_rx+d1",

		"WhichAxis:="		, "X"

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Ter2_Rec1",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])



oEditor.CreateRectangle(

	[

		"NAME:RectangleParameters",

		"IsCovered:="		, True,

		"XStart:="		, "w1/2+space1+5mm",

		"YStart:="		, "-l1-space1-d1/2",

		"ZStart:="		, "offset_tx-d1/2",

		"Width:="		, "d1",

		"Height:="		, "-1mm",

		"WhichAxis:="		, "X"

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Ter1_Rec2",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])



oEditor.CreateRectangle(

	[

		"NAME:RectangleParameters",

		"IsCovered:="		, True,

		"XStart:="		, "w1/2+space2+5mm",

		"YStart:="		, "-l1-space2-d1/2",

		"ZStart:="		, "offset_rx-d1/2",

		"Width:="		, "d1",

		"Height:="		, "-1mm",

		"WhichAxis:="		, "X"

	], 

	[

		"NAME:Attributes",

		"Name:="		, "Ter2_Rec2",

		"Flags:="		, "",

		"Color:="		, "(143 175 143)",

		"Transparency:="	, 0,

		"PartCoordinateSystem:=", "Global",

		"UDMId:="		, "",

		"MaterialValue:="	, "\"copper\"",

		"SurfaceMaterialValue:=", "\"\"",

		"SolveInside:="		, True,

		"IsMaterialEditable:="	, True,

		"UseMaterialAppearance:=", False,

		"IsLightweight:="	, False

	])



# ===========================================================================================

# Make Terminal

# ===========================================================================================





oModule = oDesign.GetModule("BoundarySetup")



oEditor = oDesign.SetActiveEditor("3D Modeler")

oFaceIDs1 = oEditor.GetFaceIDs("Ter1_Rec1")

oFaceIDs2 = oEditor.GetFaceIDs("Ter1_Rec2")

oFaceIDs3 = oEditor.GetFaceIDs("Ter2_Rec1")

oFaceIDs4 = oEditor.GetFaceIDs("Ter2_Rec2")



oModule.AutoIdentifyPorts(

	[

		"NAME:Faces", 

		oFaceIDs1[0]

	], False, 

	[

		"NAME:ReferenceConductors", 

		"Tx_in"

	], "1", True)

oModule.AssignTerminal(

	[

		"NAME:Ter1",

		"Objects:="		, ["Ter1_Rec2"],

		"ParentBndID:="		, "1",

		"TerminalResistance:="	, "50ohm"

	])

oModule.AutoIdentifyPorts(

	[

		"NAME:Faces", 

		oFaceIDs3[0]

	], False, 

	[

		"NAME:ReferenceConductors", 

		"Rx_in"

	], "2", True)

oModule.AssignTerminal(

	[

		"NAME:Ter2",

		"Objects:="		, ["Ter2_Rec2"],

		"ParentBndID:="		, "2",

		"TerminalResistance:="	, "50ohm"

	])









oModule = oDesign.GetModule("ReportSetup")



oProject.Save()

oDesign.Analyze("Setup1")



oModule.CreateReport(" Table 1", "Terminal Solution Data", "Data Table", "Setup1 : LastAdaptive", [], 

	[

		"Freq:="		, ["All"],

		"air:="			, ["Nominal"],

		"l1:="			, ["Nominal"],

		"l2:="			, ["Nominal"],

		"l3:="			, ["Nominal"],

		"h1:="			, ["Nominal"],

		"d1:="			, ["Nominal"],

		"w1:="			, ["Nominal"],

		"space1:="		, ["Nominal"],

		"space2:="		, ["Nominal"],

		"Num:="			, ["Nominal"]

	], 

	[

		"X Component:="		, "Freq",

		"Y Component:="		, ["(im(Zt(Ter1,Ter2))/2/pi/freq / sqrt(im(Zt(Ter1,Ter1))/2/pi/freq*im(Zt(Ter2,Ter2))/2/pi/freq))^2 * im(Zt(Ter1,Ter1))/2/pi/freq * 1e+3"]

	])

oModule.AddTraces(" Table 1", "Setup1 : LastAdaptive", [], 

	[

		"Freq:="		, ["All"],

		"air:="			, ["Nominal"],

		"l1:="			, ["Nominal"],

		"l2:="			, ["Nominal"],

		"l3:="			, ["Nominal"],

		"h1:="			, ["Nominal"],

		"d1:="			, ["Nominal"],

		"w1:="			, ["Nominal"],

		"space1:="		, ["Nominal"],

		"space2:="		, ["Nominal"],

		"Num:="			, ["Nominal"]

	], 

	[

		"X Component:="		, "Freq",

		"Y Component:="		, ["(im(Zt(Ter1,Ter2))/2/pi/freq / sqrt(im(Zt(Ter1,Ter1))/2/pi/freq*im(Zt(Ter2,Ter2))/2/pi/freq))^2 * im(Zt(Ter2,Ter2))/2/pi/freq * 1e+3"]

	])

oModule.AddTraces(" Table 1", "Setup1 : LastAdaptive", [], 

	[

		"Freq:="		, ["All"],

		"air:="			, ["Nominal"],

		"l1:="			, ["Nominal"],

		"l2:="			, ["Nominal"],

		"l3:="			, ["Nominal"],

		"h1:="			, ["Nominal"],

		"d1:="			, ["Nominal"],

		"w1:="			, ["Nominal"],

		"space1:="		, ["Nominal"],

		"space2:="		, ["Nominal"],

		"Num:="			, ["Nominal"]

	], 

	[

		"X Component:="		, "Freq",

		"Y Component:="		, ["(1 - (im(Zt(Ter1,Ter2))/2/pi/freq / sqrt(im(Zt(Ter1,Ter1))/2/pi/freq*im(Zt(Ter2,Ter2))/2/pi/freq))^2) * im(Zt(Ter1,Ter1))/2/pi/freq * 1e+6"]

	])

oModule.AddTraces(" Table 1", "Setup1 : LastAdaptive", [], 

	[

		"Freq:="		, ["All"],

		"air:="			, ["Nominal"],

		"l1:="			, ["Nominal"],

		"l2:="			, ["Nominal"],

		"l3:="			, ["Nominal"],

		"h1:="			, ["Nominal"],

		"d1:="			, ["Nominal"],

		"w1:="			, ["Nominal"],

		"space1:="		, ["Nominal"],

		"space2:="		, ["Nominal"],

		"Num:="			, ["Nominal"]

	], 

	[

		"X Component:="		, "Freq",

		"Y Component:="		, ["re(Zt(Ter1,Ter1))"]

	])

oModule.AddTraces(" Table 1", "Setup1 : LastAdaptive", [], 

	[

		"Freq:="		, ["All"],

		"air:="			, ["Nominal"],

		"l1:="			, ["Nominal"],

		"l2:="			, ["Nominal"],

		"l3:="			, ["Nominal"],

		"h1:="			, ["Nominal"],

		"d1:="			, ["Nominal"],

		"w1:="			, ["Nominal"],

		"space1:="		, ["Nominal"],

		"space2:="		, ["Nominal"],

		"Num:="			, ["Nominal"]

	], 

	[

		"X Component:="		, "Freq",

		"Y Component:="		, ["re(Zt(Ter2,Ter2))"]

	])



oProject.Save()

oDesign.Analyze("Setup1")

oModule.ExportToFile(" Table 1", "D:/script2/ML_v2_data/Data 1.csv", False)

#time.sleep(1)





#oEditor.Delete(

#	[

#		"NAME:Selections",

#		"Selections:="		, "Core,Tx_in,Rx_in,Tx_in_ObjectFromEdge1,Rx_in_ObjectFromEdge1"

#	])

#oModule = oDesign.GetModule("BoundarySetup")

#oModule.DeleteBoundaries(["Rad1"])

#oModule = oDesign.GetModule("AnalysisSetup")

#oModule.DeleteSetups(["Setup1"])



#oProject.Save()





oProject.DeleteDesign("HFSS_ML_v1")

#time.sleep(1)

oProject.Save()
