data = require("./emoji.json");

module.exports.list = list;
module.exports.random = random;
module.exports.len = data.length;
module.exports.calc = calc;

function isInFun(list, list_name) {
  isIn = false;
  list.forEach((element) => {
    if (
      String(list_name).toLowerCase() ==
      String(element.toLowerCase()).replace(/-/gm, " ").replace(/and/gm, "&")
    ) {
      isIn = true;
    }
  });
  return isIn;
}

function returnHelper(emoji, verbose) {
  if (!verbose) {
    e = [];
    emoji.forEach((el) => {
      e.push(el["emoji"]);
    });

    return e;
  }
  return emoji;
}

function isEligible(
  element,
  emoji,
  noduplicates,
  skintones,
  allstatus,
  group,
  subgroup,
  nogroup,
  nosubgroup,
  search,
  maxversion,
  genders
) {
  if (emoji.includes(element) && noduplicates) return false;

  if (!skintones && String(element["description"]).includes("skin tone"))
    return false;

  if (!genders && (String(element["description"]).includes("men")|| String(element["description"]).includes("man")) && String(element["group"]) == "People & Body")
    return false;

  if (element["status"] != "fully-qualified" && allstatus == false)
    return false;

  if (group.length != 0)
    if (!isInFun(group.split(","), element["group"])) return false;

  if (subgroup.length != 0)
    if (!isInFun(subgroup.split(","), element["subgroup"])) return false;

  if (nogroup.length != 0)
    if (isInFun(nogroup.split(","), element["group"])) return false;

  if (nosubgroup.length != 0)
    if (isInFun(nosubgroup.split(","), element["subgroup"])) return false;

  if (search.length != 0)
    if (!String(element["description"]).includes(search)) return false;

  if (element["version"].split("E")[1] > maxversion) return false;

  return true;
}

function list(
  {n = 0,
  allstatus = false,
  noduplicates = true,
  group = "",
  subgroup = "",
  nogroup = "",
  nosubgroup = "",
  skintones = false,
  v = false,
  search = "",
  maxversion = 14.0,
  genders = false,
  offset = 0} = {}
) {
  emoji = [];
  var count = 0
  for (elem of data) {
    

    if (n != 0 && emoji.length == n) break;

    


    if (
      !isEligible(
        elem,
        emoji,
        noduplicates,
        skintones,
        allstatus,
        group,
        subgroup,
        nogroup,
        nosubgroup,
        search,
        maxversion,
        genders
      )
    )
      continue;

    count++;

    if (count <= offset) {
      continue;
    }

    emoji.push(elem);
  }

  return returnHelper(emoji, v);
}

function random(
  {n = 1,
  allstatus = false,
  noduplicates = true,
  group = "",
  subgroup = "",
  nogroup = "",
  nosubgroup = "",
  skintones = true,
  v = false,
  search = "",
  maxversion = 13.0,
  genders = false,
} = {}
) {
  emoji = [];

  while (emoji.length < n) {
    if (data.length == 0) break;

    index = Math.floor(Math.random() * (data.length - 1));

    if (
      !isEligible(
        data[index],
        emoji,
        noduplicates,
        skintones,
        allstatus,
        group,
        subgroup,
        nogroup,
        nosubgroup,
        search,
        maxversion,
        genders
      )
    ) {
      data.splice(index, 1);
      continue;
    }

    emoji.push(data[index]);
  }

  return returnHelper(emoji, v);
}



function calc(
  {
  allstatus = false,
  noduplicates = true,
  group = "",
  subgroup = "",
  nogroup = "",
  nosubgroup = "",
  skintones = false,
  search = "",
  maxversion = 14.0,
  genders = false,
  } = {}
) {
  var count = 0
  for (elem of data) {
    


   


    if (
      isEligible(
        elem,
        [],
        noduplicates,
        skintones,
        allstatus,
        group,
        subgroup,
        nogroup,
        nosubgroup,
        search,
        maxversion,
        genders
      )
    )
      count++;

  }
  return count
}