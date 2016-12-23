
// This is the canvas context that gives us all the good stuff the canvas provides
//context = document.getElementById("canvas").getContext("2d");

var canvas = new fabric.Canvas("canvas", {
	isDrawingMode:true
});
var context = fabric.document.getElementById("canvas").getContext("2d");

// Here are our global variables
var lineObjects = []; // This is where we store the mouse movements that are then drawn by render()
var brushColor = "#000000"; // Current color
var brushShape = "round";
var brushSize = 5;
var mousePosOrig = [];

$("#canvas").mousedown(function(e) {
    // Gets the position of the mouse in relation to the canvas's size
    var X = e.pageX - this.offsetLeft; 
    var Y = e.pageY - this.offsetTop;
    mousePosOrig = [X, Y];
    addPoint(X, Y) // Adds the point object to the lineObjects array
});

$("#canvas").mousemove(function(e) {
    if(canvas.isDrawingMode) { // If the mouse is being held down then this will be called. It does the same thing as .mousedown(
        var X = e.pageX - this.offsetLeft;
        var Y = e.pageY - this.offsetTop;
        addPoint(X, Y)
    }
});

$("#canvas").on("mouseup mouseleave", function(e) { // These events will stop the mouse from drawing
    var X = e.pageX - this.offsetLeft; 
    var Y = e.pageY - this.offsetTop;
    if(JSON.stringify(mousePosOrig) === JSON.stringify([X, Y])) // This is for adding dots (clicking in the same position doesn't draw a line)
        addPoint(X+1,Y)
    
    canvas.isDrawingMode = false;
    lineObjects.push(false);        
});

function addPoint(X, Y) {
    // We are now dragging the mouse
    canvas.isDrawingMode = true;
    lineObjects.push({ // We store the mouse movement information as JSOn objects. We can store color and what not as well.
        x:X,
        y:Y,
        color: brushColor,
        brush:brushShape,
        size:brushSize
    })
    render();
}

function undo() {

    // Since we have an array that looks like this
    // [obj, obj, obj, false, obj, obj, obj, false]
    // undoing is a sinch because all that needs to happen is that we need to follow the array
    // backwards to the next nearest `false` and then splice the array from 
    // For example, undoing the canvas above would create a new array that looks like this
    // [obj,obj,obj,false]

    let newArray = []
    let indexOn = lineObjects.length - 3;
    while(lineObjects[indexOn] && indexOn > -1)
        indexOn--
    for(var x = 0; x < indexOn; x++)
        newArray.push(lineObjects[x]);
    lineObjects = newArray;
    render();
}

function clearCanvas() {
    lineObjects = []; // Removes all lines from canvas
    render();
}

function render() {
    context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears canvas

    // The following code works by following an array that looks like this:
    // [obj, obj, false, obj, obj, obj, false]
    // A "line" is from obj -> false
    // So the following code cycles through an array and connects the object at index `x` to the object at index `x-1` with a line.
    // If x is false the line is done and a new line stars somewhere else
    // if x == 0 or x == false or x - 1 == false then no line is drawn

    if (lineObjects.length > 0) { 
        for(var x = 0; x < lineObjects.length; x++) {
            context.beginPath();
            var on = lineObjects[x];
            var prev = lineObjects[x - 1]
            if (!on || !prev)
                continue
            
            // Used for dynamic values such as color, brush size, etc.

            context.strokeStyle = on.color;
            context.lineJoin = on.brush;
            context.lineWidth = on.size;            
			console.log(on.size);
            // Draws the line
            
            context.moveTo(on.x, on.y);
            context.lineTo(prev.x, prev.y);
            
            context.closePath();
            context.stroke();
        }
    }
}


$("#size").change(function(e) { // Change size of brush
    brushSize = Number($("#size").val());
});

$("#color").change(function(e) { // Change color of brush
	brushColor = $("#color").val();
});

