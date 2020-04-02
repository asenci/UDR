Name:		udr
Version:	0.9.4
Release:	26%{?dist}
Summary:	Wrapper around rsync that enables rsync to use UDT

Group:		Development/Libraries
License:	Apache v2
URL:		https://github.com/LabAdvComp/UDR

Source:		https://github.com/asenci/UDR/archive/v%{version}.tar.gz

BuildRequires:	make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libudt-devel > 4.10
BuildRequires:  openssl-devel > 1.0

Requires: libudt > 4.10
Requires: openssl-libs > 1.0

ExclusiveOS:	linux
ExclusiveArch:	x86_64

%description
UDR is a wrapper around rsync that enables rsync to use UDT


%prep
%setup -q -c

%build
pushd UDR-%{version}/src
%{__make} -e os=LINUX arch=AMD64

%install
%{__install} -d %{buildroot}%{_bindir}
%{__install} UDR-%{version}/src/udr %{buildroot}%{_bindir}

%files
%defattr(755,root,root,755)
%{_bindir}/udr

%clean
%{__rm} -rf %{buildroot}


# Changelog
%changelog
* Thu Apr 02 2020 Andre Sencioles <asenci@gmail.com> - 0.9.4-24
- Initial release
