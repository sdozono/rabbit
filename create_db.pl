use strict;
use DBI;

# Connection
my $dbh = DBI->connect("dbi:SQLite:dbname=addrbook2.db");

# Table definition
$dbh->do("create table personal (id INTEGER PRIMARY KEY AUTOINCREMENT, name,addr, tel, email);");
# Data
$dbh->do("insert into personal (name, addr, tel, email) values ('Shun Dozono','Test Addr','07011112222','dozono\@example.com');");

# disconnect
$dbh->disconnect;

# finished
print "OK\n";

