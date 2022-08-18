# Web infrastructure design
====================================================================================

0. Simple web stack
------------------------------
<p>is a simple web infrastructure design that consist of:</p>
<ul>
<li>1 server</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 application files (your code base)</li>
<li>1 database (MySQL)</li>
<li>1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8 </li>
</ul>


1. Distributed web infrastructure
------------------------------
<p>is a simple Distributed web infrastructure that consist of:</p
<ul>
<li>2 servers</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 load-balancer (HAproxy)</li>
<li>1 set of application files (your code base)</li>
<li>1 database (MySQL) </li>
</ul>

2. Secured and monitored web infrastructure
------------------------------
<p>is a simple Secured and monitored web infrastructure that consist of:</p>
<ul>
<li>2 servers</li>
<li>1 web server (Nginx)</li>
<li>1 application server</li>
<li>1 load-balancer (HAproxy)</li>
<li>1 set of application files (your code base)</li>
<li>1 database (MySQL) </li>
<li>3 firewalls</li>
<li>1 SSL certificate to serve www.foobar.com over HTTPS</li>
<li>3 monitoring clients (data collector for Sumologic or other monitoring services) </li>
</ul>


====================================================================================
# AUTHORS
<h4> by: YourDevLebo & <a href="https://github.com/samie-ya"> samie-ya </a> </h4>
