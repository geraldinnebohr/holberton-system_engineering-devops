# create a file in /tmp using puppet
file { '/tmp/holberton':
ensure  => file,
owner   => 'www-data',
group   => 'www-data',
mode    => '0600',
content => 'I love Puppet',
}