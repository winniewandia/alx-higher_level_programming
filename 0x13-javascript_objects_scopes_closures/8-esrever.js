#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const newList = [];
  for (let j = len - 1; j >= 0; j--) {
    newList.push(list[j]);
  }
  return newList;
};
