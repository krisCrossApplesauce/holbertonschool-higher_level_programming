#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) { console.log(err); }
  const taskList = JSON.parse(body);
  const usrsDoneTasks = {};
  let count = 0;
  for (const task of taskList) {
    if (usrsDoneTasks[task.userId] && (usrsDoneTasks[task.completed] === true)) {
      count += 1;
      usrsDoneTasks[task.userId] = count;
    } else if (usrsDoneTasks[task.completed] === true) {
      count = 1;
      usrsDoneTasks[task.userId] = count;
    } else {
      count = 0;
    }
  }
  console.log(usrsDoneTasks);
});
