%define upstream_name       Test-Manifest

Name:		perl-%{upstream_name}
Version:	2.023
Release:	1
Summary:	Interact with a t/test_manifest file

License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{version}.tar.gz
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
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/man3/*
