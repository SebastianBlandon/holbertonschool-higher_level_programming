#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (const i in list) {
    if (searchElement === list[i]) {
      occ += 1;
    }
  }
  return occ;
};
