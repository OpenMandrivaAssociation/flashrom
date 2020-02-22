%define debug_package %{nil}

Summary:	Utility which can be used to detect/read/write BIOS chips
Name:		flashrom
Epoch:		1
Version:	1.2
Release:	1
Source0:	http://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://flashrom.org
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel
BuildRequires:	glibc-static-devel

%description
Flashrom is a utility which can be used to detect BIOS chips (DIP, PLCC),
read their contents and write new contents on the chips ("flash the chip").

%prep
%setup -q -n %{name}-v%{version}

%build
%make_build CFLAGS="%optflags" PREFIX=%_prefix 

%install
#install -dm755 %buildroot%_sbindir
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%{_sbindir}/*
%{_mandir}/man8/*
