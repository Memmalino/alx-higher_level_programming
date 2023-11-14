#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length; let tmp;
  for (let j = 0; j < list.length / 2; j++, i--) {
    tmp = list[j];
    list[j] = list[i - 1];
    list[i - 1] = tmp;
  }
  return (list);
};
