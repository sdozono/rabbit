#!/usr/bin/perl
if(defined($sth)){
    my $ref_row = $sth->fetchrow_hashref;
    print "<form action='' method='POST'>\n";
    print "<input type='hidden' name='id' value='".$ref_row->{"id"}."'>\n";
    print "<input type='hidden' name='action' value='edit'>\n";
    for my $item (@items){
        if($item->[0] ne "id"){
            print $item->[1].": <input type='text' name='".$item->[0]."' value='".$ref_row->{$item->[0]}."'><br>\n";
        }
    }
    print "<input type='submit' value='".__("modify")."'>\n";
    print "<input type='reset' value='".__("reset")."'>\n";
    print "</form>\n";

}

1;

