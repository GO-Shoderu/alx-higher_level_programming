#!/usr/bin/node
exports.esrever = function (list) {
  const len = Math.floor(list.length / 2);
  for (let i = 0; i < len; i++) {
    const mid = list.length - i - 1;
    const temp = list[mid];
    list[mid] = list[i];
    list[i] = temp;
  }
  return (list);
};
