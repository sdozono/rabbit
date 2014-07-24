#!/usr/bin/perl    
    print "Content-Type: text/html; charset=utf-8\n\n";
    print "<html>\n";
    print "<head>\n";
    print "<title>".$title."</title>\n";
    print "<script type='text/javascript'>\n";
    print "<!--\n";
    print "function mydel(id)\n";
    print "{\n";
    print "    c = confirm('ID:'+id+'を削除しますか？');\n";
    print "    return c;";
    print "}\n";
    print "//-->\n";
    print "</script>\n";
    print "</head>\n";
    print "<body>\n";

