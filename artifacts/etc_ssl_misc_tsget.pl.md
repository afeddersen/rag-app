#!/usr/bin/env perl
# Copyright 2002-2018 The OpenSSL Project Authors. All Rights Reserved.
# Copyright (c) 2002 The OpenTSA Project. All rights reserved.
#
# Licensed under the Apache License 2.0 (the "License").  You may not use
# this file except in compliance with the License.  You can obtain a copy
# in the file LICENSE in the source distribution or at
# https://www.openssl.org/source/license.html

use strict;
use IO::Handle;
use Getopt::Std;
use File::Basename;
use WWW::Curl::Easy;

use vars qw(%options);

# Callback for reading the body.
sub read_body {
    my ($maxlength, $state) = @_;
    my $return_data = "";
    my $data_len = length ${$state->{data}};
    if ($state->{bytes} < $data_len) {
        $data_len = $data_len - $state->{bytes};
        $data_len = $maxlength if $data_len > $maxlength;
        $return_data = substr ${$state->{data}}, $state->{bytes}, $data_len;
        $state->{bytes} += $data_len;
    }
    return $return_data;
}

# Callback for writing the body i