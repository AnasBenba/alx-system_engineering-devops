#!/usr/bin/env bash
#set up your client SSH configuration 
#file so that you can connect to a 
#server without typing a password.
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}
