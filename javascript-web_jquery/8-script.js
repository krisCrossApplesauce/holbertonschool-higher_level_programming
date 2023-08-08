#!/usr/bin/node
$(document).ready(function () {
  $.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
    $(data.results).each(function () {
        $("ul#list_movies").append("<li>" + this.title + "</li>");
    });
  });
});
