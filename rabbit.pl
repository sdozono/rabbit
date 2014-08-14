###########################################
# "Rabbit" development framework for cgi.
# by SD
# license: MIT
###########################################
use DBI;
use CGI qw(param);
our $title;
our @items;
our $table_name;
our $method;

require "settings.cgi";
our $dbname;
our $my_dbi;
our $sth;
our $cgi;
our $request_method;

# connect DB
our $dbh = DBI->connect($my_dbi) or do {
    print_err('can not connect database.');
    exit 0;
};
$cgi = CGI->new;
$request_method = $cgi->request_method;

###########
# Methods
###########
sub action_all {
    my $cols = &list_cols(1);
    my $sql = "SELECT ".$cols." FROM ".$table_name;
    myquery($sql);
}

sub action_add {
    my $cols = &list_cols(0);
    my $vals = &list_vals(0);
    my $sql = "insert into ".$table_name. " (".$cols.") values (".$vals.");";
    myquery($sql);
}

sub action_edit {
    my $id = shift;
    my $cols = &list_cols(0);
    my $data = param();
    if($id !~ /^[0-9]*$/){
        print_err("id is not number.[".$id."]");
        exit 0;
    }
    if($request_method eq 'GET'){
        my $sql = "select * from ".$table_name." where id=".$id;
        myquery($sql);
    } else {
        #update data
        my $sql = " update ".$table_name." SET ";
        my $count = 0;
        for my $item (@items){
            if($item->[0] ne "id"){
                if($count > 0){
                    $del = ",";
                } else {
                    $del = "";
                }
                $count++;
                my $val = param($item->[0]);
                $sql .= $del . $item->[0]."='".$val."' ";
            }
        }
        $sql .= "where id =".$id.";";
        myquery($sql);
        my @urlinfo = &split_url($ENV{REQUEST_URI});
        print CGI::redirect($urlinfo[4]);
    }
}

sub action_del {
    my $id = shift;
    my $sql = "delete from ".$table_name. " where id = ".$id.";";
    myquery($sql);
    my @urlinfo = &split_url($ENV{REQUEST_URI});
    print CGI::redirect($urlinfo[4]);
}

############
# Templates
############

sub show_header {
    my $file = shift;
    require $file.".cgi";
}

sub show_add {
    my $file = shift;
    require $file.".cgi";
}

sub show_edit {
    my $file = shift;
    my $id = shift;
    require $file.".cgi";
}

sub show_footer {
    my $file = shift;
    require $file.".cgi";
    $dbh->disconnect;
}

sub show_all {
    my $file = shift;
    require $file.".cgi";
}

###########
# Funcs
###########
sub __{
    our $translations;
    my $str = shift;
    if(exists($translations{$str})){
        return $translations{$str};
    } else {
        return $str;
    }
}

sub myquery {
    my $sql = shift;
    $sth = $dbh->prepare($sql) or do {
        print_err("SQL Prepare Failed.($sql)", __LINE__,$DBI::errstr);
        exit 0;
    };
    my $rc = $sth->execute or do {
        print_err("SQL Exec Failed. ($sql)", __LINE__,$DBI::errstr);
        exit 0;
    };
}

sub list_cols {
    my $all_flag = shift;
    my %in=();
    for my $item (@items){
        $in{$item->[0]} = h(param($item->[0]));
    }
    my $cols = "";
    my $i=0;
    my $del=",";
    for my $item (@items){
        if($i==0){$del=""}else{$del=",";}
        if($all_flag == 1 || defined $in{$item->[0]}){ #if exists the form data in @items
            $cols .= $del.$item->[0];
            $i++;
        }
    }
    return $cols; 
}

sub list_vals {
    my $all_flag = shift;
    my %in=();
    for my $item (@items){
        $in{$item->[0]} = h(param($item->[0]));
    }
    my $vals = "";
    my $i=0;
    my $del=",";
    for my $item (@items){
        if($i==0){$del=""}else{$del=",";}
        if($all_flag == 1 || defined $in{$item->[0]}){
            $vals .= $del."'".$in{$item->[0]}."'";
            $i++;
        }
    }
    return $vals;
}
 
sub print_err
{
    my $msg = shift @_;
    my $line = $#_ >= 0 ? shift : undef;
    my $errmsg = shift;
    print "Content-Type: text/html;charset=utf-8\n\n";
    print "<html>\n";
    print "<head>\n";
    print "<title>Error</title>\n";
    print "</head>\n";
    print "<body>\n";
    print "<h1>Error</h1>\n";
    if ($line) {
        print "line:$line<br/>";
    }
    print "<div>$msg</div>\n";
    print "<div>[".$errmsg."]</div>\n";
    print "</body>\n";
    print "</html>\n";
}

sub h {
 my $str = shift;
 if(!defined($str)){
    return;
 }
 $str =~ s/'/''/g;
 $str =~ s/\\/\\\\/g;
 return $str;
}

sub trim {
    my @out = @_;
    for (@out) {
        s/^\s+//;
        s/\s+$//;
    }
    return wantarray ? @out : $out[0];
}

sub log {
        my $logfile = "rabbit.log";
        my $string = $_[0];
        open(DAT,">>$logfile");
        print DAT "[".localtime(time)."] ".$string."\n";
        close(DAT);
}

#http://notebook99.blog87.fc2.com/blog-entry-33.html
sub split_url{
 my ($urltxt) = @_;
 my @splitlist;
 my $QUERYCH = '&?=$#!';
 $splitlist[0] = $urltxt;
 #if( $urltxt =~ m|^(.*)://(.*?)?:?(\d+)?((/.*?)([$QUERYCH].*)?)$|i ){
 if( $urltxt =~ m|(.*?)?:?(\d+)?((/.*?)([$QUERYCH].*)?)$|i ){
  $splitlist[1] = $1;
  $splitlist[2] = $2;
  $splitlist[3] = $3;
  $splitlist[4] = $4;
  $splitlist[5] = $5;
  $splitlist[6] = $6;
  if( $splitlist[5] =~ m|(.*/)?(.*?(\..*)?)$|i ){
   $splitlist[7] = $1;
   $splitlist[8] = $2;
   $splitlist[9] = $3;
  }
 }
 return @splitlist;
}



1;
