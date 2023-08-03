#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) { console.log(err); }
  const taskList = JSON.parse(body);
  const usrsDoneTasks = {};
  for (const task of taskList) {
    if (task.completed) {
      if (usrsDoneTasks[task.userId]) {
        usrsDoneTasks[task.userId] += 1;
      } else {
        usrsDoneTasks[task.userId] = 1;
      }
    }
  }
  console.log(usrsDoneTasks);
});
