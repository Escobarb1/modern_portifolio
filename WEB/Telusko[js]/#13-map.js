let map = new Map();

map.set("Ernest", "Java");
map.set("Karin", "Android");
map.set("Chirag", "ML");
map.set("Ernest", "Blockchain");
// console.log(map.keys());

// console.log(map.has("Ernest"));

// console.log(map.get("Ernest"));


// for(let [k,v] of map) {
//     console.log(k, " : ", v);
// }

map.forEach((v, k) => {
    console.log(k, " : ", v);
});