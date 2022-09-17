# kills a process
exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
}
