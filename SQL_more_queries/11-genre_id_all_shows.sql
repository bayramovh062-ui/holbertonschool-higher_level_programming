-- we can list tw_shows base's title column and tv_show_genres base's genre_id column with using this code

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
