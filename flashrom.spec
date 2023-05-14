%define debug_package %{nil}

Summary:	Utility which can be used to detect/read/write BIOS chips
Name:		flashrom
Epoch:		1
Version:	1.3.0
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://flashrom.org
Source0:	http://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2
# upstream already: https://review.coreboot.org/c/flashrom/+/38939
Patch0:		0001-Install-the-man-file-when-using-meson-as-a-buildsyst.patch
# upstreamed: https://review.coreboot.org/c/flashrom/+/48478
Patch1:		0002-meson-Add-missing-config-option-for-J-Link-SPI.patch
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
sed -e 's/MODE="[0-9]*", GROUP="plugdev"/TAG+="uaccess"/g' util/z60_flashrom.rules -i

%build
%meson \
%ifarch %{ix86} x86_64
  -Dconfig_jlink_spi=false \
  -Dconfig_internal=true
%else
  -Dconfig_atahpt=false \
  -Dconfig_atapromise=false \
  -Dconfig_atavia=false \
  -Dconfig_drkaiser=false \
  -Dconfig_gfxnvidia=false \
  -Dconfig_it8212=false \
  -Dconfig_jlink_spi=false \
  -Dconfig_nic3com=false \
  -Dconfig_nicintel_eeprom=false \
  -Dconfig_nicintel=false \
  -Dconfig_nicintel_spi=false \
  -Dconfig_nicnatsemi=false \
  -Dconfig_nicrealtek=false \
  -Dconfig_ogp_spi=false \
  -Dconfig_rayer_spi=false \
  -Dconfig_satamv=false \
  -Dconfig_satasii=false \
  -Dconfig_internal=false
%endif

%meson_build

%install
%meson_install

install -D -p -m 0644 util/z60_flashrom.rules %{buildroot}/%{_udevrulesdir}/60_flashrom.rules

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
