Name:           ecmtools
Version:        1.3.1
Release:        1%{?dist}
Summary:        ECM encode/decode utilities

License:        GPLv2
URL:            http://www.neillcorlett.com/ecm/
Source0:        https://github.com/kidoz/ecm/archive/v%{version}.tar.gz/#%{name}-%{version}.tar.gz
BuildRequires:  gcc glibc-devel meson

%description
The ECM format allows you to reduce the size of a typical CD image file
(BIN, CDI, NRG, CCD, or any other format that uses raw sectors; results may
vary).

It works by eliminating the Error Correction/Detection Codes (ECC/EDC) from
each sector whenever possible. The encoder automatically adjusts to
different sector types and automatically skips any headers it encounters.


%prep
%autosetup -n ecm-%{version}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license LICENSE AUTHORS.md CHANGELOG.md
%doc README.md doc/FORMAT.md
%{_bindir}/ecm
%{_bindir}/unecm


%changelog
* Sat May 2 2026 Martin RS - 1.3.1
- 1.3.1
* Sun Jul 5 2020 Martin RS - 1.0git20180207
- Initial for Fedora, fix install
* Wed Jan 15 2014 bb <bb> 1.0-2pclos2014
- fix rpmgroup
* Fri Aug 23 2013 Agent Smith <ruidobranco@yahoo.com.br> 1.0-1pclos2012
- Created package ecmtools
