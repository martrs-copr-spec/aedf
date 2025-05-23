Name: iat
Version: 0.1.7
Release: 1%{?dist}
License: GPLv3
Summary: iso9660 analyzer tool
Source: https://sourceforge.net/projects/iat.berlios/files/%{name}-%{version}.tar.bz2
BuildRequires: gcc-c++ glibc-devel

%description
Iso9660 Analyzer Tool is a free utility tool for detecting the
structure of DVD/ CD-ROM image file formats; the tool supports many CD/DVD-ROM
data image file formats.

%prep
%setup -q
sed -i -e '/^install-data-am:\s\+install-includeHEADERS/s/^/#/' \
    src/Makefile.in

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog INSTALL NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Jun 28 2020 Martin RS - 0.1.7
- Initial for Fedora
