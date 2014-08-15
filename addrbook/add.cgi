#!/usr/bin/perl
    print '<fieldset>';
    print '<form action="" method="POST">';
    print '<input type="hidden" name="action" value="add">';
    for my $item (@items){
        if($item->[0] ne "id"){
            print $item->[1].": <input type='text' name='".$item->[0]."'><br>\n";
        }
    }
    print '<input type="submit" value="'.__("add").'">';
    print '</form>';
    print '</fieldset>';

