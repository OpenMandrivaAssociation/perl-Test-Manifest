%define upstream_name       Test-Manifest
%define upstream_version    1.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Summary:	Interact with a t/test_manifest file
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz
Patch:		Test-Manifest-1.23-force-man-pages.patch
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Test::Harness assumes that you want to run all of the .t files in the
t/ directory in ascii-betical order during make test unless you say
otherwise.  This leads to some interesting naming schemes for test
files to get them in the desired order. This interesting names ossify
when they get into source control, and get even more interesting as
more tests show up.

Test::Manifest overrides the default behaviour by replacing the
test_via_harness target in the Makefile.  Instead of running at the
t/*.t files in ascii-betical order, it looks in the t/test_manifest
file to find out which tests you want to run and the order in which
you want to run them.  It constructs the right value for MakeMaker to
do the right thing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch -p 1

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.230.0-4mdv2012.0
+ Revision: 765693
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.230.0-3
+ Revision: 764235
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.230.0-2
+ Revision: 667327
- mass rebuild

* Sun Jul 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.230.0-1mdv2011.0
+ Revision: 397435
- new version
- use %%perl_convert_version macro
- better summary and description

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.22-2mdv2009.0
+ Revision: 224136
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Nov 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.22-1mdv2008.1
+ Revision: 104269
- 1.22

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2008.1
+ Revision: 98036
- update to new version 1.21
- update to new version 1.21


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 1.17-1mdv2007.0
+ Revision: 131713
- 1.17

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Test-Manifest

* Tue Apr 04 2006 Buchan Milne <bgmilne@mandriva.org> 1.14-2mdk
- Rebuild
- use mkrel

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 1.14-1mdk
- initial Mandriva package

