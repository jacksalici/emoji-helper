module.exports = EmojiList;

function isIn(list, list_name) {
  isIn = false;
  list.forEach((element) => {
    if (
      str(list_name).lower() ==
      str(element.lower()).replace("-", " ").replace("and", "&")
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
      e.append(el.get("emoji"));
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
  maxversion
) {
  if (emoji.includes(element) && noduplicates) return false;

  if (!skintones && str(element.get("description")).includes("skin tone"))
    return false;

  if (element.get("status") != "fully-qualified" && allstatus == false)
    return false;

  if (group.length != 0)
    if (!isIn(group.split(","), element.get("group"))) return false;

  if (subgroup.length != 0)
    if (!isIn(subgroup.split(","), element.get("subgroup"))) return false;

  if (nogroup.length != 0)
    if (!isIn(nogroup.split(","), element.get("group"))) return false;

  if (nosubgroup.length != 0)
    if (isIn(nosubgroup.split(","), element.get("subgroup"))) return false;

  if (search.length != 0)
    if (!str(element.get("description")).includes(search)) return false;

  if (float(element.get("version").split("E")[1]) > maxversion) return false;

  return true;
}

class EmojiList {
  data = [];

  constructor() {
    data = require("./emoji.json");
  }

  list(
    n = 0,
    allstatus = False,
    noduplicates = True,
    group = "",
    subgroup = "",
    nogroup = "",
    nosubgroup = "",
    skintones = False,
    v = False,
    search = "",
    maxversion = 14.0
  ) {
    emoji = [];

    for (elem of this.data) {
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
          maxversion
        )
      )
        continue;

      emoji.push(elem);
    }

    return returnHelper(emoji, v);
  }

  random(
    n = 1,
    allstatus = False,
    noduplicates = True,
    group = "",
    subgroup = "",
    nogroup = "",
    nosubgroup = "",
    skintones = True,
    v = False,
    search = "",
    maxversion = 14.0
  ) {
    emoji = [];

    while (emoji.length < n) {
      if (this.data.length == 0) break;

      index = int(random.random() * (len(data) - 1));

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
          maxversion
        )
      ) {
        data.splice(index, 1);
        continue;
      }

      emoji.push(data[index]);
    }

    return returnHelper(emoji, v);
  }
}
