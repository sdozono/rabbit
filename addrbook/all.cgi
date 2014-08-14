#!/usr/bin/perl
    print '<table border="1">';
    print '<tr>';
    for my $item (@items){
        print "<th>".$item->[1]."</th>\n";
    }
    print "<th colspan=2>".__("actions")."</th>\n";
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
            print "<td><a href='?action=edit&id=".$id."' >".__("edit")."</a></td>\n";
            my $del = "if(!mydel(".$id.")){return false;}";
            print "<td><a href='?action=del&id=".$id."' onclick='".$del."'>".__("delete")."</a></td>\n";
        print "</tr>\n";
    }
    print "</table>";

