# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.1.0
# 20:04:29  7 09, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# Open aedt file
oDesktop.OpenProject("D:/transformer_2021/ML_v1.aedt")

# Make project
oProject = oDesktop.SetActiveProject("ML_v1")
oProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oDesign.RenameDesignInstance("HFSSDesign1", "HFSS_name") # project name

# Make setup
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "40kHz",
		"MaxDeltaE:="		, 0.1,
		"MaximumPasses:="	, 2,
		"MinimumPasses:="	, 1,
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
					"Value:="		, "300mm"
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
					"Value:="		, "10mm"
					
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
					"Value:="		, "50mm"
					
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
					"Value:="		, "10mm"
					
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
					"Value:="		, "50mm"
					
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
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "30mm"
					
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
		"Transparency:="	, 0,
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

# Tx1
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
				"Z:="			, "-1/4*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space1",
				"Y:="			, "l1+space1",
				"Z:="			, "-2/4*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space1",
				"Y:="			, "l1+space1",
				"Z:="			, "-3/4*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space1",
				"Y:="			, "-l1-space1",
				"Z:="			, "-4/4*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space1",
				"Z:="			, "-4/4*move_tx"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Circle",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Circle",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Circle",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Circle",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Circle",
				"StartIndex:="		, 4,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Circle",
				"StartIndex:="		, 5,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "d1",
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

oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Tx1"
	])

oEditor.Paste()

oEditor.Paste()

oEditor.Paste()

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
		"TranslateVectorZ:="	, "0mm"
	])

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
		"TranslateVectorZ:="	, "-1*move_tx"
	])

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
		"TranslateVectorZ:="	, "-2*move_tx"
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx4",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0",
		"TranslateVectorY:="	, "0",
		"TranslateVectorZ:="	, "-3*move_tx"
	])
