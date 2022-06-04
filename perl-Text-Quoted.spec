#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Quoted
Version  : 2.10
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/B/BP/BPS/Text-Quoted-2.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BP/BPS/Text-Quoted-2.10.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-quoted-perl/libtext-quoted-perl_2.09-2.debian.tar.xz
Summary  : 'Extract the structure of a quoted mail message'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Quoted-license = %{version}-%{release}
Requires: perl-Text-Quoted-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Text::Autoformat)
BuildRequires : perl(Text::Reform)

%description
NAME
Text::Quoted - Extract the structure of a quoted mail message
SYNOPSIS
use Text::Quoted;
my $structure = extract($text);

%package dev
Summary: dev components for the perl-Text-Quoted package.
Group: Development
Provides: perl-Text-Quoted-devel = %{version}-%{release}
Requires: perl-Text-Quoted = %{version}-%{release}

%description dev
dev components for the perl-Text-Quoted package.


%package license
Summary: license components for the perl-Text-Quoted package.
Group: Default

%description license
license components for the perl-Text-Quoted package.


%package perl
Summary: perl components for the perl-Text-Quoted package.
Group: Default
Requires: perl-Text-Quoted = %{version}-%{release}

%description perl
perl components for the perl-Text-Quoted package.


%prep
%setup -q -n Text-Quoted-2.10
cd %{_builddir}
tar xf %{_sourcedir}/libtext-quoted-perl_2.09-2.debian.tar.xz
cd %{_builddir}/Text-Quoted-2.10
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Text-Quoted-2.10/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Quoted
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Text-Quoted/6cdf787a274af49fe2e242c3aa39c007dc57f844
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Quoted.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Quoted/6cdf787a274af49fe2e242c3aa39c007dc57f844

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
