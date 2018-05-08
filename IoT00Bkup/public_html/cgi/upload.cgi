#!/usr/bin/perl
 
 use CGI;
 use File::Copy;
 use File::Basename;
 
 my $q = new CGI;
 
 my $fname = basename($q->param('upfile'));
 my $path = '/home/IoT00/public_html/files';
 my $newfile = "$path/$fname";
 
 my $fh = $q->upload('upfile');
 copy ($fh, "$newfile");
 undef $q;
 
 print "Location: ../upload_bin.html\n\n";

