%global debug_package %nil

Name:           novi
Version:        2.1.2
Release:        3%{?dist}
Summary:        find the latest-version RPMs in a tree

License:        Apache 2.0
URL:            http://www.ExMachinaTech.net
Source0:        https://github.com/martrs-wayback/novi/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Vendor:         Q Ethan McCallum, ExMachinaTech.net
Group:          Utilities

BuildRequires:  gcc-c++ glibc-devel
BuildRequires:  expat-devel
BuildRequires:  popt
BuildRequires:  rpm-devel >= 4.6
BuildRequires:  zlib-devel
Requires:       popt

%description
novi searches directories for the latest-version RPMs of each product.

In turn, this data can be used to:
- see what are the latest RPMs on your system
- fold the latest RPMs into a Kickstart tree, such that you can
  build systems with the updates already applied

This process is described in much greater (and better) detail in the
following article on the O\'Reilly Network:

"Pre-Patched Kickstart Installs"
http://www.linuxdevcenter.com/pub/a/linux/2005/02/17/kickstart_updates.html

%prep
%autosetup
sed -i Makefile.in \
  -e 's/^\(INSTALL.*\)555/\1755/' \
  -e 's/^\(INSTALL.*\)444/\1644/' \
  -e 's/^\(CXXFLAGS\s\+=\)/\1 -std=c++03/'


%build
%configure
%make_build


%install
%make_install ALT_ROOT_DIR=${RPM_BUILD_ROOT}


%files
%doc EXAMPLES.TXT FAQ.TXT INSTALL.TXT LICENSE README.TXT WISHLIST.TXT
%doc doc/novi.1.html doc/novi_examples.1.html
%{_bindir}/%name
%{_mandir}/man1/novi.1.gz
%{_mandir}/man1/novi_examples.1.gz


%changelog
* Thu Dec 10 2015 Martin RS - 2.1.2
- update from Fedora 16 src.rpm
