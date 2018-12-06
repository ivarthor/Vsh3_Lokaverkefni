<!DOCTYPE html>
<html>
<head>
	<style>
		a {
			text-decoration: none;
		}

		body {
          background-color: #cccccc;
          margin: 3em;
          padding-left: 3em;
      }

      	h3 {
          color: #073100;
      }
    
	</style>
	<title>Frettir</title>
	<meta charset="utf-8">
</head>
<body>
	<section><h3>{{frett[0][0]}}</h3></section>
	<section>
		<ul>
			% tel = 0
			% for i in frett:
				<li><a href="/frett/{{tel}}">{{i[0]}}</a></li>
				% tel += 1
			% end
		</ul>
	</section>
</body>
</html>