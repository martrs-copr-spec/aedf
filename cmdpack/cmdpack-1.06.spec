Name:           cmdpack
Version:        1.06
Release:        1%{?dist}
Summary:        Collection of command line utilities, most for emulation or disk images

License:        GPLv3
URL:            http://www.neillcorlett.com/cmdpack
Source0:        https://github.com/chungy/cmdpack/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc glibc-devel asciidoc

%description  
These are a set of utilities originally released by Neill Corlett
(http://www.neillcorlett.com/cmdpack/), but the upstream has since vanished
from the web. This is based on Neill's last version, 1.03.

Mike Swanson cleaned up the utilities at least a little bit. So far, the most
major change is ecm’s name change to bin2ecm, and requires being called with
a name of ecm2bin to do the reverse operation now. Past versions of cmdpack
included some utilities that have been deleted, deemed redundant by, and
worse than, alternative programs.

%prep
%autosetup


%build
%make_build

%install
%make_install prefix=%{_prefix}


%files
%license COPYING
%doc README.adoc
%{_bindir}/bin2ecm
%{_bindir}/ecm2bin
%{_bindir}/bincomp
%{_bindir}/brrrip
%{_bindir}/byteshuf
%{_bindir}/cdpatch
%{_bindir}/fakecrc
%{_bindir}/hax65816
%{_bindir}/pecompat
%{_bindir}/rels
%{_bindir}/screamf
%{_bindir}/uips
%{_bindir}/vb2rip
%{_bindir}/wordadd
%{_mandir}/man1/*.1.gz

%changelog
* Sun May 11 2025 Martin RS - 1.06
- update
* Wed Nov 17 2021 Martin RS - 1.03
- Initial for Fedora
* Sun Jun 03 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 1.03-1
- Initial release 1.03
