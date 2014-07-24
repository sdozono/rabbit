#!/usr/bin/perl
    my $cols = &list_cols(1);
    my $sql = "SELECT ".$cols." FROM ".$table_name;
    my $sth = $dbh->prepare($sql) or do {
        print_err("SQL Prepare Failed.($sql)", __LINE__,$DBI::errstr);
        exit 0;
    };
    my $rc = $sth->execute or do {
        print_err("SQL Exec Failed. ($sql)", __LINE__,$DBI::errstr);
        exit 0;
    };

    print '<table border="1">';
    print '<tr>';
    for my $item (@items){
        print "<th>".$item->[1]."</th>\n";
    }
    print "<th colspan=2>操作</th>\n";
    print '</tr>';

    while (my $ref_row = $sth->fetchrow_hashref) {
        print "<tr>\n";
            my $id = ""; 
            for my $item (@items){
                print "<td>", $ref_row->{$item->[0]}, "</td>\n";
                if($item->[0] eq "id"){
                    $id = $ref_row->{$item->[0]};
                }
            }
            #action
            print "<td><a href='?method=edit&id=".$id."' >編集</a></td>\n";
            my $del = "if(!mydel(".$id.")){return false;}";
            print "<td><a href='?method=del&id=".$id."' onclick='".$del."'>削除</a></td>\n";
        print "</tr>\n";
    }
    print "</table>";

