#!/usr/bin/perl
use strict;
require "rabbit.pl";
require "translation.cgi";

#Inial Settings
our $method = "";
our $table_name = "personal";
our $title = __("Address Book");
our $request_method;

#Table Data
our @items=(
    ["id", "id"],
    ["name",__("name")],
    ["addr",__("addr")],
    ["tel"  ,__("tel")],
    ["email",__("email")]
);

#Controller
my $use_all = 1;
if (param()) {
    $method = param('action');
    if($method eq "add") {&action_add();}
    if($method eq "del") {&action_del(param('id'));}
    if($method eq "edit"){
        if($request_method eq "GET"){
            &action_edit(param('id'));
            &show_header("./addrbook/header");
            &show_edit("./addrbook/edit", param('id'));
            &show_footer("./addrbook/footer");
            exit;
        } else {
            &action_edit(param('id'));
        }
    }
} 

#all View
&action_all();

#View
&show_header("./addrbook/header");
print "<h1>".$title."</h1>\n";
&show_add("./addrbook/add");
&show_all("./addrbook/all");
&show_footer("./addrbook/footer");

1;


