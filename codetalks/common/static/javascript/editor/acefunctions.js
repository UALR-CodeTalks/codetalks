function outf(text)
{
	document.getElementById("output").innerHTML += text;
}
function builtinRead(x)
{
	if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
	{
		throw "File not found: '" + x + "'";
	}
	return Sk.builtinFiles["files"][x];
}
function runit()
{
	var program = editor.getSession().getValue();
	var output = document.getElementById("output")
	output.innerHTML = '';
	Sk.canvas = "mycanvas";
	Sk.pre = "output";
	Sk.configure({output:outf, read:builtinRead});
	try
	{
		eval(Sk.importMainWithBody("<stdin>", false, program));
	}
	catch(e)
	{
		alert(e.toString())
	}
}
