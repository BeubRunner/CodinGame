/**
 * Don't let the machines win. You are humanity's last hope...
 **/

const width = parseInt(readline()); // the number of cells on the X axis
const height = parseInt(readline()); // the number of cells on the Y axis
let map = [];
for (let i = 0; i < height; i++) {
  const line = readline(); // width characters, each either 0 or .
  map.push(line.split(""));
}
console.error(map);

for (let i = 0; i < map.length; i++) { //interate on y axis
  for (let j = 0; j < map[i].length; j++) { //iterate on x axis
    let array = [j, i, -1, -1, -1, -1] //[x1, y1, x2, y2, x3, y3]
    
    if (map[i][j] === "0") {
        nearestRight(map, array);
        nearestBottom(map, array);
        console.log(array.join(" "));
    }
  }
}


function nearestRight(map, array) {
  for (let i = map[ array[1] ].length -1; i > array[0]; i--){
    if (i > array[0] && map[ array[1] ][i] === "0") {
        array[2] = i;
        array[3] = array[1];
    }
  }
  return array;
}

function nearestBottom(map, array) {
  for (let i = map.length -1; i > array[1]; i--){
    if (i > array[1] && map[i][ array [0] ] === "0") {
        array[4] = array[0];
        array[5] = i;
    }
  }
  return array;
}




// Write an action using console.log()
// To debug: console.error('Debug messages...');