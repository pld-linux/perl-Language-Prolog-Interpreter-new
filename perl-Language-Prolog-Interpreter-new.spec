%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	Prolog-Interpreter
Summary:	Language::Prolog::Interpreter module replacement
Summary(pl):	Inna wersja modu³u Language::Prolog::Interpreter
Name:		perl-Language-Prolog-Interpreter-new
Version:	0.021
Release:	1
Epoch:		1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-Language-Prolog
Obsoletes:	perl-Language-Prolog-Interpreter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An apparently untended module, Language::Prolog has all sorts of
potential. This distribution is a replacement for the main
distribution's *Interpreter* module, and allows the reading of files,
which may contain multi-line clauses, single- or multi-line clauses.

%description -l pl
Od dawna pozostawiony bez opieki modu³ Language::Prolog ma wci±¿ du¿y
potencja³. Ten pakiet jest zamiennikiem dla modu³u Interpreter z
g³ównego pakietu. Pozwala na czytanie plików zawieraj±cych jedno-
lub wieloliniowe warunki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.txt
%{perl_sitelib}/Language/Prolog/Interpreter.pm
%{_mandir}/man3/*
