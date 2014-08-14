#!/usr/bin/perl
use strict;
require "rabbit.pl";

#初期設定
our $method = "";
our $table_name = "personal";
our $title = "アドレス帳";
our $request_method;

#テーブルデータ
our @items=(
    ["id", "id"],
    ["name","名前"],
    ["addr","住所"],
    ["tel","電話"],
    ["email","メール"]
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


