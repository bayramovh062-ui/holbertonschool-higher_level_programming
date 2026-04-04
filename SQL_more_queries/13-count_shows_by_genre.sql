-- we can list tw_shows base's title column and tv_show_genres base's genre_id column with using this code

SELECT tv_genres.name AS genre, count(tv_show_genres.show_id) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
