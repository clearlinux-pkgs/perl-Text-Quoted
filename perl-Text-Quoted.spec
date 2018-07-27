#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Quoted
Version  : 2.10
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/B/BP/BPS/Text-Quoted-2.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BP/BPS/Text-Quoted-2.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-quoted-perl/libtext-quoted-perl_2.09-2.debian.tar.xz
Summary  : 'Extract the structure of a quoted mail message'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Quoted-license
Requires: perl-Text-Quoted-man
BuildRequires : buildreq-cpan
BuildRequires : perl(Text::Autoformat)
BuildRequires : perl(Text::Reform)

%description
NAME
Text::Quoted - Extract the structure of a quoted mail message
SYNOPSIS
use Text::Quoted;
my $structure = extract($text);

%package license
Summary: license components for the perl-Text-Quoted package.
Group: Default

%description license
license components for the perl-Text-Quoted package.


%package man
Summary: man components for the perl-Text-Quoted package.
Group: Default

%description man
man components for the perl-Text-Quoted package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Text-Quoted-2.10
mkdir -p %{_topdir}/BUILD/Text-Quoted-2.10/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Text-Quoted-2.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Text-Quoted
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-Text-Quoted/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Text/Quoted.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Text-Quoted/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Quoted.3
