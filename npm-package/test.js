var emoji = require("./index.js")
console.log(emoji.len)
var offset=Math.random()*emoji.len
console.log(offset)
console.log(emoji.list({n: 5, offset: Math.floor(offset)}))
console.log(emoji.random({n: 5, group: 'objects'}))