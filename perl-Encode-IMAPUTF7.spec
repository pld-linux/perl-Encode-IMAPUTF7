#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define		pdir	Encode
%define		pnam	IMAPUTF7
Summary:	Encode::IMAPUTF7 - modification of UTF-7 encoding for IMAP
Name:		perl-Encode-IMAPUTF7
Version:	1.05
Release:	1
License:	Perl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ef9d1a438f3fa29771d24f9e587fd2a
URL:		https://metacpan.org/dist/Encode-IMAPUTF7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-NoWarnings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modification of UTF-7 encoding for IMAP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Encode/IMAPUTF7.pm
%{_mandir}/man3/Encode::IMAPUTF7.3*
