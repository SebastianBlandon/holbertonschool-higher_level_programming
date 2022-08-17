#!/usr/bin/node
exports.esrever = function (list) {
  const rarray = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    rarray[j] = list[i];
  }
  return rarray;
};
