#!/usr/bin/perl    
    print "Content-Type: text/html; charset=utf-8\n\n";
    print "<html>\n";
    print "<head>\n";
    print "<link rel='stylesheet' href='css/table.css' type='text/css'>\n";
    print "<link rel='stylesheet' href='css/form.css' type='text/css'>\n";
    print "<title>".$title."</title>\n";
    print "<script type='text/javascript'>\n";
    print "<!--\n";
    print "function mydel(id)\n";
    print "{\n";
    print "    c = confirm('".__("Are you going to delete")."ID:'+id+'".__("?")."');\n";
    print "    return c;\n";
    print "}\n";
    print "//-->\n";
    print "</script>\n";
    print "</head>\n";
    print "<body>\n";

