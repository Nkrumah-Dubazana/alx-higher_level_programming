-- lists all shows contained in hbtn_0d_tvshows that have at least one genere linked
-- lists all rows of a database that have one column in common
SELECT tv_shows.title, tv_show_genere.genere_id FROM tv_shows_generes ON tv_shows.id = tv_shows_genres.show_id ORDER BY tv_shows_generes.genre_id ASC;
