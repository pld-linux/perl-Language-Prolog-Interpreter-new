%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	Prolog-Interpreter
Summary:	Language::Prolog::Interpreter module replacement
Summary(pl):	Inna wersja modu�u Language::Prolog::Interpreter
Name:		perl-Language-Prolog-Interpreter-new
Version:	0.021
Release:	2
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1159b02e61855b16d1b1a1eed63538f7
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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
Od dawna pozostawiony bez opieki modu� Language::Prolog ma wci�� du�y
potencja�. Ten pakiet jest zamiennikiem dla modu�u Interpreter z
g��wnego pakietu. Pozwala na czytanie plik�w zawieraj�cych jedno-
lub wieloliniowe warunki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Language/Prolog/Interpreter.pm
%{_mandir}/man3/*
