#!/usr/bin/perl
    print '<form action="addrbook.cgi" method="POST">';
    print '<input type="hidden" name="method" value="add">';
    for my $item (@items){
        if($item->[0] ne "id"){
            print $item->[1].": <input type='text' name='".$item->[0]."'><br>\n";
        }
    }
    print '<input type="submit" value="追加">';
    print '</form>';

