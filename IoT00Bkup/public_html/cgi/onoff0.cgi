#!/usr/bin/perl

use strict;
use warnings;
use CGI;

#データファイル指定。chmod a+w しておくこと
my $datafile='./onoff.txt';

# POST / GET パラメータを取得
my $q = new CGI;

#HTMLヘッダ出力
print $q->header(-charset=>"utf-8");
print $q->start_html(-title=>"部屋の電灯");

# パラメータ名をkeywordsと指定して取得する（無記名パラメータ）
my $param1 = $q->param('keywords');

# print $param1. '<br>';

if($param1){ #もし param1の中身があれば、ファイルを上書きする
	open(FH,">$datafile"); #追記ではなく上書きにする
	 print FH $param1;
	close(FH);
}

open(FH,"$datafile");
  my $line =<FH>;
  print $q->h1("$line");
close (FH);

print  $q->end_html;
exit;

