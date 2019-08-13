$(document).ready(function(){
    $('#ex1').zoom({
        on: 'mouseover',
        magnify: 0.3,
    });
});


window.addEventListener('click',
    function(event){
        var obj = $('img.zoomImg');
        if(obj.css("opacity")==1){
            s_left = obj.css("left");
            s_top = obj.css("top");
            left_px = parseFloat(s_left.slice(1,s_left.length-2));
            top_px = parseFloat(s_top.slice(1,s_top.length-2));
            console.log(left_px, top_px);
            var num = 1;
            for (var pixel of obj.values()){
                pixel.setRed(255);
                pixel.setGreen(0);
                pixel.setBlue(0);
                num ++ ;
                if(num>10) break;
            }
        }
})
