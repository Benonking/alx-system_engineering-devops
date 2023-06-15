# enbable user hoberton to login and open files without error

# increase hard file limit from 5 to 5000
exec { 'increase-soft-file-limit-user-holberton':
    command => 'sed -i "/holberton hard/s/5/5000/g" /etc/security/limits.conf',
    path    => 'usr/local/bin:/bin/'
}

# increase soft file limit
exec { 'increase-hard-file-limit-user-holberton':
    command => 'sed -i "/holberton soft/s/5/5000/g" /etc/security/limits.conf',
    path    => 'usr/local/bin:/bin/'
}