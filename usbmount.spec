Name: usbmount 
Version: 1.2.3  
Release: 1.tsinghua
Summary: automount USB drives with systemd
Group: Applications/System
License: GPLv3+
URL: https://github.com/DaiZhiyuan/usbmount
Source0: %{name}-%{version}.tar.gz
Packager: Jerry Dai

BuildRequires: bash
Requires: systemd
Requires: gawk 
Requires: sed 
Requires: grep  
Requires: util-linux

%description
On inserting an USB drive, automounts the drive at /media/ as a
directory named by device label; just the device name if label is
empty: /media/sdb1.

%prep
%setup -q

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT/%{_bindir}
%{__mkdir_p} $RPM_BUILD_ROOT/%{_unitdir}
%{__mkdir_p} $RPM_BUILD_ROOT/%{_udevrulesdir}
install -m 755 usbmount $RPM_BUILD_ROOT/%{_bindir}
install -m 644 usbmount@.service $RPM_BUILD_ROOT/%{_unitdir}
install -m 644 99-local.rules $RPM_BUILD_ROOT/%{_udevrulesdir}

%files
%{_bindir}/usbmount
%{_unitdir}/usbmount@.service
%{_udevrulesdir}/99-local.rules

%post
systemctl daemon-reload
udevadm control --reload-rules

%changelog
* Thu Aug 16 2018 Jerry Dai <daizhiyuan@tsinghua.edu.cn> - 1.2.3-1
- initialize package
