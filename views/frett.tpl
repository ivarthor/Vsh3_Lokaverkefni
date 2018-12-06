<!DOCTYPE html>
<html>
<head>
	<style>
	body {
          margin: 10em;
      }

     .nafnid {
     	display: grid;
     	grid-area: nafnid; 
     	padding: 1em;
     }

     .col-2 {
     	display: grid;
     	grid-area: mynd_frett;
     }
     .frett {
     	display: grid;
     	grid-area: frett;
     	padding: 1em;
     }
     .img {
     	display: grid;
     	grid-area: image;
     	padding: 1em;
     }
     body {
     	grid-template-areas:"nafnid",
     						"image",
     						"frett";
     }
</style>
	<title>frett</title>
	<meta charset="utf-8">
</head>
<body>
	<section class="nafnid"><h1>{{frett[0]}}</h1></section>
	<section class="img"> 
		<img src="/static/mynd{{nr}}.jpeg"> 
	</section>
	<section class="frett">	
		<p>{{frett[1]}}</p>		
	</section>
</body>
</html>