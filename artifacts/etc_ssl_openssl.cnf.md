#
# OpenSSL example configuration file.
# See doc/man5/config.pod for more info.
#
# This is mostly being used for generation of certificate requests,
# but may be used for auto loading of providers

# Note that you can include other files from the main configuration
# file using the .include directive.
#.include filename

# This definition stops the following lines choking if HOME isn't
# defined.
HOME			= .

# Use this in order to automatically load providers.
openssl_conf = openssl_init

# Comment out the next line to ignore configuration errors
config_diagnostics = 1

# Extra OBJECT IDENTIFIER info:
# oid_file       = $ENV::HOME/.oid
oid_section = new_oids

# To use this configuration file with the "-extfile" option of the
# "openssl x509" utility, name here the section containing the
# X.509v3 extensions to use:
# extensions		=
# (Alternatively, use a configuration file that has only
# X.509v3 extensions in its main [= default] section.)

[ new_oids ]
# We can add new OIDs in here