%define		pdir	Language
%define		pnam	Prolog-Interpreter
%include	/usr/lib/rpm/macros.perl
Summary:	Language::Prolog::Interpreter module replacement
Summary(pl.UTF-8):	Inna wersja modułu Language::Prolog::Interpreter
Name:		perl-Language-Prolog-Interpreter-new
Version:	0.021
Release:	4
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1159b02e61855b16d1b1a1eed63538f7
URL:		http://search.cpan.org/dist/Language-Prolog-Interpreter/
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Od dawna pozostawiony bez opieki moduł Language::Prolog ma wciąż duży
potencjał. Ten pakiet jest zamiennikiem dla modułu Interpreter z
głównego pakietu. Pozwala na czytanie plików zawierających jedno- lub
wieloliniowe warunki.

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
