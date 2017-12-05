<html>
<body>
	<h1>Deepblu Backup Tool</h1>
	<span>by Sander Van de Moortel (<a href="mailto:sander.vandemoortel@gmail.com">sander.vandemoortel@gmail.com</a>)</span>
	<ul>
		<li>Keep a local backup of your dive logs uploaded to Deepblu.</li>
		<li>Download uploaded COSMIQ or COSMIQ<sup>+</sup> dive logs onto your computer.</li>
		<li>Exported data is in <a href="http://uddf.org">UDDF format.</a></li>
	</ul>

	<h2>Ready?</h2>
	<span>Enter your Deepblu username (email address) and password below.</span>
	<ul>
		<li>If you signed up through Facebook, just enter your user id instead.</li>
		<li>To find your user id, visiting your profile page on Deepblu, look at the address bar, and copy the text between <code>/user/</code> and <code>/profile/</code>
		<li><strong>I will not store your username and password</strong>, but you'll have to take my word for it.</li>
		<li>If you don't believe me, just enter your user id or download the <a href="https://github.com/bluppfisk/deepblu-tools">Deepblu Backup Tool source code from Github</a> and run it yourself.</li>
	</ul>
<form method="POST" action="index.php">
<input type="text" name="user" placeholder="Deepblu userID or email" />
<input type="password" name="password" placeholder="password" />
<input type="submit" name="submit" value="Get backup" />
</form>
	<?php
	if ($_POST['submit'] && !empty($_POST['user']) && isset($_POST['password'])) {
	        $user = $_POST['user'];
	        $password = $_POST['password'];
	        $command = escapeshellcmd('./backupdives.py '.$user.' '.$password);
	        echo('<h2>Result!</h2><div class="result">');
			$result=explode(",", exec('/usr/bin/python3 backupdives.py '.$user.' '.$password));
			if($result[0]!=='0') {
				printf("<span>Sometheeng ees wrong, officeur. Error message: %s</span>", $result[1]);
			} else {
				printf("<span>That worked! Here's your backup: <a href='done/%s'>%s</a></span>",$result[1], $result[1]);
			}
			?>
				<h2>What's next</h2>
				<ul>
					<li>Click the link to download your backup in UDDF format.</li>
					<li>Import this file into your favourite divelog software (I like <a href="https://subsurface-divelog.org">Subsurface</a>)</li>

					<li><strong>Before you go...</strong> This took a few days of my life to develop. Consider supporting me with a <a href="https://www.paypal.me/sandervdm?locale.x=en_US&country.x=DE">small donation through PayPal</a>.</li>

			<?php
	        echo('</div>');
	}
	?>
</body>
</html>