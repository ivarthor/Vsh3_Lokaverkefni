<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>admin</title>
</head>
<body>
	<h2>Velkominn ritstjori</h2>
	<h3>nýskráning frétta</h3>
	<form method="POST" action="/nyfrett" accept-charset="ISO-8859-1">
		<textarea name="story" cols="100" rows="5"></textarea>
		<p>
			Höfundur: <input type="text" name="author"> | <input type="submit" value="skrá frétt">
		</p>
	</form>
	<hr>
	<p><a href="/">Fréttasíða</a></p>
	<hr>
	<h3>Breyta frétt:</h3>
	<form method="POST" action="/breyta" accept-charset="ISO-8859-1">
		Höfundur:<br>
		<input type="text" name="author" required><br>
		<input type="submit" value="Innskrá">
	</form>
</body>
</html>