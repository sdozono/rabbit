#!/usr/bin/perl
use strict;
require "rabbit.pl";

#初期設定
our $method = "";
our $table_name = "personal";
our $title = "アドレス帳";

#テーブルデータ
our @items=(
    ["id", "id"],
    ["name","名前"],
    ["addr","住所"],
    ["tel","電話"],
    ["email","メール"]
);

#Controller
if (param()) {
    $method = param('method');
    if($method eq "add") {&action_add();}
    if($method eq "del") {&action_del(param('id'));}
    if($method eq "edit"){
        &action_edit(param('id'));
        &show_header("./addrbook/header");
        &show_edit(param('id'));
        &show_footer("./addrbook/footer");
        exit;
    }
}

#View
&show_header("./addrbook/header");
print "<h1>".$title."</h1>\n";
&show_add("./addrbook/add");
&show_all("./addrbook/all");
&show_footer("./addrbook/footer");

1;


