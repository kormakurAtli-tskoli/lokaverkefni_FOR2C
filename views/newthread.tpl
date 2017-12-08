<!DOCTYPE html>
<html>
	<style type="text/css">
	*{
		font-family: Roboto;
	}
	body{
		margin: 0;
		margin-top:200px;
		background-color:#F5F5F5 ;
	}
	.signup{
		text-align:center;
		border:black solid 1px;
		font-size 1em;
		padding: 0 10px;
		width:24%;
		float:left;
	}
	.signup h3{
		color:black;
	}
	.signup:hover{
		background-color:#E0E0E0;
	}
	.alert{
		position:fixed;
		right:0;
		left:0;
		top:0;
	}
	form{
		max-width: 600px;
		margin: auto;
	}
	h2{
		font-family: arial;
		margin-bottom: 0;
	}
	input{
		width: 95%;
		padding: 10px;
		outline-style: outset;
		margin: 10px 0 10px 0;
		font-size: 1.2em;
		margin:10px auto;
	}
	input[type=submit]{
		width:99%;
	}
	input[type=radio]{
		outline: none;
	}
	ul li{
		color: #AAAAAA;
		display: block;
		position: relative;
		float: left;
		width: 100%;
		height: 100px;
		border-bottom: 1px solid white;
	}
	ul li input[type=radio]{
		position: absolute;
		visibility: hidden;
	}
	ul li input[type=checkbox]{
		position: absolute;
		visibility: hidden;
	}
	ul li label{
		display: block;
		position: relative;
		font-weight: 300;
		font-size: 1.35em;
		padding: 25px 25px 25px 80px;
		margin: 10px auto;
		height: 30px;
		z-index: 9;
		cursor: pointer;
		-webkit-transition: all 0.25s linear;
	}
	ul li:hover label{
		color: black;
	}
	ul li .check{
		display: block;
		position: absolute;
		border: 5px solid #AAAAAA;
		border-radius: 100%;
		height: 25px;
		width: 25px;
		top: 30px;
		left: 20px;
		z-index: 5;
		transition: border .25s linear;
		-webkit-transition: border .25s linear;
	}
	ul li .checkb{
		border-radius: 0%;
	}
	ul li:hover .check {
		border: 5px solid black;
	}
	ul li .check::before {
		display: block;
		position: absolute;
		content: '';
		border-radius: 100%;
		height: 15px;
		width: 15px;
		top: 5px;
		left: 5px;
		margin: auto;
		transition: background 0.25s linear;
		-webkit-transition: background 0.25s linear;
	}
	ul li .checkb::before{
		border-radius: 0%;
	}
	input[type=radio]:checked ~ .check {
		border: 5px solid DodgerBlue;
	}
	input[type=radio]:checked ~ .check::before{
		background: DodgerBlue;
	}
	input[type=radio]:checked ~ label{
		color: DodgerBlue;
	}
	input[type=checkbox]:checked ~ .check {
		border: 5px solid DodgerBlue;
	}
	input[type=checkbox]:checked ~ .check::before{
		background: DodgerBlue;
	}
	input[type=checkbox]:checked ~ label{
		color: DodgerBlue;
	}
	/* The alert message box */
	.alert {
		padding: 20px;
		background-color: #f44336; /* Red */
		color: white;
		margin-bottom: 15px;
	}

	/* The close button */
	.closebtn {
		margin-left: 15px;
		color: white;
		font-weight: bold;
		float: right;
		font-size: 22px;
		line-height: 20px;
		cursor: pointer;
		transition: 0.3s;
	}

	/* When moving the mouse over the close button */
	.closebtn:hover {
		color: black;
	}
	body{
		max-width:1000px;
		margin:auto;
	}
	.header{
		height:50px;
		width:100%;
	}
	.header a{
		width:50%
	}
	.header h2{
		width:47%;
		float:left;
	}
	h1{
		width:100%;
		margin-top:1px;
	}
</style>
	<head>
		<title>Bindle - Nýr þráður</title>
		<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
		<link rel="shortcut icon" type="image/ico" href="static/favicon.ico"/>
	</head>
	<body>
		<div class="header">
			<h2>Sæl/l, {{name}}! Velkomin/n...</h2>
			<a href="/utskra"><div class="signup"><h3>Skrá út</h3></div></a>
			<a href="/thread"><div class="signup"><h3>Til baka</h3></div></a>
		</div>
		<br>
		<form action="/thread" method="post" id="newthread">
			<input type="text" name="titill" placeholder="Titill þráðar">
			<textarea name="text" form="newthread" style="width: 95%;padding: 10px;outline-style: outset;margin: 10px 0 10px 0;font-size: 1.2em;margin:10px auto;height: 400px;" placeholder="Efni þráðar..."></textarea>
			<input type="submit" name="submit">
		</form>
		</form>
	</body>
</html>