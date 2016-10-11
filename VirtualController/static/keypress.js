function setupKey(key, button, route) {
    $(button).on({
        "touchstart":function() {
            $(button).css("background-color", "gray");
            $.post(route, {"keydown":key});
        }, 
        "touchend":function() {
            $(button).css("background-color", "lightgray");
            $.post(route, {"keyup":key});
        }
    });
}
