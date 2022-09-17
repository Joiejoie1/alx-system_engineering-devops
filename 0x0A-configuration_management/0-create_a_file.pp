# A file is created using puppet in /tmp
file { '/tmp/school':
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
