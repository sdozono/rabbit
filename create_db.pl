use strict;
use DBI;
require "settings.cgi";
our $dbname;
our $my_dbi;

# connect DB
our $dbh = DBI->connect($my_dbi) or do {
    print_err('can not connect database.');
    exit 0;
};

# Table definition
$dbh->do("create table personal (id INTEGER PRIMARY KEY AUTOINCREMENT, name,addr, tel, email);");
# Data
$dbh->do("insert into personal (name, addr, tel, email) values ('Shun Dozono','Test Addr','07011112222','dozono\@example.com');");

# disconnect
$dbh->disconnect;

# finished
print "OK\n";

