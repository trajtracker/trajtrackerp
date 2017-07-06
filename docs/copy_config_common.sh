#!/bin/bash

cat $1/num2pos/Config_common.txt | sed 's/currentmodule:: trajtrackerp.num2pos/currentmodule:: trajtrackerp.dchoice/' | perl -e 'foreach $line (<STDIN>) { print $line; print "    :noindex:\n" if $line =~ m/autoinstanceattribute/; }' > $1/dchoice/Config_common.txt

