<!doctype html>
<html lang="en">
<head>
	<title>Deepblu Backup Tool</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<meta property="description" content="Backup your Deepblu and COSMIQ dive logs and keep a local copy in UDDF format.">
	<meta property="og:title" content="Deepblu Backup Tool">
	<meta property="og:description" content="Backup your Deepblu and COSMIQ dive logs and keep a local copy in UDDF format.">
	<meta property="og:image" content="http://worldofnonging.com/deepblu-tools/images/imported_into_subsurface.jpg">
	<meta property="og:type" content="website">
	<meta property="og:url" content="http://worldofnonging.com/deepblu-tools/">
	<meta name="twitter:card" content="summary_large_image">
</head>
<body>
	<main role="main">
		<div class="jumbotron">
			<div class="container">
				<h1 class="display-4">Deepblu Backup Tool</h1>
				<p class="lead">Backup your Deepblu and COSMIQ dive logs and keep a local copy in UDDF format</p>
				<?php
					if (isset($_POST['submit']) && !empty($_POST['user'])) {
						if (isset($_POST['max_logs'])) {
							$max_logs = '-m '.escapeshellarg($_POST['max_logs']);
						} else {
							$max_logs = '';
						}
						$drafts = isset($_POST['with_drafts']) ? '-d' : '';
				        $user = escapeshellarg($_POST['user']);
				        $password = escapeshellarg($_POST['password']);
				        $command = './backupdives.py '.$user.' '.$password;
						$result=explode(",", exec('/usr/bin/python3 backupdives.py '.$drafts.' '.$max_logs.' -u '.$user.' -p '.$password));
						if($result[0]!=='0') {
							printf("Sometheeng ees wrong, officeur. Error message: %s", $result[1]);
						} else {
							printf("<p>That worked! Here's your backup:</p><a role='button' class='btn btn-success' href='done/%s'>Download now</a>", $result[1]);
						}
				?>
				<a role='button' class='btn btn-secondary' href='./'>Again?</a>
			</div>
		</div>
		<div class="container">
			<h2>What's next?</h2>
			<ul>
				<li>Click the button to download your backup in UDDF format.</li>
				<li>Import this file into your favourite divelog software, such as <a href="https://subsurface-divelog.org">Subsurface</a>.</li>

				<li><strong>Before you go...</strong> This took a few days of my life to develop. Consider supporting me with a <a href="https://www.paypal.me/sandervdm?locale.x=en_US&country.x=DE">small donation through PayPal</a>.</li>
			</ul>
		</div>
		<?php
			} else {
				?>
				<p>
					<form method="POST" action="index.php">
						<input type="text" name="user" placeholder="Deepblu userID or email" />
						<input type="password" name="password" placeholder="Password or blank" /><br />
						<input type="text" name="max_logs" placeholder="# logs"><label for="max_logs">Only download latest x</label>
						<input type="checkbox" name="with_drafts" id="draftsbox" /><label for="draftsbox">Include drafts?</label>
						<input type="submit" name="submit" value="Get backup" class="btn btn-primary" />
					</form>
				</p>
			</div>
		</div>
		<div class="container">
			<h2>Instructions</h2>
			<p>Enter your Deepblu username (email address) and password in the fields above.</p>
			<ul>
				<li>If you signed up through Facebook, just enter your <em>user id</em> instead.</li>
				<li>To find your <em>user id</em>: visit your Deepblu profile page and look at the address bar. It's the text between <code>/user/</code> and <code>/profile/</code>.
				<li><strong>I will not store your username and password</strong>, but by using this service you'll have to take my word for it.</li>
				<li>If you don't trust it, enter only your <em>user id</em> or download the <a href="https://github.com/bluppfisk/deepblu-tools">Deepblu Backup Tool source code</a> and run it yourself.</li>
				<li><strong>Note: </strong>If you only use your <em>user id</em>, your 'private' dive logs will not be backed up and the backup will not contain any personal information.</li>
			</ul>
			<?php
			}
			?>
		</div>
	</main>
	<footer class="container">
		<p class="small">Inquiries to <a href="mailto:sander.vandemoortel@gmail.com">sander.vandemoortel@gmail.com</a> | <a href="https://github.com/bluppfisk/deepblu-tools">View source code at Github</a> | Buy me a beer --&gt; <a href="https://www.paypal.me/sandervdm?locale.x=en_US&country.x=DE"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif"/></a></p>
	</footer>
</body>
</html>