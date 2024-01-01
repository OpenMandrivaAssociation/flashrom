%define debug_package %{nil}
%global build_ldflags %{build_ldflags} -Wl,--undefined-version

Summary:	Utility which can be used to detect/read/write BIOS chips
Name:		flashrom
Epoch:		1
Version:	1.3.0
Release:	2
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://flashrom.org
Source0:	http://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2

BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	meson
#BuildRequires:	libjaylink-devel
BuildRequires:	pkgconfig(libftdi1)
BuildRequires:	systemd-rpm-macros
%ifarch %{ix86} %{x86_64} %{armx}
BuildRequires:	dmidecode
Requires:	dmidecode
%endif
Requires:	udev

%description
Flashrom is a utility which can be used to detect BIOS chips (DIP, PLCC),
read their contents and write new contents on the chips ("flash the chip").

%package devel
Summary:	Development package for %{name}
Requires:	%{name} = %{EVRD}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}
# Replace GROUP="plugdev" specifiers with TAG+="uaccess"
sed -e 's/MODE="[0-9]*", GROUP="plugdev"/TAG+="uaccess"/g' util/flashrom_udev.rules -i

%build
%meson -Dtests=disabled
%meson_build

%install
%meson_install

install -D -p -m 0644 util/flashrom_udev.rules %{buildroot}/%{_udevrulesdir}/60_flashrom.rules            
rm %{buildroot}/%{_libdir}/libflashrom.a

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%doc %{_mandir}/man8/%{name}.*
%{_udevrulesdir}/60_flashrom.rules
%{_libdir}/libflashrom.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
