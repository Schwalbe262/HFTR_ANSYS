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
		"Name:="		, "Box1",
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
