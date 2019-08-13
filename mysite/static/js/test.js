var div = document.getElementById('img');
var img = new Image();
img.src = '../static/images/4-2.jpg';
var width = img.width;
var height = img.height;
//var canvas = document.querySelector('canvas')
//canvas.width = 400;
//canvas.height = 400;
//canvas.width = window.innerWidth;
//canvas.height = window.innerHeight;
//var c = canvas.getContext('2d');
img.onload = function(){
    div.appendChild(img)
}
// c.fillStyle = 'rgba(255,0,0, 0.1)'
// c.fillRect(400, 100, 300, 300);
// c.fillStyle = 'rgba(23,255,134, 0.1)'
// c.fillRect(700, 400, 30, 30);

// c.beginPath();
// c.moveTo(400,100);
// c.lineTo(700,100);
// c.lineTo(700,400);
// c.lineTo(400,400);
// c.lineTo(400,100);
// c.strokeStyle = "#fa34a3";
// c.stroke();

var mouse = {
    x: undefined,
    y: undefined
}

window.addEventListener('click',
    function(event){
        mouse.x = event.x;
        mouse.y = event.y;
        console.log(mouse);
})

// function ColorCircle(init_x, init_y, r){
//     this.x = init_x;
//     this.y = init_y;
//     this.r = r;
//     this.dy = 0.2;
//     this.draw = function(){
//         c.beginPath();
//         c.arc(this.x, this.y, this.r, 0, Math.PI*2, false);
//         c.strokeStyle = "blue";
//         c.stroke();
//         c.fillStyle = "red";
//         c.fill();
//     }
//     this.update = function(){
//         if(this.y >= init_y+13 || this.y <= init_y-13){
//             this.dy = -this.dy;
//         }
//         this.y += this.dy;
//     }
//     this.activate = function(){

//     }
//     this.goback = function(){

//     }
// }

// var circleArray = []
// for (var i=0; i<100; i++){
//     var x = Math.random() * innerWidth;
//     var y = Math.random() * innerHeight;
//     circleArray.push(new ColorCircle(x,y,30));
// }

// function animate(){
//     requestAnimationFrame(animate);
//     c.clearRect(0, 0, innerWidth, innerHeight);
//     for (var i=0; i< circleArray.length;i++){
//         circleArray[i].draw();
//         circleArray[i].update();
//     }
// }

// // 一群圆 先draw 
// // 一开始调用白色上下
// // 然后监听鼠标 点到哪个圆内（且不是当前的） 
// // 就调用当前上下的回位置 调用新的上下即可
// animate();