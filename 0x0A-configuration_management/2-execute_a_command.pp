# manifest that kills a process named killmenow
exec { 'kill':
command => '/usr/bin/pkill killmenow',
}
