-- import same database from 10-12, and list all genres from hbtn_0d_tvshows and display the nunmber of shows linked to each
SELECT tv_show_genres.genre_id AS genre, count(tv_shows) AS number_of_shows
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id=tv_show.id
ORDER BY number_of_shows DESC;
