Name:           sfarkxtc
Version:        3.0
Release:        3%{?dist}
Summary:        sfArk extractor, console version

License:        GPLv3
URL:            https://github.com/raboof/sfarkxtc
Source0:        https://github.com/raboof/sfarkxtc/archive/master.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ glibc-devel
BuildRequires:  sfarklib-devel

%description
Converts soundfonts in the legacy sfArk v2 file format to sf2.

%prep
%autosetup -n %{name}-master
sed -i Makefile -e 's:/usr/local/bin:%{_bindir}:'


%build
%make_build


%install
%make_install


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}


%changelog
* Sun Dec 26 2021 Martin RS - 3.0
- Initial for Fedora
