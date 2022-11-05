## 0x19-postmortem

![image](https://user-images.githubusercontent.com/99324596/200134291-63bc7900-acf2-4c94-ba4d-7abdafd4098b.png)

After the launch of the System Engineering & Dev Ops project 0x19 at Holberton School, an outage happened on a lone Ubuntu 14.04 container hosting the Apache web server. When GET calls were made to the server, 500 Internal Server Errors were returned instead of the HTML file specifying a straightforward Holberton WordPress site.

## Debugging Process:

Using ps aux, checked the status of the first process that was debugging. Root and www-data were two apache2 processes that were successfully executing.
looked in the /etc/apache2/sites-available directory’s folder. discovered that /var/www/html/ was the location of the content being served by the web server.
3. Ran strace on the PID of the root Apache process in one terminal. The server coiled in another. Great things were anticipated, yet disappointed. No meaningful information was provided by strace.

4. Step 3 was repeated, but this time used the PID for the www-data process. lowered expectations this time, and it paid off! When trying to access the file /var/www/html/wp-includes/class-wp-locale.phpp, strace revealed a -1 ENOENT (No such file or directory) error.

5: Used Vim pattern matching to examine each file in the /var/www/html/ directory in an effort to identify the incorrect.phpp file extension. the wp-settings.php file is where you may find it. Line 137, require once(ABSPATH.WPINC.’/class-wp-locale.php’);).

6.eliminated the line’s trailing p.

7: The server was given another curl test. 200 A-ok!

8: Created an automated Puppet manifest to remedy the mistake.

## Summation
Simply said, a typo. Have to adore ’em. Specifically, when attempting to load the file class-wp-locale.phpp, the WordPress software was running into a major issue in wp-settings.php. Class-wp-locale.php was the right file name, and it was located in the wp-content directory of the application folder.

The trailing p was simply removed as part of the typo’s patch.

## Prevention
This outage was not a web server error, but an application error. To prevent such outages moving forward, please keep the following in mind.

Test the application before deploying. This error would have arisen and could have been addressed earlier had the app been tested.

Note that in response to this error, I wrote a Puppet manifest 0-strace_is_your_friend.pp to automate fixing of any such identitical errors should they occur in the future. The manifest replaces any phpp extensions in the file /var/www/html/wp-settings.php with php.

But of course, it will never occur again, because we’re programmers, and we never make errors!


Thanks for reading!
