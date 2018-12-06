<!DOCTYPE html>
<html>
<head>
	<style>
	body {
          background-color: #cccccc;
          margin: 3em;
          padding-left: 3em;
      }

      h3 {
          color: #073100;
      }

      form {
          font-family: sans-serif;
      }
      input {
        padding: .3em;
        margin: .3em 1em;
      }
</style>
	<meta charset="utf-8">
	<title>Lokaverkefni</title>
</head>
<body>
	<h3>Ef þig langar bara að sjá fréttirnar ýttu</h3>
	<a href="/frettir">Hér</a>
	<hr>
	<h3>Innskráningarform:</h3>
	<form method="post" action="/doinnskra" accept-charset="ISO-8859-1" id="inn">
		Notendanafn:<br>
		<input type="text" name="user" required>
		Lykilorð:<br>
		<input type="text" name="pass" required>
		<input type="submit" name="Skrá-inn">
	</form>
</body>
</html>