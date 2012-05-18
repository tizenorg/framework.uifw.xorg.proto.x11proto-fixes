
Name:       xorg-x11-proto-fixesproto
Summary:    X.Org X11 Protocol fixesproto
Version:    4.1.2
Release:    1.1
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/fixesproto-%{version}.tar.gz
Provides:   fixesproto
BuildRequires: pkgconfig(xorg-macros)


%description
Xorg X11 Protocol fixesproto



%prep
%setup -q -n %{name}-%{version}

%build

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install







%files
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/fixesproto.pc
%{_includedir}/X11/extensions/xfixeswire.h
%{_includedir}/X11/extensions/xfixesproto.h
%doc %{_datadir}/doc/fixesproto


