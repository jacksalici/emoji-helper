var emoji = require("./index.js")
var offset=Math.random()*emoji.len
console.log(emoji.list({n: 10, offset: Math.floor(offset)}))
