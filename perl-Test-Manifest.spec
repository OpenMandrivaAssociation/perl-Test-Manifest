%define real_name Test-Manifest

Summary:	Test::Manifest - interact with a t/test_manifest file
Name:		perl-%{real_name}
Version:	1.17
Release: %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Pod
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

In t/test_manifest, simply list the tests that you want to run.  Their
order in the file is the order in which they run.  You can comment
lines with a #, just like in Perl, and Test::Manifest will strip
leading and trailing whitespace from each line.  It also checks that
the specified file is actually in the t/ directory.  If the file does
not exist, it does not put its name in the list of test files to run.

Optionally, you can add a number after the test name in test_manifest
to define sets of tests. See get_t_files() for more information.

%prep
%setup -q -n %{real_name}-%{version} 

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
%{perl_vendorlib}/Test/Manifest.pm
%{_mandir}/*/*


