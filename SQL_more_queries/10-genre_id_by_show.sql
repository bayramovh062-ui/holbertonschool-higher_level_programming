-- this code gives us an example about inner join

SELECT tv_shows.tittle, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows_id = tv_show_genres.show_id;
