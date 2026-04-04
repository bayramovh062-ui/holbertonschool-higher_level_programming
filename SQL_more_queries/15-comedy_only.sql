-- we can list tw_shows base's title column and tv_show_genres base's genre_id column with using this code

SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genre.id
WHERE tv_genre.name = 'Comedy'
ORDER BY tv_shows.title;
