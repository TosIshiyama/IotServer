#!/usr/bin/perl

##　グラフ作成CSV取り込み用

use strict;
use warnings;
use CGI;

my $datafile='./data.csv';

#データファイル指定。chmod a+w しておくこと
open(FH,">>$datafile");
 
# POST / GET パラメータを取得
my $q = new CGI;
 
#HTMLヘッダ出力
print $q->header(-charset=>"utf-8");
print $q->start_html(-title=>"CGI Test");

# パラメータ名を指定して取得する場合はこうします
#my $param1 = $q->param('name1');  
#my $param2 = $q->param('name2'); 

# 全てのパラメータを取得する場合
print $q->strong("入力データ:"),$q->br;
my $strg = "";
for my $param_name ($q->param) {

	# my $inP = $q->param($param_name);
	# my $ooo = " $param_name = $inP ";
	# print $ooo. '<br>';
	# print FH $ooo. ' / ';

 $strg = $strg . $ooo . ',';
}
 chop($strg);
 print $strg. '<br>';
 print FH $strg."\n";

#print FH "\n";
close(FH);

#    print $q->br,
#    $q->strong("ファイル内容:"),$q->br;

#open(FH,"$datafile");
#while (my $line =<FH>){
#  chomp($line);
#  print "$line <br>";
#}
#close (FH);

print  $q->end_html;
exit;
