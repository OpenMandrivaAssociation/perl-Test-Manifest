%define upstream_name       Test-Manifest
%define upstream_version    1.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Interact with a t/test_manifest file
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz
Patch:      Test-Manifest-1.23-force-man-pages.patch
BuildRequires:	perl-Test-Pod
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/man3/*

