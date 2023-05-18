BEGIN Search
	Artist_name = INPUT Artist
	VAR url = https://theaudiodb.com/api/v1/json/523532/searchalbum.php?s=artist_name
	VAR response = GET data from url
	VAR data = format response
	VAR dict = SORT data
	CONNECT albums.db
	OUTPUT data
	DISPLAY data AS results.html
END Search
